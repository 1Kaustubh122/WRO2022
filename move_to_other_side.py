#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor)
from pybricks.nxtdevices import ColorSensor as ColorSensorNXT
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from line_follow import line_follower3
from red_white import last_two_marking_is_white
from blue_room import blue_green,blue_white
from red_room import red_green,red_white, red_white_Y
from yellow_room import yellow_green,yellow_white
from last_two_greens import last_two_green_blocks


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
def abc(green_block,grabber_used):
    if green_block==2:
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
                drive_base.drive(1000,-14)
                
    #moving to second black line
        stopwatch1=StopWatch()
        while stopwatch1.time()<=900:
            drive_base.drive(1000,8)
        drive_base.stop()    
        
        # line_follower3(color3,color4,drive_base,left_motor,right_motor)
        # drive_base.stop()


        drive_base.settings(1000)
        drive_base.straight(20)
        drive_base.stop()

        line_follower3(color3,color4,drive_base,left_motor,right_motor)
        drive_base.stop()
        
        last_two_marking_is_white(color3,color4,drive_base,left_motor,right_motor,down_sensor)
            

    #line following till second black line

    elif green_block==1: # and white block = 1

            #move till center
        drive_base.settings(1000)
        drive_base.straight(120)
        drive_base.stop(Stop.BRAKE) 

        stopwatch=StopWatch()
    #move from center to other side
        drive_base.settings(1000)
        
        
        while stopwatch.time()<=1700:
            if stopwatch.time()<=510:
                drive_base.drive(1000,12) 
            else:
                drive_base.drive(1000,-13)
                
        drive_base.stop()
        
        left_motor.run_angle(1000,220)
        left_motor.brake()
        c=1
        if (color3.reflection()<10 or color4.reflection()<10):
            c=1
            pass

        else:
            left_motor.run_angle(100,100,wait=False)
            right_motor.run_angle(100,100)
            left_motor.hold()
            right_motor.hold()

        if (color3.reflection()<10 or color4.reflection()<10):
            if c!=1:
                left_motor.run_angle(-100,200,wait=False)
                right_motor.run_angle(-100,200)
                left_motor.hold()
                right_motor.hold()
        
        line_follower3(color3,color4,drive_base,left_motor,right_motor)
        drive_base.stop()
        
        right_motor.run_angle(1000,170)
        right_motor.hold()

        #move forward to sense the marking block
        drive_base.settings(1000)
        drive_base.straight(70)
        drive_base.stop(Stop.BRAKE)

        # left_motor.run_angle(1000,20)
        # left_motor.brake()


        red_marking = down_sensor.reflection()
        a = ""
        if red_marking > 25:
            a = "White"
        else:
            a = "Green"
                
        drive_base.settings(1000)
        drive_base.straight(10)
        drive_base.stop(Stop.BRAKE)

        print("reflected value = ", red_marking, "\nAssumed color = " ,a,"\nData of BLUE ROOM\n")
        # print(c)
        # # white marking block
        if a == "White" :
            if grabber_used == "Y": # Yellow room had white marking
                red_white(color3,color4,drive_base,left_motor,right_motor,grabber_motor)
            else: # Blue room had white marking 
                red_white_Y(color3,color4,drive_base,left_motor,right_motor,grabber_motor)
            # green_room_green() 
        else:
            red_green(color3,color4,drive_base,left_motor,right_motor,grabber_motor,grabber_used)

    #for two green blocks on the other side
    else:

            #move till center
        drive_base.settings(1000)
        drive_base.straight(120)
        drive_base.stop(Stop.BRAKE) 

        stopwatch=StopWatch()
    #move from center to other side
        drive_base.settings(1000)
        
        
        while stopwatch.time()<=1700:
            if stopwatch.time()<=550:
                drive_base.drive(1000,12) 
            else:
                drive_base.drive(1000,-13)
                
        drive_base.stop()
                
    #moving to second black line
        stopwatch1=StopWatch()
        while stopwatch1.time()<=900:
            drive_base.drive(1000,16)
        drive_base.stop()    

        drive_base.settings(1000,1000)
        drive_base.straight(20)
        drive_base.stop()

        line_follower3(color3,color4,drive_base,left_motor,right_motor)
        drive_base.stop()
        
        last_two_green_blocks(color3,color4,drive_base,left_motor,right_motor)
        