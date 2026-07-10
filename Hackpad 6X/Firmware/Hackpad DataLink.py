import time
import hid
import psutil
import screen_brightness_control as sbc

from pynvml import *

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume



# =========================
# Find Hackpad RAW HID
# =========================

VID = 0xCAFE   # change this
PID = 0x4000   # change this


device = None


def connect():

    global device

    try:

        device = hid.device()
        device.open(
            VID,
            PID
        )

        print("Hackpad connected")

    except Exception:

        device = None
        print("Hackpad not found")



# =========================
# GPU
# =========================

try:
    nvmlInit()
    gpu = nvmlDeviceGetHandleByIndex(0)
except:
    gpu = None



# =========================
# Stats
# =========================

def get_cpu():

    return int(
        psutil.cpu_percent()
    )



def get_gpu():

    if gpu is None:
        return 0

    try:

        return int(
            nvmlDeviceGetUtilizationRates(gpu).gpu
        )

    except:

        return 0



def get_volume():

    try:

        speakers = AudioUtilities.GetSpeakers()

        interface = speakers.Activate(
            IAudioEndpointVolume._iid_,
            CLSCTX_ALL,
            None
        )

        volume = cast(
            interface,
            POINTER(IAudioEndpointVolume)
        )

        return int(
            volume.GetMasterVolumeLevelScalar()
            * 100
        )

    except:

        return 0



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

print("Telemetry started")


while True:


    if device is None:

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



    print(
        "CPU:",
        cpu,
        "GPU:",
        gpu_usage,
        "VOL:",
        vol,
        "BRI:",
        bright
    )


    if device:


        try:

            # RAW HID packet
            packet = [
                0,          # report ID
                cpu,
                gpu_usage,
                vol,
                bright
            ]

            device.write(
                packet
            )


        except:

            print(
                "Disconnected"
            )

            device = None



    time.sleep(0.25)