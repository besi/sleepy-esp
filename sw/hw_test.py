### Wireless button rx480
from machine import Pin
from time import sleep

p1 = Pin(16, Pin.IN)
p2 = Pin(2, Pin.IN)
p3 = Pin(0, Pin.IN)
p4 = Pin(4, Pin.IN)
p5 = Pin(21, Pin.IN)

while True:
    print(f"A={p1()}, B={p2()}, C={p3()}, D={p4()}, ALL={p5()}")
    sleep(.2)

### SD CARD

from machine import SoftSPI, Pin, SDCard
import os

sd = SDCard(slot=2, sck=25, miso=27, mosi=32, cs=12)

os.mount(sd, "/sd")  # mount
print(os.listdir('/sd'))
os.umount('/sd')
sd.deinit()
