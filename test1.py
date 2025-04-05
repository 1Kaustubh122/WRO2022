#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor)
from pybricks.nxtdevices import ColorSensor as ColorSensorNXT
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from line_follow import *
from yellow_room import yellow_white, yellow_green
from blue_room import blue_white, blue_green
from move_to_other_side import abc
from red_white import last_two_marking_is_white
from laundary import laundary

ev3 = EV3Brick()
down_sensor = ColorSensorNXT(Port.S1)
up_sensor = ColorSensorNXT(Port.S2)
color3=ColorSensor(Port.S3)
color4=ColorSensor(Port.S4)
left_motor=Motor(Port.A)
right_motor=Motor(Port.D)
medium_motor = Motor(Port.B)
grabber_motor=Motor(Port.C)
drive_base=DriveBase(left_motor,right_motor,45,250)
color3=ColorSensor(Port.S3)
color4=ColorSensor(Port.S4)

line_follower_fast(color3,color4,drive_base,left_motor,right_motor,1000)

# # drive_base.settings(1000)
# # drive_base.turn(38)
# # drive_base.stop()

# left_motor.run_angle(1000,-350,wait=False)
# right_motor.run_angle(1000,-350)
# left_motor.hold()
# right_motor.hold()

# right_motor.run_angle(1000,-80)
# right_motor.hold()

# line_follower1(color3,color4,drive_base,left_motor,right_motor,1200)

# left_motor.run_angle(1000,-200,wait=False)
# right_motor.run_angle(1000,-200)
# left_motor.hold()
# right_motor.hold()

# right_motor.run_angle(1000,-100)
# right_motor.hold()

# left_motor.run_angle(1000,-400,wait=False)
# right_motor.run_angle(1000,-400)
# left_motor.hold()
# right_motor.hold()

# grabber_motor.run_until_stalled(-1000,Stop.BRAKE)

# left_motor.run_angle(1000,-100)
# left_motor.stop()

# left_motor.run_angle(1000,-100,wait=False)
# right_motor.run_angle(1000,-100)
# left_motor.hold()
# right_motor.hold()





    
