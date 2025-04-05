#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor)
from pybricks.nxtdevices import ColorSensor as ColorSensorNXT
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from line_follow import *


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

def moving_from_center(color3,color4,drive_base,left_motor,right_motor,down_sensor):
#move till center
    drive_base.settings(1000)
    drive_base.straight(120)
    drive_base.stop(Stop.BRAKE)

    stopwatch=StopWatch()

#move from center to other side
    drive_base.settings(1000)
    while stopwatch.time()<=1600:
        if stopwatch.time()<=550:
            drive_base.drive(1000,12) 
        else:
            drive_base.drive(1000,-17)
    drive_base.stop()

    left_motor.run_angle(1000,200)
    left_motor.hold()
    
    #follow the line till marking block
    line_follower3(color3,color4,drive_base,left_motor,right_motor)
    drive_base.stop()

def yellow_green(color3,color4,drive_base,left_motor,right_motor,grabber_motor):
    
    # #turning the robot towards the laundry block
    left_motor.run_angle(1000,-30)
    left_motor.hold()
    right_motor.run_angle(1000,-540)
    right_motor.hold()


    # moving back to open the grabber
    line_follower1(color3,color4,drive_base,left_motor,right_motor,1800)
    drive_base.stop()

    # opening the grabber to pick the laundry block
    grabber_motor.run_until_stalled(1000,Stop.BRAKE)

    #moving forward to pick the laundry block
    left_motor.run_angle(1000,-30,wait=True)
    left_motor.hold()
    right_motor.run_angle(1000,-120,wait = False)
    left_motor.run_angle(1000,-120,wait=True)
    right_motor.hold()
    left_motor.hold()

    # opening the grabber to pick the laundry block
    grabber_motor.run_until_stalled(-1000,Stop.BRAKE)
    grabber_motor.run_until_stalled(1000,Stop.BRAKE)

    #move towards the ball
    right_motor.run_angle(1000,-150)
    left_motor.run_angle(1000,-100)
    right_motor.hold()
    left_motor.hold()

    line_follower1(color3,color4,drive_base,left_motor,right_motor,1400)
    drive_base.stop()

    left_motor.run_angle(1000,-15)
    left_motor.hold()


    # moving towards the ball
    drive_base.settings(1000)
    drive_base.straight(-125)
    drive_base.stop()

    #pick the ball
    grabber_motor.run_angle(1000, -580)
    grabber_motor.hold()

    # turning towards the ball net


    left_motor.run_angle(1000,-280)
    left_motor.hold()

    # move towards the ball net
    right_motor.run_angle(300,-135,wait = False)
    left_motor.run_angle(300,-135,wait=True)
    right_motor.hold()
    left_motor.hold()


    #leave the ball
    grabber_motor.run_angle(1000,400)
    grabber_motor.stop()

    grabber_motor.run_angle(1000,-300)
    grabber_motor.hold()

    right_motor.run_angle(1000,200,wait = False)
    left_motor.run_angle(1000,200,wait=True)
    right_motor.hold()
    left_motor.hold()

    #close the grabber
    grabber_motor.run_until_stalled(-1000,Stop.BRAKE)
    grabber_motor.stop()

    #turning for moving towards the black line
    left_motor.run_angle(1000,250,wait=True)
    left_motor.hold()

    #moving towards the black line
    right_motor.run_angle(1000,410,wait = False)
    left_motor.run_angle(1000,410,wait=True)
    right_motor.hold()
    left_motor.hold()

    grabber_motor.run_angle(1000,250)
    grabber_motor.stop()

    #turning the right motor to make the robot straight
    drive_base.settings(1000)
    drive_base.turn(-32)
    drive_base.stop()


    line_follower3(color3,color4,drive_base,left_motor,right_motor)
    drive_base.stop()
    
    
def yellow_white(color3,color4,drive_base,left_motor,right_motor,grabber_motor):

    # #turning the robot towards the laundry block
    left_motor.run_angle(1000,-30)
    left_motor.hold()
    right_motor.run_angle(1000,-540)
    right_motor.hold()
    
    # moving back to open the grabber
    line_follower1(color3,color4,drive_base,left_motor,right_motor,1800)
    drive_base.stop()

    # opening the grabber to pick the laundry block
    grabber_motor.run_until_stalled(1000,Stop.BRAKE)

    #moving forward to pick the laundry block
    left_motor.run_angle(1000,-30,wait=True)
    left_motor.hold()
    right_motor.run_angle(1000,-150,wait = False)
    left_motor.run_angle(1000,-150,wait=True)
    right_motor.hold()
    left_motor.hold()

    # opening the grabber to pick the laundry block
    grabber_motor.run_until_stalled(-1000,Stop.BRAKE)
    grabber_motor.run_until_stalled(1000,Stop.BRAKE)

    # turning towards the table

    right_motor.run_angle(1000, -410)
    right_motor.hold()

    drive_base.settings(1000)
    drive_base.straight(120)
    drive_base.stop()

    grabber_motor.run_until_stalled(1000, Stop.HOLD)

    drive_base.settings(1000)
    drive_base.straight(80)
    drive_base.stop()

    # kept the water block from right side of the grabber
    grabber_motor.run_angle(1000,-250) 
    grabber_motor.stop()

    # moving back after keeping the water block from right side of the grabber
    left_motor.run_angle(1000,-480,wait=False)
    right_motor.run_angle(1000,-480)
    right_motor.brake()
    left_motor.brake()

    # Turning towards black line
    right_motor.run_angle(1000,800)
    right_motor.stop()

    line_follower3(color3,color4,drive_base,left_motor,right_motor)
    drive_base.stop()