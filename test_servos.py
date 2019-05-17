from adafruit_servokit import ServoKit
from time import sleep
import sys

# angle = int(sys.argv[1])
# kit = ServoKit(channels=16)
# kit.servo[0].angle = angle

kit = ServoKit(channels=16)
throttle_1 = float(sys.argv[1])
throttle_2 = float(sys.argv[2])
kit.continuous_servo[0].throttle = throttle_1
kit.continuous_servo[1].throttle = throttle_2
