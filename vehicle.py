"""
Class for controlling the motors inside of our small 3-wheeled vehicle.
"""
from adafruit_servokit import ServoKit
import math
# import numpy as np
np = None

class Vehicle():
    def __init__(self, motion_servos=[0, 1, 2], trapdoor_servo = 3):

        self.motion_servos = motion_servos
        self.trapdoor_servo = trapdoor_servo
        self.kit = ServoKit(channels=16)

    def set_speed_expo(self, left, right):
        """
        Sets the speed of the car, less complex version to be used for the demo.
        """
        self.kit.continuous_servo[0].throttle = left
        self.kit.continuous_servo[1].throttle = left
        self.kit.continuous_servo[2].throttle = right
        self.kit.continuous_servo[3].throttle = right


    def set_speed(self, direction, magnitude):
        """
        Sets the speed of the car.

        We convert (vx, vy) velocities to (mv1, mv2, mv3) motor velocities by
        transforming vx and vy into (mv1, mv2, mv3) space individually and adding
        these individual solutions together, and then normalizing these vectors
        to the range [0, 1].

        For the X-direction:
        - mv1 = 0
        - mv2 = vx
        - mv3 = vx * -1

        For the Y-direction:
        - mv1 = vy
        - mv2 = vy * cos(60)
        - mv3 = vy * cos(60) * -1

        We might need to switch around the values we multiply by -1; the important thing
        is just that they have opposite signs.

        The magnitudes of the velocities will likely be different;
        - The max magnitude that the y-direction can get is 1
        - The max magnitude that the x-direciton can get is cos(30)
        We can get around the above by multiplying the y-direction by cos(30) before normalization.

        Direction is a 2-tuple containing the X and Y components of the velocity. The magnitude of this vector will be normalized to be 1.
        Magnitude is a scalar value containing the velocity; ranges from 0 to 1.
        """

        mv = np.array([0, 0, 0])
        vx = direction[0]
        vy = direction[1]

        # X-Direction
        mv[1] += vx
        mv[2] -= vx

        # Y-Direction
        mv[0] += vy * math.cos(30)
        mv[0] += vy * math.cos(60) * math.cos(30)
        mv[0] -= vy * math.cos(60) * math.cos(30)

        # Normalize and multiply by magnitude
        mv = (mv / np.max(mv)) * magnitude

        # Apply these velocities to the servo motors
        for motor_number, motor_value in enumerate(mv):
            motor_pin = self.motion_servos[motor_number]
            self.kit.continuous_servo[motor_pin].throttle = motor_value

    def rotate(self, clockwise, magnitude):
        """
        Rotates the car

        clockwise is a boolean.
        magnitude is a number between 0 and 1, representing the speed of the rotation.

        """
        if clockwise:
            magnitude = -magnitude
        for servo_num in self.motion_servos:
            self.kit.continuous_servo[servo_num].throttle = magnitude

    def stop_car(self):
        """
        Stops the car in place
        """
        for servo_num in self.motion_servos:
            # self.kit.continuous_servo[servo_num].throttle = 0
            self.kit.continuous_servo[servo_num].throttle = 0.09

    def read_trapdoor_servo_angle(self):
        """
        Reads the servo angle of the trapdoor servo
        """
        pass # TODO: Implement this

    def door_open(self):
        """
        Returns true if the mouse door is open
        """

    def door_closed(self):
        """
        Returns true if the mouse door is closed
        """

    def open_door(self):
        """
        Opens the door for the mouse to come inside.
        """

    def close_door(self):
        """
        Closes the door to trap the mouse inside.
        """
