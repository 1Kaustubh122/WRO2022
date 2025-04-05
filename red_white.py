#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor)
from pybricks.nxtdevices import ColorSensor as ColorSensorNXT
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from line_follow import *
from threading import Thread
from laundary import laundary


ev3 = EV3Brick()
down_sensor = ColorSensorNXT(Port.S1)
up_sensor = ColorSensorNXT(Port.S2)
color3=ColorSensor(Port.S3)
color4=ColorSensor(Port.S4)
left_motor=Motor(Port.A)
medium_motor = Motor(Port.B)
right_motor=Motor(Port.D)
grabber_motor=Motor(Port.C)
drive_base=DriveBase(left_motor,right_motor,45,250)
color3=ColorSensor(Port.S3)
color4=ColorSensor(Port.S4)

def last_two_marking_is_white(color3,color4,drive_base,left_motor,right_motor,down_sensor):
        
    grabber_motor.run_until_stalled(1000, Stop.HOLD)
    grabber_motor.hold()
    # Moving backward 
    left_motor.run_angle(1000, -150, wait = False)
    right_motor.run_angle(1000, -150, wait = True)
    left_motor.brake()
    right_motor.brake()

    # Turning towards red room table
    right_motor.run_angle(1000,290)
    right_motor.brake()

    #  Moving towards red room table
    left_motor.run_angle(1000, 320, wait = False)
    right_motor.run_angle(1000, 320, wait = True)
    left_motor.brake()
    right_motor.brake()

    # Keeping the water block
    grabber_motor.run_angle(1000,-330)
    grabber_motor.stop()

    # Going to pick up the laundary in green room
    grabber_motor.run_angle(1000,250, wait = False)
    left_motor.run_angle(1000,-300, wait = False)
    right_motor.run_angle(1000, -300, wait = True)
    left_motor.brake()
    right_motor.brake()
    grabber_motor.stop()

    left_motor.run_angle(1000,-50)
    left_motor.stop()

    left_motor.run_angle(1000,-300, wait = False)
    right_motor.run_angle(1000, -300, wait = True)
    left_motor.hold()
    right_motor.hold()



    # Picking up the laundary in green room
    # check if laundary is picked up
    grabber_motor.run_until_stalled(-1000, Stop.BRAKE)
    grabber_motor.stop()

    # lifting up the water block to keep water block in green room 
    grabber_motor.run_until_stalled(1000, Stop.HOLD)
    grabber_motor.hold()

    left_motor.run_angle(1000,-30, wait = False)
    right_motor.run_angle(1000, -30, wait = True)
    left_motor.brake()
    right_motor.brake()

    # Turning the robot to table
    left_motor.run_angle(1000,630)
    left_motor.brake()

    left_motor.run_angle(1000,70, wait = False)
    right_motor.run_angle(1000,70, wait = True)
    left_motor.brake()
    right_motor.brake()

    # keeping the water block in green room
    grabber_motor.run_angle(1000,-330)
    grabber_motor.stop()




    # Turning towards red room laundary

    # moving forward to pick up laundary
    grabber_motor.run_angle(1000,250, wait = False)
    left_motor.run_angle(1000,-600, wait = False)
    right_motor.run_angle(1000, -600, wait = True)
    left_motor.brake()
    right_motor.brake()
    grabber_motor.stop()

    # Picking up the laundary block in red room
    grabber_motor.run_until_stalled(-1000, Stop.BRAKE)
    grabber_motor.stop()

    left_motor.run_angle(1000,70)
    left_motor.stop()

    left_motor.run_angle(1000,200, wait = False)
    right_motor.run_angle(1000, 200, wait = True)
    left_motor.hold()
    right_motor.hold()

    drive_base.settings(1000)
    drive_base.turn(35)
    drive_base.stop()



    line_follower1(color3,color4,drive_base,left_motor,right_motor,1400)
    drive_base.stop()

    left_motor.run_angle(1000,200, wait = False)
    right_motor.run_angle(1000, 200, wait = True)
    left_motor.hold()
    right_motor.hold()


    right_motor.run_angle(1000,90)
    right_motor.stop()

    left_motor.run_angle(1000,880, wait = False)
    right_motor.run_angle(1000, 880, wait = True)
    left_motor.hold()
    right_motor.hold()


    drive_base.settings(1000)
    drive_base.turn(-35)
    drive_base.stop()

    
    left_motor.run_angle(1000,-100, wait = False)
    right_motor.run_angle(1000, -100, wait = True)
    left_motor.hold()
    right_motor.hold()

    laundary(drive_base,left_motor,right_motor,medium_motor,up_sensor, down_sensor)


