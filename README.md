# Hackpad 6x

Hackpad 6x is a small but very over-engineered macropad that I designed because apparently a normal keyboard was not enough :)

The idea was to make a compact control pad that could do a bit of everything: media controls, shortcuts, gaming controls, numpad functions, and displaying useless (but cool) information from my PC.

Basically, I wanted an "infinite keys" macropad where a few buttons could become a lot of buttons through layers.

(Yes, this did start as "I'll just make a simple macropad" and then somehow became OLEDs, RGB, and a PC monitoring system. I have no idea how this happened.)

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

# Firmware

Hackpad 6x uses QMK firmware.

The firmware includes:

- Layer switching
- Encoder controls
- RGB effects
- OLED graphics
- RAW HID PC communication

(Translation: lots of C code that compiles, but is so far untested.)

---

# Hackpad DataLink

HackpadDataLink is a Python script that sends PC information to the hackpad.

Currently supported:

- CPU usage
- GPU usage
- Volume
- Brightness

(Yes, I made a tiny keyboard display show things my PC already knows)

---

# Troubleshooting

If something doesn't work:

1. Check the wiring
2. Check the firmware
3. Check your code
4. Question your life choices
5. Realise you forgot to plug in USB

(The last step is optional but happens more often than I would like to admit.)

---

# AI Usage

AI was used minimally throughout this project. The only instance of AI use was on 4 occasions fixing compile errors in the firmware. This was done with VS code's built in AI. Aside from this, no other AI tools were used in the making of this project.


Hackpad 6x was built as a personal project to learn PCB design, CAD, QMK firmware, and hardware/software integration.

Huge thanks to Hack Club for making this program possible :)

(Also thanks to Google, Stack Overflow, and whoever wrote the forum post that fixed kicad at 1am.)
