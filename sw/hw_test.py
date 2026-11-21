### SD CARD

from machine import SoftSPI, Pin, SDCard
import os

sd = SDCard(slot=2, sck=25, miso=27, mosi=32, cs=12)

os.mount(sd, "/sd")  # mount
print(os.listdir('/sd'))
os.umount('/sd')
sd.deinit()
