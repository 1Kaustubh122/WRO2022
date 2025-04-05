#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor)
from pybricks.nxtdevices import ColorSensor as ColorSensorNXT
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from laundary import laundary
from line_follow import *
from blue_room import blue_green

ev3 = EV3Brick()
down_sensor = ColorSensorNXT(Port.S1)
up_sensor = ColorSensorNXT(Port.S2)
color3=ColorSensor(Port.S3)
color4=ColorSensor(Port.S4)
left_motor=Motor(Port.A)
right_motor=Motor(Port.D)
grabber_motor=Motor(Port.C)
medium_motor = Motor(Port.B)
drive_base=DriveBase(left_motor,right_motor,45,250)
color3=ColorSensor(Port.S3)
color4=ColorSensor(Port.S4)

def last_two_green_blocks(color3,color4,drive_base,left_motor,right_motor):
    left_motor.run_angle(1000,260)
    left_motor.brake()

    # Going towards the laundary
    drive_base.settings(1000)
    drive_base.straight(-100)
    drive_base.stop()

    #pick up the laundry block
    grabber_motor.run_until_stalled(-1000, Stop.BRAKE)
    grabber_motor.stop()

    # going to picking up the ball
    grabber_motor.run_until_stalled(1000,Stop.BRAKE)
    grabber_motor.stop()

    left_motor.run_angle(1000,-150,wait = False)
    right_motor.run_angle(1000,-150,wait = True)
    left_motor.brake()
    right_motor.brake()

    # Turning towards the ball
    right_motor.run_angle(1000,-100)
    right_motor.brake()

    #moving forward to pick up the ball
    left_motor.run_angle(100,-60,wait = False)
    right_motor.run_angle(100,-60,wait = True)
    left_motor.brake()
    right_motor.brake()

    #picking the ball
    grabber_motor.run_angle(1000, -520)
    grabber_motor.hold()

    #turning towards the ball net
    left_motor.run_angle(190,150,wait=False)
    right_motor.run_angle(190,-150)
    left_motor.brake()
    right_motor.brake()

    #moving towards the ball net
    left_motor.run_angle(200,-180,wait=False)
    right_motor.run_angle(200,-180)
    left_motor.hold()
    right_motor.hold()

    #leaving the ball
    grabber_motor.run_angle(1000,420)
    grabber_motor.stop()

    grabber_motor.run_angle(1000,-350)
    grabber_motor.hold()

    #### Going towards Green room #####
    drive_base.settings(1000,1000)
    drive_base.straight(80)
    drive_base.stop()

    left_motor.run_angle(1000,5, wait = False)
    right_motor.run_angle(1000,5)
    left_motor.hold()
    right_motor.hold()

    right_motor.run_angle(1000,270)
    right_motor.stop()

    left_motor.run_angle(1000,150, wait = False)
    right_motor.run_angle(1000,150)
    left_motor.hold()
    right_motor.hold()

    #closing the grabber
    grabber_motor.run_until_stalled(1000, Stop.BRAKE)

    line_follower1(color3,color4,drive_base,left_motor,right_motor,1200)
    drive_base.stop()

    # Turning towards green room
    drive_base.settings(1000)
    drive_base.turn(72)
    drive_base.stop()

    right_motor.run_angle(1000,30)
    right_motor.hold()

    # Going to pick up the laundary in green room
    left_motor.run_angle(1000,-120, wait = False)
    right_motor.run_angle(1000,-120)
    left_motor.hold()
    right_motor.hold()

    # picking up the laundary in green room
    grabber_motor.run_until_stalled(-1000, Stop.BRAKE)
    grabber_motor.run_until_stalled(1000, Stop.BRAKE)

    # Going to pick up the ball in green room
    left_motor.run_angle(1000,-50, wait = False)
    right_motor.run_angle(1000,-50)
    left_motor.hold()
    right_motor.hold()

    line_follower1(color3,color4,drive_base,left_motor,right_motor,1200)
    drive_base.stop()

    left_motor.run_angle(1000,-15)
    left_motor.hold()

    # moving towards the ball
    drive_base.settings(1000)
    drive_base.straight(-150)
    drive_base.stop()

    #pick the ball
    grabber_motor.run_angle(1000, -580)
    grabber_motor.hold()

    # turning towards the ball net
    left_motor.run_angle(200,-280)
    left_motor.hold()

    # move towards the ball net
    right_motor.run_angle(300,-130,wait = False)
    left_motor.run_angle(300,-130,wait=True)
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
    
    right_motor.run_angle(1000,150,wait = False)
    left_motor.run_angle(1000,150,wait=True)
    right_motor.hold()
    left_motor.hold()

    grabber_motor.run_until_stalled(-1000,Stop.BRAKE)



    drive_base.settings(1000)
    drive_base.turn(29)
    drive_base.stop()


    right_motor.run_angle(1000,520,wait = False)
    left_motor.run_angle(1000,520,wait=True)
    right_motor.hold()
    left_motor.hold()



    drive_base.settings(1000)
    drive_base.turn(-35)
    drive_base.stop()


    line_follower1(color3,color4,drive_base,left_motor,right_motor,2000)


        
    right_motor.run_angle(1000,40)
    right_motor.stop()

    right_motor.run_angle(1000,930,wait = False)
    left_motor.run_angle(1000,930,wait=True)
    right_motor.hold()
    left_motor.hold()

    drive_base.settings(1000)
    drive_base.turn(-30)
    drive_base.stop()

    
    right_motor.run_angle(1000,-100,wait = False)
    left_motor.run_angle(1000,-100,wait=True)
    right_motor.hold()
    left_motor.hold()

    laundary(drive_base,left_motor,right_motor,medium_motor,up_sensor, down_sensor)



