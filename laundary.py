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

ev3 = EV3Brick()
down_sensor = ColorSensorNXT(Port.S1)
up_sensor = ColorSensorNXT(Port.S2)
color3=ColorSensor(Port.S3)
color4=ColorSensor(Port.S4)
left_motor=Motor(Port.A)
right_motor=Motor(Port.D)
grabber_motor=Motor(Port.C)
Medium_motor = Motor(Port.B)
drive_base=DriveBase(left_motor,right_motor,45,250)
color3=ColorSensor(Port.S3)
color4=ColorSensor(Port.S4)

def laundary(drive_base,left_motor,right_motor,medium_motor,up_sensor, down_sensor):
    # Opening the grabber
    grabber_motor.run_angle(1000,330)
    grabber_motor.stop()

    # following line till intersection
    line_follower3(color3,color4,drive_base,left_motor,right_motor) 
    drive_base.stop()

    # shifting the laundary container
    left_motor.run_angle(300,200,wait = False)
    right_motor.run_angle(300,200)
    right_motor.hold()
    left_motor.hold()

    # moving back to turn
    left_motor.run_angle(300,-20,wait = False)
    right_motor.run_angle(300,-20)
    right_motor.hold()
    left_motor.hold()

    # turning the robot so that line sensors can come above the black line
    right_motor.run_angle(1000,-450)
    right_motor.hold()

    # Moving back to give time to follow line
    right_motor.run_angle(1000,-70,wait = False)
    left_motor.run_angle(1000,-70)
    left_motor.hold()
    right_motor.hold()

    # following line till intersection and down senor will sense the first container
    line_follower1(color3,color4,drive_base,left_motor,right_motor,1050) 
    drive_base.stop()
        
    laundary_1 = down_sensor.color()
    # sensing the first container reflected intensity
    laundary_1_reflected = down_sensor.reflection()
    First_Container = ""
    # Findind laundary container color
    if (laundary_1 == Color.BLACK)or(laundary_1==None):
        First_Container = ("Black")
    elif (laundary_1 == Color.YELLOW)  or (laundary_1 == Color.WHITE):
        First_Container = ("Yellow")
    elif laundary_1 == Color.RED:
        First_Container = ("Red")
    print("First container_Sensed_color = ", laundary_1, "  reflected intensity = ",laundary_1_reflected,"\nAssumed color = ",First_Container,"\n")

    laundary_block1 = up_sensor.color()
    laundary_block1_reflected = up_sensor.reflection()

    First_Block = ("")
    if (laundary_block1 == Color.BLACK) or (laundary_block1 == None):
        if laundary_block1_reflected  < 20:
            First_Block = ("Black")
        else:
            First_Block = ("Yellow")
            
    elif (laundary_block1 == Color.YELLOW) or (laundary_block1 == Color.WHITE):
        if laundary_block1_reflected  < 20:
            First_Block = ("Black")
        else:
            First_Block = ("Yellow")
        
    elif laundary_block1 == Color.RED:
        if laundary_block1_reflected  < 19:
            First_Block = ("Black")
        else:
            First_Block = ("Red")
    print("\n","First Block sensed color = ", laundary_block1 ,"   reflected intensity = ",laundary_block1_reflected,"\nAssumed color = ", First_Block, "\n")

    if  First_Container == First_Block :
        
        # Moving back to drop the laundary block
        left_motor.run_angle(1000,-30,wait=False)
        right_motor.run_angle(1000, -30)
        left_motor.hold()
        right_motor.hold()
        
        medium_motor.run_until_stalled(1000, Stop.BRAKE)
        medium_motor.run_angle(1000,-55)
        medium_motor.stop()
        
        # Going to sense the second container
        line_follower3(color3,color4,drive_base,left_motor,right_motor)
        drive_base.stop()
        
        line_follower1(color3,color4,drive_base,left_motor,right_motor,700)
        drive_base.stop()

        
        # sensing the second container
        laundary_2 = down_sensor.color()
        laundary_2_reflected = down_sensor.reflection()
        Second_Container = ("")
        if (laundary_2 == Color.BLACK) or (laundary_2==None):
            Second_Container = ("Black")    
        elif (laundary_2 == Color.YELLOW) or (laundary_2 == Color.WHITE):
            Second_Container = ("Yellow")
        elif laundary_2 == Color.RED:
            Second_Container = ("Red")
        print( "Second_container_Sensed_color = ", laundary_2, "\nAssumed color = ",Second_Container)
        
        # Sensing the second block
        laundary_block2 = up_sensor.color()
        laundary_block2_reflected = up_sensor.reflection()
        Second_Block = ("")
        if (laundary_block2 == Color.BLACK) or (laundary_block2 == None):
            if laundary_block1_reflected  < 20:
                Second_Block = ("Black")
            else:
                Second_Block = ("Yellow")
        elif (laundary_block2 == Color.YELLOW) or (laundary_block2 == Color.WHITE):
            if laundary_block2_reflected  < 20:
                Second_Block = ("Black")
            else:
                Second_Block = ("Yellow")    
        elif laundary_block2 == Color.RED:
            if laundary_block2_reflected  < 20:
                Second_Block = ("Black")
            else:
                Second_Block = ("Red")
        print("\n", "Second Block sensed color = ", laundary_block2 ,"   reflected intensity = ",laundary_block2_reflected,"\nAssumed color = ", Second_Block, "\n")
        
        if Second_Container == Second_Block:
            #  moving back to drop the second block
            left_motor.run_angle(1000,-40,wait=False)
            right_motor.run_angle(1000, -40)
            left_motor.hold()
            right_motor.hold()
            
            medium_motor.run_until_stalled(1000, Stop.BRAKE)
            medium_motor.run_angle(1000,-55)
            medium_motor.stop()
            
            # lifting the water side grabber to save the people life because life matters
            grabber_motor.run_until_stalled(1000,Stop.BRAKE)
            
            # Going to drop the third block in third container
            line_follower1(color3,color4,drive_base,left_motor,right_motor,1400)
            drive_base.stop()

            medium_motor.run_until_stalled(1000, Stop.BRAKE)
            medium_motor.run_angle(1000,-55)
            medium_motor.stop()
            
            left_motor.run_angle(1000,-260,wait = False)
            right_motor.run_angle(1000,-260)
            right_motor.hold()
            left_motor.hold()
            
            line_follower3(color3,color4,drive_base,left_motor,right_motor)
            drive_base.stop()
            
        else:
            # lifting the water side grabber to save the people life because life matters
            grabber_motor.run_until_stalled(1000,Stop.BRAKE)
            
            line_follower1(color3,color4,drive_base,left_motor,right_motor,1100)
            drive_base.stop()
            
            # dropped in third container
            medium_motor.run_until_stalled(1000, Stop.BRAKE)
            medium_motor.run_angle(1000,-55)
            medium_motor.stop()
            
            #  moving back to drop the second block
            left_motor.run_angle(1000,-170,wait=False)
            right_motor.run_angle(1000, -170)
            left_motor.hold()
            right_motor.hold()
            
            medium_motor.run_until_stalled(1000, Stop.BRAKE)
            medium_motor.run_angle(1000,-55)
            medium_motor.stop()
            
            left_motor.run_angle(1000,-150,wait = False)
            right_motor.run_angle(1000,-150)
            left_motor.hold()
            right_motor.hold()
            
            line_follower3(color3,color4,drive_base,left_motor,right_motor)
            drive_base.stop()
            
    else:
        # Going to sense the second container
        line_follower3(color3,color4,drive_base,left_motor,right_motor)
        drive_base.stop()
        line_follower1(color3,color4,drive_base,left_motor,right_motor,800)
        drive_base.stop()
        
        # sensing the second container
        laundary_2 = down_sensor.color()
        laundary_2_reflected = down_sensor.reflection()
        Second_Container = ("")
        if (laundary_2 == Color.BLACK) or (laundary_2==None):
            Second_Container = ("Black")    
        elif (laundary_2 == Color.YELLOW) or (laundary_2 == Color.WHITE):
            Second_Container = ("Yellow")
        elif laundary_2 == Color.RED:
            Second_Container = ("Red")
        print( "Second_container_Sensed_color = ", laundary_2, "\nAssumed color = ",Second_Container)
        
        if Second_Container == First_Block:
            
            # Moving back to drop the laundary block in second Container
            left_motor.run_angle(1000,-30,wait=False)
            right_motor.run_angle(1000, -30)
            left_motor.hold()
            right_motor.hold()
            
            # Dropping First block in second Container
            medium_motor.run_until_stalled(1000, Stop.BRAKE)
            medium_motor.run_angle(1000,-55)
            medium_motor.hold()
            
            # Sensing the second block
            laundary_block2 = up_sensor.color()
            laundary_block2_reflected = up_sensor.reflection()
            Second_Block = ("")
            if (laundary_block2 == Color.BLACK) or (laundary_block2 == None):
                if laundary_block1_reflected  < 20:
                    Second_Block = ("Black")
                else:
                    Second_Block = ("Yellow")
            elif (laundary_block2 == Color.YELLOW) or (laundary_block2 == Color.WHITE):
                if laundary_block2_reflected  < 20:
                    Second_Block = ("Black")
                else:
                    Second_Block = ("Yellow")    
            elif laundary_block2 == Color.RED:
                if laundary_block2_reflected  < 15:
                    Second_Block = ("Black")
                else:
                    Second_Block = ("Red")
            print("\n", "Second Block sensed color = ", laundary_block2 ,"   reflected intensity = ",laundary_block2_reflected,"\nAssumed color = ", Second_Block, "\n")
            
            if First_Container == Second_Block:
                
                left_motor.run_angle(1000,-140,wait = False)
                right_motor.run_angle(1000,-140)
                right_motor.hold()
                left_motor.hold()
                
                # Dropping the Second block in First container
                medium_motor.run_until_stalled(1000, Stop.BRAKE)
                medium_motor.run_angle(1000,-55)
                medium_motor.hold()
                
                # lifting the water side grabber to save the people life because life matters
                grabber_motor.run_until_stalled(1000,Stop.BRAKE)
                
                # Dropping the third block in third container
                line_follower3(color3,color4,drive_base,left_motor,right_motor)
                drive_base.stop()
                
                line_follower1(color3,color4,drive_base,left_motor,right_motor,1600)
                drive_base.stop()
                
                medium_motor.run_until_stalled(1000, Stop.BRAKE)
                medium_motor.run_angle(1000,-55)
                medium_motor.hold()
                
                left_motor.run_angle(1000,-260,wait = False)
                right_motor.run_angle(1000,-260)
                right_motor.hold()
                left_motor.hold()
                
                line_follower3(color3,color4,drive_base,left_motor,right_motor)
                drive_base.stop()
            else:
                # lifting the water side grabber to save the people life because life matters
                grabber_motor.run_until_stalled(1000,Stop.BRAKE)
                
                line_follower1(color3,color4,drive_base,left_motor,right_motor,1200)
                drive_base.stop()
                
                # Dropping second block in third container
                medium_motor.run_until_stalled(1000, Stop.BRAKE)
                medium_motor.run_angle(1000,-55)
                medium_motor.hold()
                
                # droppig third block in first container
                left_motor.run_angle(1000,-260,wait = False)
                right_motor.run_angle(1000,-260)
                right_motor.hold()
                left_motor.hold()
                
                # Dropping the Second block in First container
                medium_motor.run_until_stalled(1000, Stop.BRAKE)
                medium_motor.run_angle(1000,-55)
                medium_motor.hold()
                
                line_follower3(color3,color4,drive_base,left_motor,right_motor)
                drive_base.stop()
                
        else: # Third Container == First Block
            # lifting the water side grabber to save the people life because life matters
            grabber_motor.run_until_stalled(1000,Stop.BRAKE)
            
            # Dropping the First block in third container
            line_follower1(color3,color4,drive_base,left_motor,right_motor,900)
            drive_base.stop()
            
            medium_motor.run_until_stalled(1000, Stop.BRAKE)
            medium_motor.run_angle(1000,-55)
            medium_motor.hold()
            
            # Sensing the second block
            laundary_block2 = up_sensor.color()
            laundary_block2_reflected = up_sensor.reflection()
            Second_Block = ("")
            if (laundary_block2 == Color.BLACK) or (laundary_block2 == None):
                if laundary_block1_reflected  < 20:
                    Second_Block = ("Black")
                else:
                    Second_Block = ("Yellow")
            elif (laundary_block2 == Color.YELLOW) or (laundary_block2 == Color.WHITE):
                if laundary_block2_reflected  < 20:
                    Second_Block = ("Black")
                else:
                    Second_Block = ("Yellow")    
            elif laundary_block2 == Color.RED:
                if laundary_block2_reflected  < 15:
                    Second_Block = ("Black")
                else:
                    Second_Block = ("Red")
            print("\n", "Second Block sensed color = ", laundary_block2 ,"   reflected intensity = ",laundary_block2_reflected,"\nAssumed color = ", Second_Block, "\n")
            
            if Second_Container == Second_Block:
                
                left_motor.run_angle(1000,-150,wait = False)
                right_motor.run_angle(1000,-150)
                right_motor.hold()
                left_motor.hold()
                
                # Dropping the Second block in First container
                medium_motor.run_until_stalled(1000, Stop.BRAKE)
                medium_motor.run_angle(1000,-55)
                medium_motor.hold()
                
                left_motor.run_angle(1000,-140,wait = False)
                right_motor.run_angle(1000,-140)
                right_motor.hold()
                left_motor.hold()
                
                # Dropping the Third block in First container
                medium_motor.run_until_stalled(1000, Stop.BRAKE)
                medium_motor.run_angle(1000,-55)
                medium_motor.hold()
                
                line_follower3(color3,color4,drive_base,left_motor,right_motor)
                drive_base.stop()
                
            else: #First Container == Second block
                
                # droppig Second block in first container
                left_motor.run_angle(1000,-260,wait = False)
                right_motor.run_angle(1000,-260)
                right_motor.hold()
                left_motor.hold()
                
                # Dropping the Second block in First container
                medium_motor.run_until_stalled(1000, Stop.BRAKE)
                medium_motor.run_angle(1000,-55)
                medium_motor.hold()
                
                # Dropping the Third block in Second container
                line_follower3(color3,color4,drive_base,left_motor,right_motor)
                drive_base.stop()
                
                line_follower1(color3,color4,drive_base,left_motor,right_motor,600)
                drive_base.stop()
                
                medium_motor.run_until_stalled(1000, Stop.BRAKE)
                medium_motor.run_angle(1000,-55)
                medium_motor.hold()
                
                left_motor.run_angle(1000,-150,wait = False)
                right_motor.run_angle(1000,-150)
                left_motor.hold()
                right_motor.hold()
                
                line_follower1(color3,color4,drive_base,left_motor,right_motor,600)
                drive_base.stop()
                
    grabber_motor.run_until_stalled(-1000, Stop.HOLD)

    left_motor.run_angle(1000,180)
    left_motor.hold()
    right_motor.run_angle(1000,-140)
    right_motor.hold()

    left_motor.run_angle(1000,40,wait=False)
    right_motor.run_angle(1000, 40)
    left_motor.hold()
    right_motor.hold()

    line_follower1(color3,color4,drive_base,left_motor,right_motor,2000)
    drive_base.stop()

    left_motor.run_angle(1000,270,wait = False)
    right_motor.run_angle(1000,270)
    right_motor.hold()
    left_motor.hold()

    drive_base.settings(50)
    drive_base.turn(18)
    drive_base.stop()

    left_motor.run_angle(100,10,wait = False)
    right_motor.run_angle(100,10)
    right_motor.hold()
    left_motor.hold()