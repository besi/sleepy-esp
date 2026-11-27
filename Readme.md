# Sleepynotes for ESP

Take sleepy notes without looking at a screen.

## Architecture

At the time of writing there does not seem to be a way of implementing a HID host via Bluetooth so the project is split up into two parts:

### A) Bluetooth HID

This part is written in the native Espressif IDF environment using IDF Version 6.1.
First a connection to a bluetooth keyboard is established. If the keyboard is named "Sleepynotes" the connection should be established automatically.

Once the pairing is done the HID messages received from the keyboard are read and sent via UART in the following format (spelling out 'Hello'):

```
HID-00-00-00-00-00-00-00-00
HID-02-00-00-00-00-00-00-00
HID-02-00-0b-00-00-00-00-00
HID-02-00-00-00-00-00-00-00
HID-00-00-00-00-00-00-00-00
HID-00-00-08-00-00-00-00-00
HID-00-00-00-00-00-00-00-00
HID-00-00-0f-00-00-00-00-00
HID-00-00-00-00-00-00-00-00
HID-00-00-0f-00-00-00-00-00
HID-00-00-00-00-00-00-00-00
HID-00-00-12-00-00-00-00-00
```

Since the ease of development is relatively low due to long compile times and old school C programming. This part is kept as simple as possible, moving more complexity to the second part of the application.

To flash the program onto an ESP32 board the following steps are required:

```bash
cd idf/
get_idf # Activate the IDF environment
idf.py build flash monitor
```

The ESP-IDF framework needs to be installed on the system (such as ~/esp-idf).

### B) Notetaking

This part is written in Micropython and the HID messages are decoded and interpreted. Any on-board peripherals such as RGB-LEDs etc. are managed by this part of the project.


## Pinout of the Micropython ESP

| Function            | GPIO |
|:--------------------|-----:|
| Neopixel            | 14   |
| Wireless Button A   |  4   |
| Wireless Button B   |  0   |
| Wireless Button C   |  2   |
| Wireless Button D   | 16   |
| Wireless Button Any | 21   |
| I2C SDA             |  9   |
| I2C SCL             | 10   |
| SPI CS              | 12   |
| SPI MOSI            | 32   |
| SPI MISO            | 27   |
| SPI CLK             | 25   |
| LDR                 | 36   |
| Button 1            | 39   |
| Button 2            | 35   |
| Button 3            | 33   |
| Button 4            | 34   |
