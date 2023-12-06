import vex
from vex import *
import random

# Brain should be defined by default
brain=Brain()

# Robot configuration code
Left1 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
Left2 = Motor(Ports.PORT8, GearSetting.RATIO_18_1, False)
Left3 = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)
Right1 = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
Right2 = Motor(Ports.PORT4, GearSetting.RATIO_18_1, False)
Right3 = Motor(Ports.PORT5, GearSetting.RATIO_18_1, False)
controller_1 = Controller(PRIMARY)
intake = Motor(Ports.PORT2, GearSetting.RATIO_6_1, False)
catapult = Motor(Ports.PORT20, GearSetting.RATIO_18_1, False)
biden = DigitalOut(brain.three_wire_port.h)
trump = DigitalOut(brain.three_wire_port.g)

driveMotorsList = []
driveMotorsList.append(Left1)
driveMotorsList.append(Left2)
driveMotorsList.append(Left3)
driveMotorsList.append(Right1)
driveMotorsList.append(Right2)
driveMotorsList.append(Right3)


def intakey():
    #controller_1.buttonRight.pressed(intake.spin(REVERSE))
    #controller_1.buttonLeft.pressed(intake.spin(FORWARD))
    #controller_1.buttonX.pressed(intake.stop())
    intake.set_velocity(100, PERCENT)
    while controller_1.buttonRight.pressing():
        intake.spin(REVERSE)
    intake.stop()
    while controller_1.buttonLeft.pressing():
        intake.set_velocity(100, PERCENT)
        intake.spin(FORWARD)
    intake.stop()

def catapulty():
    while controller_1.buttonR1.pressing():
        catapult.spin_for(REVERSE, 10, DEGREES)
    #controller_1.buttonR1.pressed(catapult.spin(REVERSE))
    #controller_1.buttonR1.pressed(catapult.stop())

#can we write our own drivetrain control program? instead of using a drivechain motor group
#the drivechain control motor group does not allow us to set custom wheel sizes, such as 4.125
#it will be immensly harder, maybe impossible to implement PID control into autonomous programs in the future
#keep what you have right now, but see if you can make a better one

def joystick():
    while (controller_1.axis3.position() or controller_1.axis1.position()):
        y = controller_1.axis3.position()
        x = controller_1.axis1.position()
        left = y + x
        right = y - x
        t1 = Timer()
        Left1.set_velocity(left, PERCENT)
        Left2.set_velocity(left, PERCENT)
        Left3.set_velocity(left, PERCENT)
        Right1.set_velocity(right, PERCENT)
        Right2.set_velocity(right, PERCENT)
        Right3.set_velocity(right, PERCENT)
        t1.clear()
        while t1.time() < 50:
            Left1.spin(FORWARD)
            Left2.spin(FORWARD)
            Left3.spin(FORWARD)
            Right1.spin(REVERSE)
            Right2.spin(REVERSE)
            Right3.spin(REVERSE)
        
        Left1.stop()
        Left2.stop()
        Left3.stop()
        Right1.stop()
        Right2.stop()
        Right3.stop()
    

def driver_control():
    print("hello")
    while True:
        print("hello1")
        joystick()
        print("hello2")
        print("hello3")
        intakey()
        print("hello6")
        #catapulty()
        print("hello7")
    
def autonomous():
    pass
# function already defined line 18 (153, 1)
# Function 'intake' has no 'spin' member (154, 38)
# Function 'intake' has no 'spin' member (155, 37)
# Function 'intake' has no 'stop' member (156, 34)
competition = Competition(driver_control, autonomous)