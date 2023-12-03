#region VEXcode Generated Robot Configuration
from vex import *
import random

# Brain should be defined by default
brain=Brain()

# Robot configuration code
Left1 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
Left2 = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
Left3 = Motor(Ports.PORT5, GearSetting.RATIO_18_1, False)
Right1 = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
Right2 = Motor(Ports.PORT4, GearSetting.RATIO_18_1, False)
Right3 = Motor(Ports.PORT6, GearSetting.RATIO_18_1, False)
right_motor_a = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
right_motor_b = Motor(Ports.PORT4, GearSetting.RATIO_18_1, True)
controller_1 = Controller(PRIMARY)
intake = Motor(Ports.PORT6, GearSetting.RATIO_6_1, False)
catapult = Motor(Ports.PORT7, GearSetting.RATIO_18_1, False)

def intakey():
    #controller_1.buttonRight.pressed(intake.spin(REVERSE))
    #controller_1.buttonLeft.pressed(intake.spin(FORWARD))
    #controller_1.buttonX.pressed(intake.stop())
    while controller_1.buttonRight.pressing():
        intake.spin(REVERSE)
    while controller_1.buttonLeft.pressing():
        intake.spin(FORWARD)

#def catapulty():
    #while controller.buttonR1.pressing():
    #    catapult.spin(REVERSE)
    #controller_1.buttonR1.pressed(catapult.spin(REVERSE))
    #controller_1.buttonR1.pressed(catapult.stop())

#can we write our own drivetrain control program? instead of using a drivechain motor group
#the drivechain control motor group does not allow us to set custom wheel sizes, such as 4.125
#it will be immensly harder, maybe impossible to implement PID control into autonomous programs in the future
#keep what you have right now, but see if you can make a better one

def forward_reverse():
    while (controller_1.axis3.position() or controller_1.axis1.position()):
        x = controller_1.axis3.position()
        y = controller_1.axis1.position()
        left = x - y
        
        Left1.set_velocity(abs(x), PERCENT)
        Left2.set_velocity(abs(x), PERCENT)
        Left3.set_velocity(abs(x), PERCENT)
        Right1.set_velocity(abs(x), PERCENT)
        Right2.set_velocity(abs(x), PERCENT)
        Right3.set_velocity(abs(x), PERCENT)
        if x > 0:
            Left1.spin_for(FORWARD, 25, DEGREES)
            Left2.spin_for(FORWARD, 25, DEGREES)
            Left3.spin_for(FORWARD, 25, DEGREES)
            Right1.spin_for(FORWARD, 25, DEGREES)
            Right2.spin_for(FORWARD, 25, DEGREES)
            Right3.spin_for(FORWARD, 25, DEGREES)
        if x < 0:
            Left1.spin_for(REVERSE, 25, DEGREES)
            Left2.spin_for(REVERSE, 25, DEGREES)
            Left3.spin_for(REVERSE, 25, DEGREES)
            Right1.spin_for(REVERSE, 25, DEGREES)
            Right2.spin_for(REVERSE, 25, DEGREES)
            Right3.spin_for(REVERSE, 25, DEGREES)
    



def left_right():
    pass

def driver_control():
    print("hello")
    while True:
        print("hello1")
        forward_reverse()
        print("hello2")
        left_right()
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