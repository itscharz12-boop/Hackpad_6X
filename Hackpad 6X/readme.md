# Hackpad 6x

Hackpad 6x is a multi-profile macropad designed to act as an all-purpose desktop control pad. Instead of relying on a large number of physical keys, it uses multiple profiles, a rotary encoder, an OLED display, RGB lighting, and PC telemetry to turn a compact set of inputs into a flexible control surface for media, desktop shortcuts, gaming, and numpad functions.

The goal of this project was to create an “infinite keys” style macropad: a device where a small number of physical inputs can perform a much larger range of tasks through layers.

Hackpad 6x was designed as an omnipurpose desktop macropad rather than a single-purpose keypad. The focus of the project was flexibility: combining multiple profiles, a rotary encoder, OLED feedback, RGB lighting, and PC-side telemetry to make a compact but highly adaptable control device.

---
## Quick Start

1. **Build the hardware** — Assemble the macropad using the PCB, case, switches, and other components listed in the BOM
2. **Flash the firmware** — Install QMK and flash the firmware to the Seeed XIAO RP2040
3. **Install software** — Set up the HackpadDataLink Python script on your PC
4. **Configure profiles** — Customize keybinds and OLED graphics as needed
5. **Enjoy!** — Use the rotary encoder to switch between profiles

---

## Features

- Multi-profile layout system for different use cases
- Rotary encoder with push button for quick control input
- OLED display with profile-specific graphics and live system information
- RGB lighting effects with multiple selectable modes
- Media and desktop shortcut controls
- Dual numpad layers for keybinds in games or editors when using 60, 65, 70% keyboards etc.
- Gaming profile for commonly used controls
- PC telemetry support displaying:
  - CPU usage
  - GPU usage
  - System volume
  - Display brightness

---

## Profiles

Hackpad 6x uses 5 profiles:

- Layer 0 — Home / Base
- Layer 1 — Media / Screen Control
- Layer 2 — Numpad A
- Layer 3 — Numpad B
- Layer 4 — Gaming


---

## Hardware

Hackpad 6x is built around a Seeed XIAO RP2040 and includes:

- 8 Cherry MX switches
- 8 keycaps
- 1 rotary encoder with push button
- 1 0.91" OLED display
- 18 RGB LEDs
- 9 diodes
- 6 M3 screws
- 6 M3 heat-set inserts
- Custom 2-layer PCB
- 3D printed case

---

## Bill of Materials (BOM)

| Part                                 | Quantity |
| ------------------------------------ | -------: | 
| Seeed XIAO RP2040                    |        1 | 
| Cherry MX switches                   |        8 |
| Keycaps                              |        8 |
| EC11 rotary encoder with push button |        1 |
| 0.91" OLED display                   |        1 | 
| RGB LEDs                             |       18 |
| Diodes                               |        9 |
| Custom PCB                           |        1 | 
| 3D printed case (BASE + TOP)         |        1 | 
| M3 screws                            |        6 | 
| M3 heatset inserts                   |        6 | 
| Encoder knob                         |        1 | 

---

## Setup & Assembly

### Prerequisites

- QMK firmware toolchain (https://docs.qmk.fm/newbs)
- Python 3.7+ (for HackpadDataLink)
- Git
- Soldering iron and solder

### Assembly Instructions

1. **PCB Assembly**: Solder all components to the PCB according to the manufacturing files
   - Install diodes, rotary encoder, and OLED display
   - Mount the Seeed XIAO RP2040 microcontroller

2. **Switch Installation**: Insert Cherry MX switches into the PCB and secure with keycaps

3. **Case Assembly**: 
   - Install M3 heatset inserts into the 3D printed case pieces
   - Assemble top and bottom case pieces
   - Secure with M3 screws

4. **Testing**: Connect via USB and verify all switches, encoder, and display are working

### Firmware Flashing

1. Clone or download the firmware files from this project
2. Install QMK: `pip install qmk`
3. Set up QMK environment: `qmk setup`
4. Navigate to the firmware directory
5. Flash to the device: `qmk flash -kb hackpad6x -km default`
6. Press the reset button on the XIAO RP2040 when prompted

### Software Setup

1. Install Python dependencies: `pip install -r requirements.txt`
2. Run HackpadDataLink: `python hackpad_datalink.py`
3. The script will automatically detect and connect to the macropad

---

## Firmware

Hackpad 6x uses QMK firmware.

The firmware includes:

- Profile switching
- Encoder modifier behaviour
- RGB mode switching
- OLED profile graphics
- RAW HID support for PC telemetry

If you would like to add/edit any layers, you can edit the firmware and modify the OLED profiles included in the "other" folder, covert them into a bitmap, and add them to the code.

### Configuration Guide

**Customizing Keybinds:**
- Edit the keymap files in the firmware `keymaps` directory
- Modify keycodes for each layer (0-4)
- Refer to QMK documentation for available keycodes
- Re-flash the firmware after making changes

**Customizing OLED Graphics:**
- Design or edit graphics for each profile
- Convert images to bitmap format
- Place bitmap files in the designated folder
- Update the firmware to reference new graphics

**RGB Lighting:**
- Modify RGB animations in the firmware configuration
- Adjust color schemes and animation speeds
- Changes take effect after re-flashing

---

## Hackpad DataLink

A Python script running on the PC sends telemetry values to the macropad over USB, which are then displayed and used by the firmware.

### Telemetry Values

- CPU usage
- GPU usage
- Volume percentage
- Brightness percentage

---

## Production Files

The "production" folder contains the manufacturing and build files needed to physically assemble the project:

- **gerbers.zip** — PCB manufacturing files
- **case.stl** — Exported printable case parts

---

Images can be found in the "Images" folder.

---

## File Structure

hackpad-6x/
├── firmware/              # QMK firmware source code
├── hackpad_datalink/      # Python PC telemetry script
├── production/            # Manufacturing files
│   ├── gerbers.zip        # PCB manufacturing files
│   └── case.stl          # 3D printable case parts
├── other/                 # Additional files
│   ├── OLED_profiles/     # Profile graphics and bitmaps
│   └── reference/        # Documentation and design files
├── images/                # Project photos and diagrams
README.md                 # you are here :)


---

Hackpad 6x was designed and built as a personal project. Special thanks to Hack Club for creating the awesome program behind this!


