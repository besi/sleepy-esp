# Still to test
# | Function            | GPIO |
# |---------------------|------|
# | SDA                 | 9    |
# | SCL                 | 10   |
# | Button 1            | 39   |
# | Button 2            | 35   |
# | Button 3            | 33   |
# | Button 4            | 34   |


### Neopixel
from machine import Pin
from neopixel import NeoPixel
from time import sleep, ticks_ms, ticks_us
np = NeoPixel(Pin(14, Pin.OUT),1)

while True:
    b = 11
    np.fill((ticks_us()%b,ticks_ms()%b,(ticks_ms()+ticks_us())%b))
    np.write()
    sleep(.05)


### LDR

from machine import ADC, Pin
from time import sleep
adc = ADC(Pin(36))

while True:
    print(adc.read())
    sleep(.2)


### Wireless button rx480
from machine import Pin
from time import sleep

p1 = Pin(4, Pin.IN)
p2 = Pin(0, Pin.IN)
p3 = Pin(2, Pin.IN)
p4 = Pin(16, Pin.IN)
p5 = Pin(21, Pin.IN)

while True:
    print(f"A={p1()}, B={p2()}, C={p3()}, D={p4()}, ANY={p5()}")
    sleep(.2)

### SD CARD

from machine import SoftSPI, Pin, SDCard
import os

sd = SDCard(slot=2, sck=25, miso=27, mosi=32, cs=12)

os.mount(sd, "/sd")  # mount
print(os.listdir('/sd'))
os.umount('/sd')
sd.deinit()
