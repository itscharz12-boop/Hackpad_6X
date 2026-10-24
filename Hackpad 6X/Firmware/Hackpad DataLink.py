import logging
import sys
import time

logger = logging.getLogger("hackpad_datalink")
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
if sys.stdout is not None:
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
else:
    logger.addHandler(logging.NullHandler())


def log_uncaught_exception(exc_type, exc_value, exc_traceback):
    logger.critical("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))


sys.excepthook = log_uncaught_exception

import hid
import psutil
import screen_brightness_control as sbc

from pynvml import NVMLError, nvmlDeviceGetHandleByIndex, nvmlDeviceGetUtilizationRates, nvmlInit

from pycaw.pycaw import AudioUtilities



# =========================
# Find Hackpad RAW HID
# =========================

VID = 0xFEED
PID = 0x1206
RAW_USAGE_PAGE = 0xFF60
RAW_USAGE_ID = 0x61
RECONNECT_INTERVAL_SECONDS = 1
MISSING_NOTICE_INTERVAL_SECONDS = 5
ACK_TIMEOUT_MS = 50
MISSED_ACK_LIMIT = 3


device = None
device_path = None
missed_ack_count = 0
link_verified = False
last_connect_attempt = 0.0
last_presence_check = 0.0
last_missing_notice = 0.0
last_link_warning = 0.0
volume_endpoint = None
last_volume_level = 0
volume_read_failed = False


def raw_hid_interfaces():
    return [
        interface
        for interface in hid.enumerate(VID, PID)
        if interface.get("usage_page") == RAW_USAGE_PAGE
        and interface.get("usage") == RAW_USAGE_ID
    ]


def connect():
    global device, device_path, last_missing_notice, missed_ack_count, link_verified

    candidate = None
    try:
        raw_interfaces = raw_hid_interfaces()
        if not raw_interfaces:
            now = time.monotonic()
            if now - last_missing_notice >= MISSING_NOTICE_INTERVAL_SECONDS:
                logger.warning(
                    "Hackpad Raw HID interface not found. Retrying automatically; "
                    "check RAW_ENABLE and flash the updated firmware if needed."
                )
                last_missing_notice = now
            return False

        candidate = hid.device()
        candidate.open_path(raw_interfaces[0]["path"])
        device = candidate
        device_path = raw_interfaces[0]["path"]
        missed_ack_count = 0
        link_verified = False
        logger.info("Hackpad Raw HID interface opened; checking keyboard firmware link")
        return True
    except OSError as error:
        if candidate is not None:
            try:
                candidate.close()
            except OSError as close_error:
                logger.error("Could not close failed Hackpad HID handle: %s", close_error)
        device = None
        device_path = None
        missed_ack_count = 0
        link_verified = False
        logger.error("Could not open Hackpad Raw HID interface: %s", error)
        return False


def close_device(message):
    global device, device_path, missed_ack_count, link_verified

    if device is not None:
        try:
            device.close()
        except OSError as error:
            logger.error("Could not close Hackpad Raw HID handle: %s", error)
    device = None
    device_path = None
    missed_ack_count = 0
    link_verified = False
    logger.info(message)


def check_device_presence():
    global last_presence_check

    if device is None:
        return

    now = time.monotonic()
    if now - last_presence_check < RECONNECT_INTERVAL_SECONDS:
        return
    last_presence_check = now

    try:
        paths = {interface["path"] for interface in raw_hid_interfaces()}
    except OSError as error:
        logger.error("Could not check Hackpad Raw HID presence: %s", error)
        return

    if device_path not in paths:
        close_device("Hackpad Raw HID disconnected")



# =========================
# GPU
# =========================

gpu = None
last_gpu_usage = 0
gpu_read_failed = False

try:
    nvmlInit()
    gpu = nvmlDeviceGetHandleByIndex(0)
except NVMLError as error:
    logger.warning("NVIDIA GPU telemetry unavailable: %s", error)
except Exception as error:
    logger.warning("NVIDIA GPU telemetry unavailable: %s", error)



# =========================
# Stats
# =========================

def get_cpu():
    return round(psutil.cpu_percent())



def get_gpu():
    global last_gpu_usage, gpu_read_failed

    if gpu is None:
        return last_gpu_usage

    try:
        last_gpu_usage = max(0, min(100, int(nvmlDeviceGetUtilizationRates(gpu).gpu)))
        if gpu_read_failed:
            logger.info("NVIDIA GPU telemetry recovered")
        gpu_read_failed = False
        return last_gpu_usage
    except NVMLError as error:
        if not gpu_read_failed:
            logger.warning("Could not read NVIDIA GPU utilization; keeping last value: %s", error)
        gpu_read_failed = True
        return last_gpu_usage



def get_volume():
    global volume_endpoint, last_volume_level, volume_read_failed

    try:
        if volume_endpoint is None:
            volume_endpoint = AudioUtilities.GetSpeakers().EndpointVolume

        scalar = volume_endpoint.GetMasterVolumeLevelScalar()
        last_volume_level = max(0, min(100, round(scalar * 100)))
        if volume_read_failed:
            logger.info("Windows master-volume telemetry recovered")
        volume_read_failed = False
        return last_volume_level
    except Exception as error:
        volume_endpoint = None
        if not volume_read_failed:
            logger.warning("Could not read Windows master volume; keeping last value: %s", error)
        volume_read_failed = True
        return last_volume_level



def get_brightness():

    try:

        return int(
            sbc.get_brightness()[0]
        )

    except:

        return 0



# =========================
# Main
# =========================

logger.info("Telemetry started")


while True:

    now = time.monotonic()
    check_device_presence()
    if device is None and now - last_connect_attempt >= RECONNECT_INTERVAL_SECONDS:
        last_connect_attempt = now
        connect()


    cpu = min(
        100,
        get_cpu()
    )

    gpu_usage = min(
        100,
        get_gpu()
    )

    vol = min(
        100,
        get_volume()
    )

    bright = min(
        100,
        get_brightness()
    )




    logger.info("CPU: %s GPU: %s VOL: %s BRI: %s", cpu, gpu_usage, vol, bright)


    if device:
        try:
            packet = [
                0,          # report ID
                cpu,
                gpu_usage,
                vol,
                bright
            ] + [0] * 28

            written = device.write(packet)
            if written != len(packet):
                raise OSError(f"incomplete HID write ({written}/{len(packet)} bytes)")

            response = device.read(32, timeout_ms=ACK_TIMEOUT_MS)
            if response[:4] == packet[1:5]:
                missed_ack_count = 0
                if not link_verified:
                    link_verified = True
                    logger.info("Hackpad telemetry link verified")
            else:
                missed_ack_count += 1
                if missed_ack_count >= MISSED_ACK_LIMIT and time.monotonic() - last_link_warning >= MISSING_NOTICE_INTERVAL_SECONDS:
                    logger.warning(
                        "Hackpad interface is present but firmware did not acknowledge telemetry. "
                        "Build and flash firmware with RAW_ENABLE = yes and the Raw HID echo enabled."
                    )
                    last_link_warning = time.monotonic()
        except OSError as error:
            close_device(f"Hackpad telemetry link lost: {error}")



    time.sleep(0.25)