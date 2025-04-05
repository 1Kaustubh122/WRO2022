#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor)
from pybricks.nxtdevices import ColorSensor as ColorSensorNXT
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from line_follow import *
from laundary import laundary
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

def red_green(color3,color4,drive_base,left_motor,right_motor,grabber_motor,grabber_used):
    
    left_motor.run_angle(1000,-20)
    
    #turning towards the laundry block
    grabber_motor.run_angle(1000,-400, wait = False)
    left_motor.run_angle(1000,320)
    grabber_motor.stop()
    left_motor.hold()

    grabber_motor.run_until_stalled(1000, Stop.HOLD)
    grabber_motor.brake()

    left_motor.run_angle(1000,-80,wait=False)
    right_motor.run_angle(1000,-80,wait = True)
    left_motor.hold()
    right_motor.hold()

    #pick up the laundry block
    grabber_motor.run_until_stalled(-1000, Stop.BRAKE)
    grabber_motor.stop()

    # going to picking up the ball
    grabber_motor.run_until_stalled(1000,Stop.BRAKE)
    grabber_motor.stop()

    left_motor.run_angle(1000,-135,wait = False)
    right_motor.run_angle(1000,-135,wait = True)
    left_motor.hold()
    right_motor.hold()

    right_motor.run_angle(1000,-180)
    right_motor.hold()

    #moving forward to pick up the ball
    left_motor.run_angle(100,-50,wait = False)
    right_motor.run_angle(100,-50,wait = True)
    left_motor.hold()
    right_motor.hold()

    #picking the ball
    grabber_motor.run_angle(1000, -520)
    grabber_motor.hold()

    #turning towards the ball net
    left_motor.run_angle(190,152,wait=False)
    right_motor.run_angle(190,-152)
    left_motor.hold()
    right_motor.hold()

    #moving towards the ball net
    left_motor.run_angle(200,-180,wait=False)
    right_motor.run_angle(200,-180)
    left_motor.hold()
    right_motor.hold()

    #leaving the ball
    grabber_motor.run_angle(1000,420)
    grabber_motor.stop()

    grabber_motor.run_angle(1000,-420)
    grabber_motor.hold()




    #moving back after keeping the ball
    left_motor.run_angle(1000,250,wait=False)
    right_motor.run_angle(1000,250)
    left_motor.hold()
    right_motor.hold()

    #turn towards the black line
    drive_base.settings(1000)
    drive_base.turn(-20)
    drive_base.stop()

    #move towards the black line
    left_motor.run_angle(1000,150,wait=False)
    right_motor.run_angle(1000,150,wait=True)
    left_motor.stop()
    right_motor.stop()

    #follow the line till intersection
    line_follower3(color3,color4,drive_base,left_motor,right_motor)

    #down the grabber to hit the marking block aside
    grabber_motor.run_angle(1000,100)
    grabber_motor.stop()

    #turn the robot to pick the laundry block and hit the marking block
    drive_base.settings(1000)
    drive_base.turn(70)
    drive_base.stop()

    #open the grabber to pick the laundry block
    grabber_motor.run_until_stalled(1000,Stop.BRAKE)

    #move forward to pick the marking block
    left_motor.run_angle(1000,-200,wait=False)
    right_motor.run_angle(1000,-200,wait=True)
    left_motor.stop()
    right_motor.stop()

    #pick the laundry block
    grabber_motor.run_until_stalled(-1000,Stop.BRAKE)




    if grabber_used=="left":
        right_motor.run_angle(1000,-400,wait=False)
        grabber_motor.run_until_stalled(1000,Stop.BRAKE)
        right_motor.stop()  
        left_motor.run_angle(1000,500,wait=False)
        right_motor.run_angle(1000,500,wait=True)
        left_motor.stop()
        right_motor.stop()

        grabber_motor.run_angle(1000,-250) 
        grabber_motor.stop()

        left_motor.run_angle(1000,-480,wait=False)
        right_motor.run_angle(1000,-480)
        right_motor.brake()
        left_motor.brake()

    if grabber_used=="right":
        grabber_motor.run_until_stalled(1000,Stop.BRAKE)
        right_motor.run_angle(1000,-500,wait=True)
        right_motor.stop()  
        left_motor.run_angle(1000,500,wait=False)
        right_motor.run_angle(1000,500,wait=True)
        left_motor.stop()
        right_motor.stop()

        grabber_motor.run_angle(1000,-250) 
        grabber_motor.stop()

    left_motor.run_angle(1000,-100,wait=False)
    right_motor.run_angle(1000,-100)
    right_motor.brake()
    left_motor.brake()

    right_motor.run_angle(1000,-120)
    right_motor.stop()

    left_motor.run_angle(1000,-540,wait=False)
    right_motor.run_angle(1000,-540)
    right_motor.brake()
    left_motor.brake()
        
    drive_base.settings(1000)
    drive_base.turn(48)
    drive_base.stop()

    line_follower1(color3,color4,drive_base,left_motor,right_motor,1400)
    drive_base.stop()

    right_motor.run_angle(1000,70)
    right_motor.stop()


    left_motor.run_angle(1000,750,wait=False)
    right_motor.run_angle(1000,750)
    right_motor.brake()
    left_motor.brake()

    drive_base.turn(-30)
    drive_base.stop()

    laundary(drive_base,left_motor,right_motor,medium_motor,up_sensor, down_sensor)


def red_white(color3,color4,drive_base,left_motor,right_motor,grabber_motor):
    left_motor.run_angle(1000,-20)
    right_motor.run_angle(1000,-35)
    right_motor.brake()
    left_motor.brake()

    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    left_motor.run_angle(100,1000,wait=False)
    right_motor.run_angle(100,1000,wait=False)
    grabber_motor.run_until_stalled(1000, Stop.HOLD)
    grabber_motor.hold()
    left_motor.brake()
    right_motor.brake()
    
    left_motor.run_angle(500,290-left_motor.angle(),wait=False)
    right_motor.run_angle(500,290-right_motor.angle())
    left_motor.brake()
    right_motor.brake()

    grabber_motor.run_angle(1000,-250) # kept the water block
    grabber_motor.stop()
    
    grabber_motor.run_angle(1000,-400, wait = False)
    right_motor.run_angle(1000,-250,wait=False)
    left_motor.run_angle(1000,-250,wait= True)
    left_motor.brake()
    right_motor.brake()
    grabber_motor.hold()
    
    left_motor.run_angle(1000,310,wait= True)
    left_motor.brake()
    right_motor.brake()

    #open the grabber
    grabber_motor.run_until_stalled(1000, Stop.HOLD)
    grabber_motor.stop()

    #move to pick the laundry block
    left_motor.run_angle(1000,-90,wait= False)
    right_motor.run_angle(1000,-90,wait= True)
    left_motor.brake()
    right_motor.brake()

    #pick up the laundry block
    grabber_motor.reset_angle(0)
    grabber_motor.run_until_stalled(-1000,Stop.HOLD)
    grabber_motor.stop() 
    
    #open the grabber to drop the laundry block
    grabber_motor.run_angle(1000,300)
    grabber_motor.stop()
    
    #turn towards the black line
    left_motor.run_angle(1000,-170,wait = True)
    left_motor.hold()

    #move towards the black line
    left_motor.run_angle(1000,-180,wait = False)
    right_motor.run_angle(1000,-180,wait = True)
    left_motor.hold()
    right_motor.hold()

    #turn to follow the black line
    drive_base.turn(33)
    drive_base.stop(Stop.BRAKE)


    #follow the line till intersection
    line_follower3(color3,color4,drive_base,left_motor,right_motor)

    #down the grabber to hit the marking block aside
    grabber_motor.run_angle(1000,100)
    grabber_motor.stop()

    #turn the robot to pick the laundry block and hit the marking block
    drive_base.settings(1000)
    drive_base.turn(70)
    drive_base.stop()

    #open the grabber to pick the laundry block
    grabber_motor.run_until_stalled(1000,Stop.BRAKE)

    #move forward to pick the laundry block
    left_motor.run_angle(1000,-200,wait=False)
    right_motor.run_angle(1000,-200,wait=True)
    left_motor.stop()
    right_motor.stop()

    #pick the laundry block
    grabber_motor.run_until_stalled(-1000,Stop.BRAKE)

    left_motor.run_angle(1000,-100,wait=False)
    right_motor.run_angle(1000,-100,wait=True)
    left_motor.stop()
    right_motor.stop()

    right_motor.run_angle(1000,40)
    right_motor.stop()

    line_follower3(color3,color4,drive_base,left_motor,right_motor)

    grabber_motor.run_until_stalled(1000,Stop.BRAKE)

    left_motor.run_angle(1000,-15)
    left_motor.hold()

    # moving towards the ball
    drive_base.settings(1000)
    drive_base.straight(-140)
    drive_base.stop()

    #pick the ball
    grabber_motor.run_angle(1000, -580)
    grabber_motor.hold()

    # turning towards the ball net
    left_motor.run_angle(200,-290)
    left_motor.hold()

    # move towards the ball net
    right_motor.run_angle(300,-135,wait = False)
    left_motor.run_angle(300,-135,wait=True)
    right_motor.hold()
    left_motor.hold()

    #leave the ball
    grabber_motor.run_angle(1000,400)
    grabber_motor.stop()

    grabber_motor.run_angle(1000,-350)
    grabber_motor.hold()


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


        
    right_motor.run_angle(1000,50)
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





    
def red_white_Y(color3,color4,drive_base,left_motor,right_motor,grabber_motor):
    left_motor.run_angle(1000,80,wait = False)
    right_motor.run_angle(1000,80,wait = True)
    left_motor.hold()
    right_motor.hold()

    right_motor.run_angle(1000,150,wait = True)
    right_motor.hold()

    grabber_motor.run_until_stalled(1000,Stop.HOLD)

    left_motor.run_angle(1000,90,wait = False)
    right_motor.run_angle(1000,90,wait = True)
    left_motor.hold()
    right_motor.hold()

    grabber_motor.run_angle(-1000,310)
    grabber_motor.stop()
    
    
    # Moving back after keeping water block
    grabber_motor.run_angle(1000,300,wait = False)
    right_motor.run_angle(1000,-300,wait=False)
    left_motor.run_angle(1000,-300,wait= True)
    left_motor.hold()
    right_motor.hold()
    grabber_motor.stop()
    
    left_motor.run_angle(1000,-30)
    left_motor.stop()
    
    right_motor.run_angle(1000,-230,wait=False)
    left_motor.run_angle(900,-200,wait= True)
    left_motor.hold()
    right_motor.hold()    
    
    # picking up the laundary block in green room
    grabber_motor.run_angle(-1000, 370)
    grabber_motor.hold()
    
    right_motor.run_angle(1000,-300)
    right_motor.hold()
    
    grabber_motor.run_until_stalled(-1000,Stop.BRAKE)
    grabber_motor.run_until_stalled(1000,Stop.BRAKE)

    right_motor.run_angle(1000,-50,wait=False)
    left_motor.run_angle(1000,-50,wait= True)
    left_motor.hold()
    right_motor.hold()

    # Turning grabber_towards the ball
    drive_base.turn(-35)
    drive_base.stop()

    line_follower3(color3,color4,drive_base,left_motor,right_motor)
    drive_base.stop()

    left_motor.run_angle(1000,-10)
    left_motor.hold()

    # moving towards the ball
    drive_base.settings(1000)
    drive_base.straight(-140)
    drive_base.stop()

 

    #pick the ball
    grabber_motor.run_angle(1000, -580)
    grabber_motor.hold()

    # turning towards the ball net
    left_motor.run_angle(1000,-280)
    left_motor.hold()

    # move towards the ball net
    right_motor.run_angle(300,-145,wait = False)
    left_motor.run_angle(300,-145,wait=True)
    right_motor.hold()
    left_motor.hold()

    #pick the ball
    grabber_motor.run_angle(1000,400)
    grabber_motor.stop()

    #leave the ball
    grabber_motor.run_angle(1000,-300)
    grabber_motor.hold()

    # move back after leaving the ball
    right_motor.run_angle(1000,200,wait = False)
    left_motor.run_angle(1000,200,wait=True)
    right_motor.hold()
    left_motor.hold()
    
    # # Turning towards red room
    # right_motor.run_angle(1000,280)
    # right_motor.hold()

    # left_motor.run_angle(1000,-180)
    # left_motor.hold()

    # # moving towards red room to remove marking
    # right_motor.run_angle(1000,-430,wait = False)
    # left_motor.run_angle(1000,-430,wait=True)
    # right_motor.stop()
    # left_motor.stop()

    # right_motor.run_angle(1000,80)
    # right_motor.stop()

    # grabber_motor.run_until_stalled(1000, Stop.HOLD)

    # Going to pick up the laundary
    right_motor.run_angle(1000,-130,wait = False)
    left_motor.run_angle(1000,-130,wait=True)
    right_motor.stop()
    left_motor.stop()

    grabber_motor.run_until_stalled(-1000, Stop.HOLD)

    right_motor.run_angle(1000,80,wait = False)
    left_motor.run_angle(1000,80,wait=True)
    right_motor.hold()
    left_motor.hold()

    #  turning towards black line 
    drive_base.settings(1000)
    drive_base.turn(34)
    drive_base.stop()

    line_follower1(color3,color4,drive_base,left_motor,right_motor,2000)

    
    right_motor.run_angle(1000,80)
    right_motor.stop()

    left_motor.run_angle(1000,805,wait = False)
    right_motor.run_angle(1000,805)
    right_motor.hold()
    left_motor.hold()

    drive_base.settings(1000)
    drive_base.turn(-30)
    drive_base.stop()
    
    laundary(drive_base,left_motor,right_motor,medium_motor,up_sensor, down_sensor)