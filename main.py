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

grabber_used = ""

stopwatch123=StopWatch()

drive_base.settings(1000)
drive_base.turn(-17)
drive_base.stop(Stop.COAST)

# # #turn with left_motor
# left_motor.run_angle(1000,-200)
# left_motor.brake()

#move straight after turning

left_motor.run_angle(1000,250,wait=False)
right_motor.run_angle(1000,250)
left_motor.hold()
right_motor.hold()

#line follow till water block
line_follower1(color3,color4,drive_base,left_motor,right_motor,1400)
drive_base.stop()

#move to grab the water block
drive_base.settings(1000)
drive_base.straight(52)
drive_base.stop(Stop.BRAKE)

#pick up the water block
grabber_motor.run_angle(1000,300)
grabber_motor.stop()

right_motor.run_angle(1000,-416,wait = False)
left_motor.run_angle(1000,-416)
left_motor.stop()
right_motor.stop()

left_motor.run_angle(500, -385)
left_motor.stop()

left_motor.run_angle(1000,450,wait=False)
right_motor.run_angle(1000,450)
left_motor.hold()
right_motor.hold()

line_follower1(color3,color4,drive_base,left_motor,right_motor,1200)
drive_base.stop()

line_follower2(color3,color4,drive_base,left_motor,right_motor)
drive_base.stop()

line_follower3(color3,color4,drive_base,left_motor,right_motor)
drive_base.stop()


#turn to sense the marking block
right_motor.run_angle(1000,170)
right_motor.hold()

#move forward to sense the marking block
drive_base.settings(1000)
drive_base.straight(75)
drive_base.stop()


blue_marking = down_sensor.reflection() 
blue_marking_color = down_sensor.color() 
laundry_block=0
green_block = 0
white_block = 0

c = ""
if blue_marking > 20:
    white_block +=1
    c = "White"
else:
    c = "Green"
    green_block += 1
        

print("reflected value = ", blue_marking, "\nAssumed color = " ,c,"\nData of BLUE ROOM\n")
print(c)
# white marking block
if c == "White" :
    blue_white(color3,color4,drive_base,left_motor,right_motor,grabber_motor)
    grabber_used ="B"
else:
    blue_green(color3,color4,drive_base,left_motor,right_motor,grabber_motor)
# # going to yellow room
# right_motor.run_angle(1000,-50,wait = False)
# left_motor.run_angle(1000,-50)
# left_motor.hold()
# right_motor.hold()

# left_motor.run_angle(1000,200)
# left_motor.hold()



# right_motor.run_angle(1000,210,wait = False)
# left_motor.run_angle(1000,210)
# left_motor.hold()
# right_motor.hold()

    
# left_motor.run_angle(1000,20)
# left_motor.hold()

      
# # Sensing yellow room marking
# yellow_marking = down_sensor.reflection() 
# laundry_block=0
# a = ""
# if yellow_marking > 20:
#     white_block +=1
#     a = "White"
# else:
#     a = "Green"
#     green_block += 1
# print("\nreflected value = ", yellow_marking, "\nAssumed color = " , a,"\nData of YELLOW ROOM\n")

# right_motor.run_angle(1000,20,wait = False)
# left_motor.run_angle(1000,20)
# left_motor.hold()
# right_motor.hold()

# left_motor.run_angle(1000,-20)
# left_motor.hold()

# # white marking block

# if a == "White":
#     yellow_white(color3,color4,drive_base,left_motor,right_motor,grabber_motor)
#     grabber_used ="Y"
#     # move_to_red_from_water(color3,color4,drive_base,left_motor,right_motor,down_sensor)
# else:
#     yellow_green(color3,color4,drive_base,left_motor,right_motor,grabber_motor)
# abc(green_block,grabber_used) # function to move from other side


# last_two_marking_is_white(color3,color4,drive_base,left_motor,right_motor,down_sensor,green_block)

print("\nTotal white block = ", white_block)
print("Total green block = ", green_block)
print(stopwatch123.time())