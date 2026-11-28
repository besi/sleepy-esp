from time import sleep

from machine import Pin, UART
from machine import SoftI2C
from hid_parser import Parser
from neopixel import NeoPixel

import ssd1306

uart = UART(1, baudrate=115200, tx=Pin(6), rx=Pin(5), timeout=3)
brightness = 0
i2c = SoftI2C(scl=Pin(10), sda=Pin(8))
led = NeoPixel(Pin(7),1) # GRB

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c, addr=61)

oled.text('Welcome', 0, 0)
oled.show()
sleep(0.5)
oled.fill(0)
oled.show()

brightness = 0
max_brightness = 8

p = Parser()
debug = False

while debug:
    line = uart.readline()
    if line: print(line.decode().strip())
    sleep(0.2)

text = ''
row = 0
row_height = 9

def log(file,text):
    with open(file, 'a') as pf:
        pf.write(text)

def setBrightness(delta):
    global brightness
    brightness = min(brightness + delta,8)
    brightness = max(brightness, 0)
    v = (brightness * 255) // max_brightness
    led.fill((int(v*.6), v, int(v*.15)))
    led.write()

setBrightness(0)

while True:
    try:
        line = uart.readline()
        if line:
            line = line.decode('utf-8').strip()
            p.put(line)
            s = p.read()
            s = s.replace('{SPACE}', ' ')
            if s=='{ESC}':
                log('notes.txt', "\n" + text)
                text = ''
                s = ''
                row = 0
                oled.fill(0)
                oled.show()
            elif s == '{BACKSPACE}':
                s = ''
                text = text[:-1]
            elif s == '{BRIGHTNESS_UP}':
                setBrightness(+1)
                s = ''
            elif s == '{BRIGHTNESS_DOWN}':
                setBrightness(-1)
                s = ''
            elif s == '{ENTER}':
                log('notes.txt', "\n" + text)
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
        log("error.log",f"ERROR {e} --- text: {text}")
        log('notes.txt', "\n" + text)

