import time
time.sleep(0.1) # Wait for USB to become ready

print("Hello, Player!")

from Lights import *
from Buzzer import *
from LightStrip import *
from Displays import LCDDisplay

red = Light(6, "Red Light")
green = Light(7, "Green Light")
buzzer = PassiveBuzzer(16)
mylightstrip = LightStrip(name="my lightstrip", pin=2, numleds=16)
mydisplay = LCDDisplay (sda = 0, scl = 1, i2cid=0)

mydisplay.showText("Start Game")
mydisplay.showText("Level1")
