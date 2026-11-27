from time import sleep

from machine import Pin, UART
from machine import SoftI2C
from hid_parser import Parser

import ssd1306

uart = UART(1, baudrate=115200, tx=Pin(6), rx=Pin(5), timeout=3)
brightness = 0
i2c = SoftI2C(scl=Pin(10), sda=Pin(8))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c, addr=61)

oled.text('Welcome', 0, 0)
oled.show()
sleep(0.5)
oled.fill(0)
oled.show()

p = Parser()
debug = False

while debug:
    line = uart.readline()
    if line: print(line.decode().strip())
    sleep(0.2)

text = ''
row = 0
row_height = 9


with open("notes.txt", "a") as file:

    while True:
        try:
            line = uart.readline()
            if line:
                line = line.decode('utf-8').strip()
                p.put(line)
                s = p.read()
                s = s.replace('{SPACE}', ' ')
                if s == '{BACKSPACE}':
                    row = 0
                    s = ''
                    oled.fill(0)
                    text = ''
                if s == '{ENTER}':
                    file.write("\n" + text)
                    print("")
                    s = ''
                    text = ''
                    row += row_height

                text += s
                oled.text(text, 0, row)
                print(s, end='')
            oled.show()
            sleep(.01)
        except Exception as e:
            print(f"ERROR {e}")
            file.write("\n" + text) # emergency write text to the file
