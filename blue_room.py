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

def blue_green(color3,color4,drive_base,left_motor,right_motor,grabber_motor):
    
    #turning towards the laundry block
    grabber_motor.run_angle(1000,-400, wait = False)
    left_motor.run_angle(1000,320)
    grabber_motor.stop()
    left_motor.hold()

    grabber_motor.run_until_stalled(1000, Stop.HOLD)
    grabber_motor.brake()

    left_motor.run_angle(1000,-100,wait=False)
    right_motor.run_angle(1000,-100,wait = True)
    left_motor.stop()
    right_motor.stop()

    # pick up the laundry block
    right_motor.run_angle(1000,-130, wait = False)
    grabber_motor.run_until_stalled(-1000, Stop.BRAKE)
    right_motor.brake()
    grabber_motor.run_until_stalled(-1000, Stop.BRAKE)
    
    left_motor.run_angle(1000,30,wait = False)
    right_motor.run_angle(1000,30)
    right_motor.stop()
    left_motor.stop()
    
    # going to picking up the ball
    grabber_motor.run_until_stalled(1000,Stop.BRAKE)
    grabber_motor.stop()
    
    drive_base.settings(1000)
    drive_base.straight(-78)
    drive_base.stop()
    
    grabber_motor.run_angle(300,-300)
    grabber_motor.hold()
    
    #turning towards the ball net
    grabber_motor.run_angle(1000,-220,wait = False)
    left_motor.run_angle(190,170,wait=False)
    right_motor.run_angle(190,-170)
    grabber_motor.hold()
    left_motor.hold()
    right_motor.hold()

    #moving towards the ball net
    left_motor.run_angle(1000,-150,wait=False)
    right_motor.run_angle(1000,-150)
    left_motor.hold()
    right_motor.hold()

    #leaving the ball
    grabber_motor.run_angle(1000,420)
    grabber_motor.stop()

    #moving back after keeping the ball
    grabber_motor.run_angle(1000,-500)
    grabber_motor.hold()
    
    left_motor.run_angle(1000,120,wait=False)
    right_motor.run_angle(1000,120)
    left_motor.hold()
    right_motor.hold()
   
    # drive_base.settings(1000)
    # drive_base.turn(30)
    # drive_base.stop()

    # left_motor.run_angle(1000,200,wait=False)
    # right_motor.run_angle(1000,200)
    # left_motor.hold()
    # right_motor.hold()
    
    # right_motor.run_angle(1000,-80)
    # right_motor.hold()
    
    # line_follower1(color3,color4,drive_base,left_motor,right_motor,1000)
    
    # right_motor.run_angle(1000,-100)
    # right_motor.hold()
    
    
    

    # right_motor.run_angle(1000,-300,wait = False)
    # left_motor.run_angle(1000,-300,wait = False)
    # grabber_motor.run_until_stalled(1000, Stop.BRAKE)
    # right_motor.hold()
    # left_motor.hold()
    
    # drive_base.settings(1000)
    # drive_base.turn(-20)
    # drive_base.stop()

    # left_motor.run_angle(1000,100,wait=False)
    # right_motor.run_angle(1000,100,wait=True)
    # left_motor.stop()
    # right_motor.stop()

    #closing the grabber
    # grabber_motor.run_angle(1000,-110)
    # grabber_motor.hold()
    
    # line_follower3(color3,color4,drive_base,left_motor,right_motor)
    # drive_base.stop()
    
def blue_white(color3,color4,drive_base,left_motor,right_motor,grabber_motor):
    left_motor.run_angle(1000,30)
    # right_motor.run_angle(1000,-35)
    # right_motor.hold()
    left_motor.hold()

    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    left_motor.run_angle(100,1000,wait=False)
    right_motor.run_angle(100,1000,wait=False)
    grabber_motor.run_until_stalled(1000, Stop.HOLD)
    grabber_motor.hold()
    left_motor.hold()
    right_motor.hold()
    
    left_motor.run_angle(1000,260-left_motor.angle(),wait=False)
    right_motor.run_angle(1000,260-right_motor.angle())
    left_motor.hold()
    right_motor.hold()

    grabber_motor.run_angle(1000,-250) # kept the water block
    grabber_motor.stop()
    
    grabber_motor.run_angle(1000,-400, wait = False)
    right_motor.run_angle(1000,-250,wait=False)
    left_motor.run_angle(1000,-250,wait= True)
    left_motor.hold()
    right_motor.hold()
    grabber_motor.hold()
    
    left_motor.run_angle(1000,295,wait= True)
    left_motor.hold()
    right_motor.hold()

    #open the grabber
    grabber_motor.run_until_stalled(1000, Stop.HOLD)
    grabber_motor.stop()

    #move to pick the laundry block
    left_motor.run_angle(1000,-110,wait= False)
    right_motor.run_angle(1000,-110,wait= True)
    left_motor.hold()
    right_motor.hold()

    #pick up the laundry block
    grabber_motor.reset_angle(0)
    grabber_motor.run_until_stalled(-1000,Stop.HOLD)
    grabber_motor.stop() 
    
    #open the grabber to drop the laundry block
    grabber_motor.run_angle(1000,300)
    grabber_motor.stop()
    
    left_motor.run_angle(1000,-170,wait = True)
    left_motor.hold()

    left_motor.run_angle(1000,-200,wait = False)
    right_motor.run_angle(1000,-200,wait = True)
    left_motor.hold()
    right_motor.hold()

    drive_base.turn(33)
    drive_base.stop(Stop.BRAKE)

    line_follower3(color3,color4,drive_base,left_motor,right_motor)
    drive_base.stop()