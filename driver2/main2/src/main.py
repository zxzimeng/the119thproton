import vex;
from vex import *;
import random;

brain = Brain()

Left1 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
Left2 = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
Left3 = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
Right1 = Motor(Ports.PORT8, GearSetting.RATIO_18_1, False)
Right2 = Motor(Ports.PORT9, GearSetting.RATIO_18_1, True)
Right3 = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
intake = Motor(Ports.PORT4, GearSetting.RATIO_36_1, False)
catapult = Motor(Ports.PORT5, GearSetting.RATIO_36_1, False)
biden = DigitalOut(brain.three_wire_port.a)
trump = DigitalOut(brain.three_wire_port.b)
controller1 = Controller(PRIMARY)


l = MotorGroup(Left1, Left2, Left3)
r = MotorGroup(Right1, Right2, Right3)
t = MotorGroup(Left1, Left2, Left3, Right1, Right2, Right3)

pressed1 = False
pressed2 = False

# NEEDS TO BE REVERSED: LEFT 2, RIGHT 1

x_pos = 0
y_pos = 0
dx = 0
dy = 0
const = 1
pxc = 1
pyc = 1
left = 0
right = 0

def spinfirst():                #CATAPULT
    global pressed1
    if pressed1:
        stopspin()
        # pressed1 = False
        return
    print("T1.2")
    intake.set_velocity(60)
    intake.spin(FORWARD)
    catapult.spin(FORWARD)
    # wait(0.25, SECONDS)
def spinsecond():              #INTAKE
    global pressed2
    print("T1.1")
    if pressed2:
        stopspin()
        # pressed2 = False
        return
    intake.set_velocity(100, PERCENT)
    intake.spin(REVERSE)
    # catapult.spin(REVERSE)
    # wait(0.25, SECONDS)
def stopspin():
    intake.set_velocity(0, PERCENT)
    print("T3.2")
    catapult.stop()
    intake.stop()
    # pressed1 = False
    # pressed2 = False
def pressedstop1():
    global pressed1
    if (pressed1):
        pressed1 = False
        return
    pressed1 = True
def pressedstop2():
    global pressed2
    if (pressed2):
        pressed2 = False
        return
    pressed2 = True

def intacata():
    # if (not intake.is_spinning()):
    #     # print("T1")
    #     if controller1.buttonL1.pressing():
    #         print("T1.2")
    #         intake.set_velocity(100, PERCENT)
    #         intake.spin(REVERSE)
    #         # intake.spin(REVERSE)
    #         catapult.spin(FORWARD)
    #         wait(5, SECONDS)
    #     if controller1.buttonL2.pressing():
    #         print("T1.1")
    #         intake.set_velocity(100, PERCENT)
    #         intake.spin(FORWARD)
    #         # catapult.spin(REVERSE)
    #         wait(5, SECONDS)
    # else:
    #     print("T2")
    #     if (controller1.buttonL2.pressing() or controller1.buttonL1.pressing()):
    #         intake.set_velocity(0, PERCENT)
    #         print("T2.1")
    #         intake.stop()
    #         catapult.stop()
    #         wait(0.25, SECONDS)

    controller1.buttonL1.pressed(spinsecond)
    controller1.buttonL1.released(pressedstop2)
    controller1.buttonL2.pressed(spinfirst)
    controller1.buttonL2.released(pressedstop1)
    controller1.buttonR2.pressed(stopspin)

    # BACKUP CODE
    # intake.set_velocity(100, PERCENT)
    # controller1.buttonL1.pressed(intake.spin, tuple([REVERSE]))
    # controller1.buttonL2.pressed(intake.spin, tuple([FORWARD]))
    # controller1.buttonX.pressed(intake.stop)

def catapulty():
    if controller1.buttonR1.pressing():
        print("T3.1")
        intake.set_velocity(60, PERCENT)
        catapult.spin(REVERSE)
        intake.spin(FORWARD)
    if controller1.buttonR2.pressing():
        intake.set_velocity(0, PERCENT)
        print("T3.2")
        catapult.stop()
        intake.stop()

def joystick():
    global x_pos
    global y_pos
    global pxc
    global pyc
    global left
    global right
    y = controller1.axis2.position()
    x = controller1.axis4.position()
    dx = x - x_pos
    dy = y - y_pos
    # if dy | dx:
    #     print(x, dx, x_pos, y, dy, y_pos)
    x_pos = x
    y_pos = y
    calibrator = 50 * 0.0275 #the first number is a number between 1 and 100, the core calibrator. the second number is the compensation for the quick time of iteration in the while loop
    
    if not x and not y:
        l.stop()
        r.stop()
        left = 0
        right = 0
    dx *= 1 #compensation for the quick iteration of the while loop
    dy *= 1 #compensation for the quick iteration of the while loop
    sign = 1
    if ((abs(dx) > 2) & (abs(dx) < 95)):
        sign = x/dx
        if (sign > 0):
            sign = 1
        elif (sign < 0):
            sign = -1
        pxc = sign * calibrator * (abs(dx) / 100)
    if (abs(dy) > 2) & (abs(dy) < 95):
        sign = y/dy
        if (sign > 0):
            sign = 1
        elif sign < 0:
            sign = -1
        pyc = calibrator * (abs(dy) / 100)
    if (abs(dx) > 2 or abs(dy) > 2):
        if (abs(dx) < 2):
            pxc = 0
        if (abs(dy) < 2):
            pyc = 0
        left += const * (pyc * y + pxc * x)
        right += const * (pyc * y - pxc * x)
        if (left > 100 and right > 100):
            left = 100
            right = 100                            #  <-- for efficiency purposes
        if (left < -100 and right < -100):
            left = -100
            right = -100
        else:
            if (left > 100):
                left = 100
            if (right > 100):
                right = 100
            if (left < -100):
                left = -100
            if (right < -100):
                right = -100
        
        if x == 0:
            c = (left + right)/2
            left = c
            right = c
        if y == 0:
            c = (left + right)/2 #gives throttle
            left -= c
            right -= c


    # BACKUP:
    # left = const * (y + x)
    # right = const * (y - x)
    # if not (not (dx or dy)):
    print("   " + str(left) + "(" + str(dx) + " - " + str(y + x) + ", " + str(x_pos) + ": " + str(x_pos == x) + "), " + str(right) + "(" + str(dy) + " - " + str(y - x) + ", " + str(y_pos) + ": " + str(y_pos == y) + ")")
    l.set_velocity(-1 * left, PERCENT)
    r.set_velocity(-1 * right, PERCENT)
    l.spin(FORWARD)   #PLS UNCOMMENT THIS BACK ON ONCE DONE WITH TESTING (PREVENTS MOTORS FROM MOVING DURING TESTING)
    r.spin(FORWARD)
    

def driver_control():
    controller1.axis2.changed(joystick)
    controller1.axis4.changed(joystick)
    # intacata()
    while True:
        intacata()
        #catapulty() #Shouldn't be here, but just backup
        continue


def autonomous():
    pass

competition = Competition(driver_control, autonomous)