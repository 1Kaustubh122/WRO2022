#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor)
from pybricks.nxtdevices import ColorSensor as ColorSensorNXT
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
# from line_follow import *
from line_follow import line_follower3, line_follower1


ev3 = EV3Brick()
down_sensor = ColorSensorNXT(Port.S1)
up_sensor = ColorSensorNXT(Port.S2)
color3=ColorSensor(Port.S3)
color4=ColorSensor(Port.S4)
left_motor=Motor(Port.A)
right_motor=Motor(Port.D)
grabber_motor=Motor(Port.C)
drive_base=DriveBase(left_motor,right_motor,45,250)
color3=ColorSensor(Port.S3)
color4=ColorSensor(Port.S4)

kd=30
kp=0.35
derivative=0
proportional=0
error=0
last_error=0
steering=0
while True:
    error=color4.reflection()-color3.reflection()
    derivative=(error-last_error)*kd
    last_error=error
    proportional=error*kp
    steering=proportional
    drive_base.drive(1000,steering)


# kd=-50
# kp=-1
# ki=-0.001
# derivative=0
# proportional=0
# error=0
# last_error=0
# steering=0
# total_error=0
# while True:
#     error=color4.reflection()-color3.reflection()
#     total_error=total_error+error
#     derivative=(error-last_error)*kd
#     integral=total_error*ki
#     last_error=error
#     proportional=error*kp
#     steering=proportional+derivative
#     drive_base.drive(-50,steering)