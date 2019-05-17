from adafruit_servokit import ServoKit
from time import sleep
import sys

angle = int(sys.argv[1])
kit = ServoKit(channels=16)
kit.servo[0].angle = angle
