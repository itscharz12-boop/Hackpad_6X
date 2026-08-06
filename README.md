# Hackpad 6x

Hackpad 6x is a small but very over-engineered macropad that I designed because apparently a normal keyboard was not enough :)

The idea was to make a compact control pad that could do a bit of everything: media controls, shortcuts, gaming controls, numpad functions, and displaying useless (but cool) information from my PC.

Basically, I wanted an "infinite keys" macropad where a few buttons could become a lot of buttons through layers.

(Yes, this did start as "I'll just make a simple macropad" and then somehow became OLEDs, RGB, and a PC monitoring system. I have no idea how this happened.)

Images of this hackpad can be found in the "images" folder.

Showcase Video (For Hack Club's Stardance event) also available at this link:
https://drive.google.com/file/d/1NDWkFQftZgt32tnkIbqYFETVVm34cNFE/view?usp=sharing

---

# Quick Start

To build this:

1. **Build the hardware**
   - Assemble the PCB, switches, encoder, OLED and case.
   - (Of course you need a soldering iron for soldering. Unfortunately staring at the PCB does not make the components attach themselves.)

2. **Flash the firmware**
   - Install QMK and flash the firmware onto the Seeed XIAO RP2040.

3. **Install HackpadDataLink**
   - Run the Python script on your PC to send system information to the OLED.

---

# Features

- 5 different profiles/layers
- Rotary encoder with push button
- OLED display
- RGB lighting
- PC telemetry

The PC telemetry shows:
- CPU usage
- GPU usage
- Volume
- Brightness

(Useful for checking your PC performance without moving your eyes approximately 20cm up to look at your monitor.)

---

# Hardware

The hackpad is built around a Seeed XIAO RP2040.

Parts:

- Seeed XIAO RP2040
- 8x Cherry MX switches
- 8x keycaps
- EC11 rotary encoder
- OLED display
- RGB LEDs
- Custom PCB
- 3D printed case

---

# Assembly

### PCB Assembly

Solder all components onto the PCB:

- Diodes
- RGB LEDs
- OLED
- Rotary encoder
- XIAO RP2040

Please please please check the orientation twice, you won't regret it

### Case Assembly

- Install heat-set inserts
- Screw everything together

---

### Firmware

Hackpad 6x uses QMK firmware.

The firmware includes:

- Layer switching
- Encoder controls
- RGB effects
- OLED graphics
- RAW HID PC communication

---

### Hackpad DataLink

HackpadDataLink is a Python script that sends PC information to the hackpad.

Currently supported:

- CPU usage
- GPU usage
- Volume
- Brightness

---

# Images

<img width="738" height="568" alt="Screenshot 2026-07-26 175118" src="https://github.com/user-attachments/assets/a634e314-bee5-447d-8930-98d4383168d4" />
<img width="894" height="696" alt="Screenshot 2026-07-09 213803" src="https://github.com/user-attachments/assets/b1e69c01-3ffd-4735-bb9a-7132558721be" />
<img width="853" height="842" alt="Screenshot 2026-07-09 213747" src="https://github.com/user-attachments/assets/d00e4dbf-f881-497f-a051-0191d4511de6" />
<img width="980" height="715" alt="Screenshot 2026-07-09 213625" src="https://github.com/user-attachments/assets/aec0e36c-9b8c-4246-8060-f9a848e6e955" />
<img width="1238" height="747" alt="Screenshot 2026-07-09 213603" src="https://github.com/user-attachments/assets/5e390dba-9ea8-4358-acc0-6f55334dd600" />
<img width="1136" height="781" alt="Screenshot 2026-07-09 213421" src="https://github.com/user-attachments/assets/5f9089a6-8158-4807-a7c7-084d543f9be0" />
<img width="1118" height="914" alt="Screenshot 2026-07-09 213408" src="https://github.com/user-attachments/assets/09354def-780d-4b39-bb22-12e4ef0621b1" />
<img width="1272" height="793" alt="Screenshot 2026-07-09 213341" src="https://github.com/user-attachments/assets/873a097a-18e7-43ed-a601-1f52a3982a08" />


### AI Usage

AI was used minimally throughout this project. The only instance of AI use was on 4 occasions fixing compile errors in the firmware. This was done with VS code's built in AI. Aside from this, no other AI tools were used in the making of this project.


Hackpad 6x was built as a personal project to learn PCB design, CAD, QMK firmware, and hardware/software integration.

Huge thanks to Hack Club for making this program possible :)

(Also thanks to Google, Stack Overflow, and whoever wrote the forum post that fixed kicad at 1am.)


