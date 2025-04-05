#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


left_motor=Motor(Port.A)
right_motor=Motor(Port.D)
grabber_motor=Motor(Port.C)
color3=ColorSensor(Port.S3)
color4=ColorSensor(Port.S4)
drive_base=DriveBase(left_motor,right_motor,45,250)



def line_follower1_white(color3,color4,drive_base,left_motor,right_motor,time):
    stopwatch=StopWatch()
    kd=16
    kp=0.55
    # ki=0.001
    derivative=0
    proportional=0
    error=0
    last_error=0
    steering=0
    # total_error=0
    while stopwatch.time()<=time:
        error=color4.reflection()-color3.reflection()
        # total_error=total_error+error
        derivative=(error-last_error)*kd
        # integral=total_error*ki
        last_error=error
        proportional=error*kp
        steering=proportional+derivative
        drive_base.drive(50,-steering)
        
def line_follower1(color3,color4,drive_base,left_motor,right_motor,time):
    stopwatch=StopWatch()
    kd=16
    kp=0.55
    # ki=0.001
    derivative=0
    proportional=0
    error=0
    last_error=0
    steering=0
    # total_error=0
    while stopwatch.time()<=time:
        error=color4.reflection()-color3.reflection()
        # total_error=total_error+error
        derivative=(error-last_error)*kd
        # integral=total_error*ki
        last_error=error
        proportional=error*kp
        steering=proportional+derivative
        drive_base.drive(50,steering)
    drive_base.stop()

def line_follower2(color3,color4,drive_base,left_motor,right_motor):
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    stopwatch=StopWatch()
    kd=22
    kp=0.3
    derivative=0
    proportional=0
    error=0
    last_error=0
    steering=0
    while  not(left_motor.angle() in range(300, 350) and right_motor.angle() in range (300,350)):
        error=color4.reflection()-color3.reflection()
        derivative=(error-last_error)*kd
        last_error=error
        proportional=error*kp
        steering=proportional+derivative
        drive_base.drive(1000,steering)
    drive_base.stop()

def line_follower4(color3,color4,drive_base,left_motor,right_motor,time):
    stopwatch=StopWatch()
    kd=22
    kp=0.3
    derivative=0
    proportional=0
    error=0
    last_error=0
    steering=0
    while not(color3.reflection()<17 and color4.reflection()<17):
        error=color4.reflection()-color3.reflection()
        derivative=(error-last_error)*kd
        last_error=error
        proportional=error*kp
        steering=proportional+derivative
        drive_base.drive(500,steering)


# def line_follower3(color3,color4,drive_base,left_motor,right_motor):
#     kd=100
#     kp=0.5
#     # ki=0.001
#     derivative=0
#     proportional=0
#     error=0
#     last_error=0
#     steering=0
#     total_error=0
#     while not(color3.reflection()<17 and color4.reflection()<17):
#         error=color4.reflection()-color3.reflection()
#         # total_error=total_error+error
#         derivative=(error-last_error)*kd
#         # integral=total_error*ki
#         last_error=error
#         proportional=error*kp
#         steering=proportional+derivative
#         drive_base.drive(100,steering)

def line_follower3(color3,color4,drive_base,left_motor,right_motor):
    kd=16
    kp=0.55
    # ki=0.001
    derivative=0
    proportional=0
    error=0
    last_error=0
    steering=0
    while not(color3.reflection()<17 and color4.reflection()<17):
        error=color4.reflection()-color3.reflection()
        # total_error=total_error+error
        derivative=(error-last_error)*kd
        # integral=total_error*ki
        last_error=error
        proportional=error*kp
        steering=proportional+derivative
        drive_base.drive(50,steering)
    drive_base.stop()
        
def White_line_follower3(color3,color4,drive_base,left_motor,right_motor):
    kd=16
    kp=0.55
    # ki=0.001
    derivative=0
    proportional=0
    error=0
    last_error=0
    steering=0
    while not(color3.reflection()<17 and color4.reflection()<17):
        error=color4.reflection()-color3.reflection()
        # total_error=total_error+error
        derivative=(error-last_error)*kd
        # integral=total_error*ki
        last_error=error
        proportional=error*kp
        steering=proportional+derivative
        drive_base.drive(50,-steering)
        
def line_follower3_with_grabber_up(color3,color4,drive_base,left_motor,right_motor):
    kd=16
    kp=0.55
    # ki=0.001
    derivative=0
    proportional=0
    error=0
    last_error=0
    steering=0
    while not(color3.reflection()<17 and color4.reflection()<17):
        error=color4.reflection()-color3.reflection()
        # total_error=total_error+error
        derivative=(error-last_error)*kd
        # integral=total_error*ki
        last_error=error
        proportional=error*kp
        steering=proportional+derivative
        drive_base.drive(50,steering)
    drive_base.stop()
    
    grabber_motor.run_until_stalled(1000,Stop.BRAKE)
    grabber_motor.stop()

def line_follower1_with_grabber_up(color3,color4,drive_base,left_motor,right_motor,time):
    stopwatch=StopWatch()
    kd=16
    kp=0.55
    # ki=0.001
    derivative=0
    proportional=0
    error=0
    last_error=0
    steering=0
    # total_error=0
    while stopwatch.time()<=time:
        error=color4.reflection()-color3.reflection()
        # total_error=total_error+error
        derivative=(error-last_error)*kd
        # integral=total_error*ki
        last_error=error
        proportional=error*kp
        steering=proportional+derivative
        drive_base.drive(50,steering)
    
    drive_base.stop()

    grabber_motor.run_until_stalled(1000,Stop.BRAKE)
    grabber_motor.stop()

def line_follower_fast(color3,color4,drive_base,left_motor,right_motor,time):
    kd=200
    kp=1
    # ki=0.001
    derivative=0
    proportional=0
    error=0
    last_error=0
    steering=0
    while not(color3.reflection()<17 and color4.reflection()<17):
        error=color4.reflection()-color3.reflection()
        # total_error=total_error+error
        derivative=(error-last_error)*kd
        # integral=total_error*ki
        last_error=error
        proportional=error*kp
        steering=proportional+derivative
        drive_base.drive(1000,steering)
    drive_base.stop()
