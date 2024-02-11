import vex
from vex import *
import random

# Brain should be defined by default
brain=Brain()

# Robot configuration code
Left1 = Motor(Ports.PORT7, GearSetting.RATIO_18_1, False)
Left2 = Motor(Ports.PORT8, GearSetting.RATIO_18_1, False)
Left3 = Motor(Ports.PORT9, GearSetting.RATIO_18_1, False)
Right1 = Motor(Ports.PORT13, GearSetting.RATIO_18_1, True)
Right2 = Motor(Ports.PORT14, GearSetting.RATIO_18_1, True)
Right3 = Motor(Ports.PORT15, GearSetting.RATIO_18_1, True)
controller_1 = Controller(PRIMARY)
intake = Motor(Ports.PORT16, GearSetting.RATIO_6_1, False)
catapult = Motor(Ports.PORT10, GearSetting.RATIO_36_1, False)
biden = DigitalOut(brain.three_wire_port.h)
trump = DigitalOut(brain.three_wire_port.g)

leftmotors=MotorGroup(Left1, Left2, Left3)
rightmotors=MotorGroup(Right1, Right2, Right3)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


def bidenDOWN():
    brain.screen.print("2")
    biden.set(True)

def trumpDOWN():
    trump.set(True)

def allUP():
    biden.set(False)
    trump.set(False)

def fly():
    brain.screen.print("1")
    controller_1.buttonY.pressed(bidenDOWN)
    controller_1.buttonA.pressed(trumpDOWN)
    controller_1.buttonRight.pressed(allUP)

def intakey():
    controller_1.buttonL1.pressed(intake.spin, tuple([REVERSE]))
    controller_1.buttonL2.pressed(intake.spin, tuple([FORWARD]))
    controller_1.buttonX.pressed(intake.stop)
    intake.set_velocity(100, PERCENT)
    # while controller_1.buttonRight.pressing():
    #     intake.spin(REVERSE)
    # intake.stop()
    # while controller_1.buttonLeft.pressing():
    #     intake.set_velocity(100, PERCENT)
    #     intake.spin(FORWARD)
    # intake.stop()

def catapulty():
    # while controller_1.buttonR1.pressing():
    #     catapult.spin_for(REVERSE, 10, DEGREES)
    #catapult.set_max_torque(90, PERCENT)
    catapult.set_velocity(75, PERCENT)
    controller_1.buttonR1.pressed(catapult.spin, tuple([REVERSE]))
    controller_1.buttonR2.pressed(catapult.stop)

#can we write our own drivetrain control program? instead of using a drivechain motor group
#the drivechain control motor group does not allow us to set custom wheel sizes, such as 4.125
#it will be immensly harder, maybe impossible to implement PID control into autonomous programs in the future
#keep what you have right now, but see if you can make a better one

def joystick():
        y = controller_1.axis3.position()
        x = controller_1.axis1.position()
        constmax =  0.6

        if y==0 and x==0:
            Left1.stop()
            Left2.stop()
            Left3.stop()
            Right1.stop()
            Right2.stop()
            Right3.stop()

        print(x, y)
        left = constmax * (y + x)
        right = constmax * (y - x)
        Left1.set_velocity(left, PERCENT)
        Left2.set_velocity(left, PERCENT)
        Left3.set_velocity(left, PERCENT)
        Right1.set_velocity(right, PERCENT)
        Right2.set_velocity(right, PERCENT)
        Right3.set_velocity(right, PERCENT)

        Left1.spin(FORWARD)
        Left2.spin(FORWARD)
        Left3.spin(FORWARD)
        Right1.spin(REVERSE)
        Right2.spin(REVERSE)
        Right3.spin(REVERSE)
        
    
def pre_autonomous():
    pass

def driver_control():
    # print("hello")
    intakey()
    catapulty()
    fly()
    print(0)
    # Left1.spin(FORWARD)
    # Left2.spin(FORWARD)
    # Left3.spin(FORWARD)
    # Right1.spin(REVERSE)
    # Right2.spin(REVERSE)
    # Right3.spin(REVERSE)
    leftmotors.spin(FORWARD)
    rightmotors.spin(FORWARD)
    while True:
        print(1)
        leftmotors.set_velocity((controller_1.axis3.position() + controller_1.axis1.position()), PERCENT)
        rightmotors.set_velocity((controller_1.axis3.position() - controller_1.axis1.position()), PERCENT)
        # print("hello1")
        # joystick()
        # print("hello2")
        # print("hello3")
        # print("hello6")
        # print("hello7")
    
def autonomous():
    pass

competition = Competition(driver_control, autonomous)
pre_autonomous()