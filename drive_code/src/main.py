# import vex;
# from vex import *;
# import random;

# brain = Brain()

# Left1 = Motor(Ports.PORT1, GearSetting.RATIO_6_1, False)
# Left2 = Motor(Ports.PORT2, GearSetting.RATIO_6_1, True)
# Left3 = Motor(Ports.PORT3, GearSetting.RATIO_6_1, False)
# Right1 = Motor(Ports.PORT8, GearSetting.RATIO_6_1, False)
# Right2 = Motor(Ports.PORT9, GearSetting.RATIO_6_1, True)
# Right3 = Motor(Ports.PORT10, GearSetting.RATIO_6_1, True)
# intake = Motor(Ports.PORT4, GearSetting.RATIO_36_1, False)
# catapult = Motor(Ports.PORT6, GearSetting.RATIO_36_1, False)
# biden = DigitalOut(brain.three_wire_port.a)
# trump = DigitalOut(brain.three_wire_port.b)
# controller1 = Controller(PRIMARY)


# l = MotorGroup(Left1, Left2, Left3)
# r = MotorGroup(Right1, Right2, Right3)
# t = MotorGroup(Left1, Left2, Left3, Right1, Right2, Right3)
# t.set_stopping(BRAKE)

# pressed1 = False
# pressed2 = False
# bidenpressed = False
# trumppressed = False

# # NEEDS TO BE REVERSED: LEFT 2, RIGHT 1

# x_pos = 0
# y_pos = 0
# dx = 0
# dy = 0
# const = 1
# pxc = 1
# pyc = 1
# left = 0
# right = 0
# yside = 0
# xside = 0



# def left():
#     global bidenpressed
#     if bidenpressed:
#         biden.set(False)
#         return
#     biden.set(True)
# def right():
#     global trumppressed
#     if trumppressed:
#         trump.set(False)
#         return
#     trump.set(True)
# def stopleft():
#     global bidenpressed
#     if bidenpressed:
#         bidenpressed = False
#         return
#     bidenpressed = True
# def stopright():
#     global trumppressed
#     if trumppressed:
#         trumppressed = False
#         return
#     trumppressed = True

# def wings():
#     controller1.buttonLeft.pressed(left)
#     controller1.buttonLeft.released(stopleft)
#     controller1.buttonRight.pressed(right)
#     controller1.buttonRight.released(stopright)


# def spinfirst():                #CATAPULT
#     global pressed1
#     if pressed1:
#         stopspin()
#         # pressed1 = False
#         return
#     print("T1.2")
#     intake.set_velocity(18, PERCENT)
#     catapult.set_velocity(30, PERCENT)
#     intake.spin(FORWARD)
#     catapult.spin(REVERSE)
#     # wait(0.25, SECONDS)
# def spinsecond():              #INTAKE
#     global pressed2
#     print("T1.1")
#     if pressed2:
#         stopspin()
#         # pressed2 = False
#         return
#     intake.set_velocity(100, PERCENT)
#     intake.spin(REVERSE)
#     # catapult.spin(REVERSE)
#     # wait(0.25, SECONDS)
# def stopspin():
#     intake.set_velocity(0, PERCENT)
#     print("T3.2")
#     catapult.stop()
#     intake.stop()
#     # pressed1 = False
#     # pressed2 = False
# def pressedstop1():
#     global pressed1
#     if (pressed1):
#         pressed1 = False
#         return
#     pressed1 = True
# def pressedstop2():
#     global pressed2
#     if (pressed2):
#         pressed2 = False
#         return
#     pressed2 = True

# def intacata():
#     # if (not intake.is_spinning()):
#     #     # print("T1")
#     #     if controller1.buttonL1.pressing():
#     #         print("T1.2")
#     #         intake.set_velocity(100, PERCENT)
#     #         intake.spin(REVERSE)
#     #         # intake.spin(REVERSE)
#     #         catapult.spin(FORWARD)
#     #         wait(5, SECONDS)
#     #     if controller1.buttonL2.pressing():
#     #         print("T1.1")
#     #         intake.set_velocity(100, PERCENT)
#     #         intake.spin(FORWARD)
#     #         # catapult.spin(REVERSE)
#     #         wait(5, SECONDS)
#     # else:
#     #     print("T2")
#     #     if (controller1.buttonL2.pressing() or controller1.buttonL1.pressing()):
#     #         intake.set_velocity(0, PERCENT)
#     #         print("T2.1")
#     #         intake.stop()
#     #         catapult.stop()
#     #         wait(0.25, SECONDS)

#     controller1.buttonL1.pressed(spinsecond)
#     controller1.buttonL1.released(pressedstop2)
#     controller1.buttonL2.pressed(spinfirst)
#     controller1.buttonL2.released(pressedstop1)
#     controller1.buttonR2.pressed(stopspin)

#     # BACKUP CODE
#     # intake.set_velocity(100, PERCENT)
#     # controller1.buttonL1.pressed(intake.spin, tuple([REVERSE]))
#     # controller1.buttonL2.pressed(intake.spin, tuple([FORWARD]))
#     # controller1.buttonX.pressed(intake.stop)

# def catapulty():
#     if controller1.buttonR1.pressing():
#         print("T3.1")
#         intake.set_velocity(60, PERCENT)
#         catapult.spin(REVERSE)
#         intake.spin(FORWARD)
#     if controller1.buttonR2.pressing():
#         intake.set_velocity(0, PERCENT)
#         print("T3.2")
#         catapult.stop()
#         intake.stop()

# def joystick():
#     global x_pos
#     global y_pos
#     global pxc
#     global pyc
#     global left
#     global right
#     global yside
#     global xside
#     y = controller1.axis2.position()
#     x = controller1.axis4.position()
#     dx = x - x_pos
#     dy = y - y_pos
#     # if dy | dx:
#     #     print(x, dx, x_pos, y, dy, y_pos)
#     x_pos = x
#     y_pos = y
#     calibrator = 50 * 0.0275 #the first number is a number between 1 and 100, the core calibrator. the second number is the compensation for the quick time of iteration in the while loop
    
#     if not x and not y:
#         l.stop()
#         r.stop()
#         left = 0
#         right = 0
#     dx *= 1 #compensation for the quick iteration of the while loop
#     dy *= 1 #compensation for the quick iteration of the while loop
#     sign = 1
#     c = (left + right)/2
#     # if (x > 0):                      #this is for reseting the pointer mechanism after the joystick has passed the center
#     #     if xside == 0:
#     #         yside = 1
#     #     if xside < 0:
#     #         xside = 1
#     #         left = c
#     #         right = c
#     #         dx = x
#     # if (x < 0):
#     #     if xside == 0:
#     #         xside = -1
#     #     if xside > 0:
#     #         xside = -1
#     #         left = c
#     #         right = c
#     #         dx = x
#     # if (y > 0):
#     #     if (yside == 0):
#     #         yside = 1
#     #     elif (yside < 0):
#     #         yside = -1
#     #         left -= c
#     #         right -= c
#     #         dy = y
#     # if (y < 0):
#     #     if yside == 0:
#     #         yside = -1
#     #     if yside > 0:
#     #         yside = -1
#     #         left -= c
#     #         right -= c
#     #         dy = y
#     if ((abs(dx) > 2) & (abs(dx) < 95)):
#         sign = x/dx
#         if (sign > 0):
#             sign = 1
#         elif (sign < 0):
#             sign = -1
#         pxc = sign * calibrator * (abs(dx) / 100)
#     if (abs(dy) > 2) & (abs(dy) < 95):
#         sign = y/dy
#         if (sign > 0):
#             sign = 1
#         elif sign < 0:
#             sign = -1
#         pyc = calibrator * (abs(dy) / 100)
#     if (abs(dx) > 2 or abs(dy) > 2):
#         if (abs(dx) < 2):
#             pxc = 0
#         if (abs(dy) < 2):
#             pyc = 0
#         left += const * (pyc * y + pxc * x)
#         right += const * (pyc * y - pxc * x)
#         if (left > 100 and right > 100):
#             left = 100
#             right = 100                            #  <-- for efficiency purposes
#         if (left < -100 and right < -100):
#             left = -100
#             right = -100
#         else:
#             if (left > 100):
#                 left = 100
#             if (right > 100):
#                 right = 100
#             if (left < -100):
#                 left = -100
#             if (right < -100):
#                 right = -100
        
#         if x == 0:
#             c = (left + right)/2
#             left = c
#             right = c
#         if y == 0:
#             c = (left + right)/2 #gives throttle
#             left -= c
#             right -= c


#     # BACKUP:
#     # left = const * (y + x)
#     # right = const * (y - x)
#     # if not (not (dx or dy)):
#     print("   " + str(left) + "(" + str(dx) + " - " + str(y + x) + ", " + str(x_pos) + ": " + str(x_pos == x) + "), " + str(right) + "(" + str(dy) + " - " + str(y - x) + ", " + str(y_pos) + ": " + str(y_pos == y) + ")")
#     l.set_velocity(-1 * left, PERCENT)
#     r.set_velocity(-1 * right, PERCENT)
#     l.spin(FORWARD)   #PLS UNCOMMENT THIS BACK ON ONCE DONE WITH TESTING (PREVENTS MOTORS FROM MOVING DURING TESTING)
#     r.spin(FORWARD)
#     wait(7.5, MSEC)
    

# def driver_control():
#     controller1.axis2.changed(joystick)
#     controller1.axis4.changed(joystick)
#     wings()
#     # intacata()
#     while True:
#         intacata()
#         #catapulty() #Shouldn't be here, but just backup
#         continue


# def autonomous():
#     t.set_velocity(100, PERCENT)
#     t.spin(FORWARD)

# competition = Competition(driver_control, autonomous)



# import vex;
# from vex import *;
# import random;

# brain = Brain()

# Left1 = Motor(Ports.PORT1, GearSetting.RATIO_6_1, False)
# Left2 = Motor(Ports.PORT2, GearSetting.RATIO_6_1, True)
# Left3 = Motor(Ports.PORT3, GearSetting.RATIO_6_1, False)
# Right1 = Motor(Ports.PORT8, GearSetting.RATIO_6_1, False)
# Right2 = Motor(Ports.PORT9, GearSetting.RATIO_6_1, True)
# Right3 = Motor(Ports.PORT10, GearSetting.RATIO_6_1, True)
# intake = Motor(Ports.PORT4, GearSetting.RATIO_36_1, False)
# catapult = Motor(Ports.PORT6, GearSetting.RATIO_36_1, False)
# biden = DigitalOut(brain.three_wire_port.a)
# trump = DigitalOut(brain.three_wire_port.b)
# controller1 = Controller(PRIMARY)


# l = MotorGroup(Left1, Left2, Left3)
# r = MotorGroup(Right1, Right2, Right3)
# t = MotorGroup(Left1, Left2, Left3, Right1, Right2, Right3)
# t.set_stopping(BRAKE)

# pressed1 = False
# pressed2 = False
# bidenpressed = False
# trumppressed = False

# # NEEDS TO BE REVERSED: LEFT 2, RIGHT 1

# x_pos = 0
# y_pos = 0
# dx = 0
# dy = 0
# const = 1
# pxc = 1
# pyc = 1
# left = 0
# right = 0
# yside = 0
# xside = 0



# def left():
#     global bidenpressed
#     if bidenpressed:
#         biden.set(False)
#         return
#     biden.set(True)
# def right():
#     global trumppressed
#     if trumppressed:
#         trump.set(False)
#         return
#     trump.set(True)
# def stopleft():
#     global bidenpressed
#     if bidenpressed:
#         bidenpressed = False
#         return
#     bidenpressed = True
# def stopright():
#     global trumppressed
#     if trumppressed:
#         trumppressed = False
#         return
#     trumppressed = True

# def wings():
#     controller1.buttonLeft.pressed(left)
#     controller1.buttonLeft.released(stopleft)
#     controller1.buttonRight.pressed(right)
#     controller1.buttonRight.released(stopright)


# def spinfirst():                #CATAPULT
#     global pressed1
#     if pressed1:
#         stopspin()
#         # pressed1 = False
#         return
#     print("T1.2")
#     intake.set_velocity(18, PERCENT)
#     catapult.set_velocity(30, PERCENT)
#     intake.spin(FORWARD)
#     catapult.spin(REVERSE)
#     # wait(0.25, SECONDS)
# def spinsecond():              #INTAKE
#     global pressed2
#     print("T1.1")
#     if pressed2:
#         stopspin()
#         # pressed2 = False
#         return
#     intake.set_velocity(100, PERCENT)
#     intake.spin(REVERSE)
#     # catapult.spin(REVERSE)
#     # wait(0.25, SECONDS)
# def stopspin():
#     intake.set_velocity(0, PERCENT)
#     print("T3.2")
#     catapult.stop()
#     intake.stop()
#     # pressed1 = False
#     # pressed2 = False
# def pressedstop1():
#     global pressed1
#     if (pressed1):
#         pressed1 = False
#         return
#     pressed1 = True
# def pressedstop2():
#     global pressed2
#     if (pressed2):
#         pressed2 = False
#         return
#     pressed2 = True

# def intacata():
#     # if (not intake.is_spinning()):
#     #     # print("T1")
#     #     if controller1.buttonL1.pressing():
#     #         print("T1.2")
#     #         intake.set_velocity(100, PERCENT)
#     #         intake.spin(REVERSE)
#     #         # intake.spin(REVERSE)
#     #         catapult.spin(FORWARD)
#     #         wait(5, SECONDS)
#     #     if controller1.buttonL2.pressing():
#     #         print("T1.1")
#     #         intake.set_velocity(100, PERCENT)
#     #         intake.spin(FORWARD)
#     #         # catapult.spin(REVERSE)
#     #         wait(5, SECONDS)
#     # else:
#     #     print("T2")
#     #     if (controller1.buttonL2.pressing() or controller1.buttonL1.pressing()):
#     #         intake.set_velocity(0, PERCENT)
#     #         print("T2.1")
#     #         intake.stop()
#     #         catapult.stop()
#     #         wait(0.25, SECONDS)

#     controller1.buttonL1.pressed(spinsecond)
#     controller1.buttonL1.released(pressedstop2)
#     controller1.buttonL2.pressed(spinfirst)
#     controller1.buttonL2.released(pressedstop1)
#     controller1.buttonR2.pressed(stopspin)

#     # BACKUP CODE
#     # intake.set_velocity(100, PERCENT)
#     # controller1.buttonL1.pressed(intake.spin, tuple([REVERSE]))
#     # controller1.buttonL2.pressed(intake.spin, tuple([FORWARD]))
#     # controller1.buttonX.pressed(intake.stop)

# def catapulty():
#     if controller1.buttonR1.pressing():
#         print("T3.1")
#         intake.set_velocity(60, PERCENT)
#         catapult.spin(REVERSE)
#         intake.spin(FORWARD)
#     if controller1.buttonR2.pressing():
#         intake.set_velocity(0, PERCENT)
#         print("T3.2")
#         catapult.stop()
#         intake.stop()

# def joystick():
#     global x_pos
#     global y_pos
#     global pxc
#     global pyc
#     global left
#     global right
#     global yside
#     global xside
#     y = controller1.axis2.position()
#     x = controller1.axis4.position()
#     dx = x - x_pos
#     dy = y - y_pos
#     # if dy | dx:
#     #     print(x, dx, x_pos, y, dy, y_pos)
#     x_pos = x
#     y_pos = y
#     calibrator = 50 * 0.0275 #the first number is a number between 1 and 100, the core calibrator. the second number is the compensation for the quick time of iteration in the while loop
    
#     if not x and not y:
#         l.stop()
#         r.stop()
#         left = 0
#         right = 0
#     dx *= 1 #compensation for the quick iteration of the while loop
#     dy *= 1 #compensation for the quick iteration of the while loop
#     sign = 1
#     c = (left + right)/2
#     # if (x > 0):                      #this is for reseting the pointer mechanism after the joystick has passed the center
#     #     if xside == 0:
#     #         yside = 1
#     #     if xside < 0:
#     #         xside = 1
#     #         left = c
#     #         right = c
#     #         dx = x
#     # if (x < 0):
#     #     if xside == 0:
#     #         xside = -1
#     #     if xside > 0:
#     #         xside = -1
#     #         left = c
#     #         right = c
#     #         dx = x
#     # if (y > 0):
#     #     if (yside == 0):
#     #         yside = 1
#     #     elif (yside < 0):
#     #         yside = -1
#     #         left -= c
#     #         right -= c
#     #         dy = y
#     # if (y < 0):
#     #     if yside == 0:
#     #         yside = -1
#     #     if yside > 0:
#     #         yside = -1
#     #         left -= c
#     #         right -= c
#     #         dy = y
#     if ((abs(dx) > 2) & (abs(dx) < 95)):
#         sign = x/dx
#         if (sign > 0):
#             sign = 1
#         elif (sign < 0):
#             sign = -1
#         pxc = sign * calibrator * (abs(dx) / 100)
#     if (abs(dy) > 2) & (abs(dy) < 95):
#         sign = y/dy
#         if (sign > 0):
#             sign = 1
#         elif sign < 0:
#             sign = -1
#         pyc = calibrator * (abs(dy) / 100)
#     if (abs(dx) > 2 or abs(dy) > 2):
#         if (abs(dx) < 2):
#             pxc = 0
#         if (abs(dy) < 2):
#             pyc = 0
#         left += const * (pyc * y + pxc * x)
#         right += const * (pyc * y - pxc * x)
#         if (left > 100 and right > 100):
#             left = 100
#             right = 100                            #  <-- for efficiency purposes
#         if (left < -100 and right < -100):
#             left = -100
#             right = -100
#         else:
#             if (left > 100):
#                 left = 100
#             if (right > 100):
#                 right = 100
#             if (left < -100):
#                 left = -100
#             if (right < -100):
#                 right = -100
        
#         if x == 0:
#             c = (left + right)/2
#             left = c
#             right = c
#         if y == 0:
#             c = (left + right)/2 #gives throttle
#             left -= c
#             right -= c


#     # BACKUP:
#     # left = const * (y + x)
#     # right = const * (y - x)
#     # if not (not (dx or dy)):
#     print("   " + str(left) + "(" + str(dx) + " - " + str(y + x) + ", " + str(x_pos) + ": " + str(x_pos == x) + "), " + str(right) + "(" + str(dy) + " - " + str(y - x) + ", " + str(y_pos) + ": " + str(y_pos == y) + ")")
#     l.set_velocity(-1 * left, PERCENT)
#     r.set_velocity(-1 * right, PERCENT)
#     l.spin(FORWARD)   #PLS UNCOMMENT THIS BACK ON ONCE DONE WITH TESTING (PREVENTS MOTORS FROM MOVING DURING TESTING)
#     r.spin(FORWARD)
#     wait(7.5, MSEC)
    

# def driver_control():
#     controller1.axis2.changed(joystick)
#     controller1.axis4.changed(joystick)
#     wings()
#     # intacata()
#     while True:
#         intacata()
#         #catapulty() #Shouldn't be here, but just backup
#         continue


# def autonomous():
#     pass

# competition = Competition(driver_control, autonomous)




import vex;
from vex import *;
import random;

brain = Brain()

Left1 = Motor(Ports.PORT11, GearSetting.RATIO_6_1, False)
Left2 = Motor(Ports.PORT13, GearSetting.RATIO_6_1, True)
Left3 = Motor(Ports.PORT12, GearSetting.RATIO_6_1, False)
Right1 = Motor(Ports.PORT18, GearSetting.RATIO_6_1, False)
Right2 = Motor(Ports.PORT20, GearSetting.RATIO_6_1, True)
Right3 = Motor(Ports.PORT19, GearSetting.RATIO_6_1, True)
intake = Motor(Ports.PORT10, GearSetting.RATIO_36_1, False)
catapult = Motor(Ports.PORT1, GearSetting.RATIO_36_1, False)
biden = DigitalOut(brain.three_wire_port.a)
trump = DigitalOut(brain.three_wire_port.b)
controller1 = Controller(PRIMARY)


l = MotorGroup(Left1, Left2, Left3)
r = MotorGroup(Right1, Right2, Right3)
t = MotorGroup(Left1, Left2, Left3, Right1, Right2, Right3)
t.set_stopping(BRAKE)

pressed1 = False
pressed2 = False
bidenpressed = False
trumppressed = False

# NEEDS TO BE REVERSED: LEFT 2, RIGHT 1

x_pos = 0
y_pos = 0
dx = 0
dy = 0
const = 1
pxc = 1
pyc = 1
left1 = 0
right1 = 0
yside = 0
xside = 0
sign = 0



def left():
    global bidenpressed
    if bidenpressed:
        biden.set(False)
        return
    biden.set(True)
def right():
    global trumppressed
    if trumppressed:
        trump.set(False)
        return
    trump.set(True)
def stopleft():
    global bidenpressed
    if bidenpressed:
        bidenpressed = False
        return
    bidenpressed = True
def stopright():
    global trumppressed
    if trumppressed:
        trumppressed = False
        return
    trumppressed = True

def wings():
    controller1.buttonLeft.pressed(left)
    controller1.buttonLeft.released(stopleft)
    controller1.buttonRight.pressed(right)
    controller1.buttonRight.released(stopright)


def spinfirst():                #INTAKE
    global pressed1
    if pressed1:
        stopspin()
        # pressed1 = False
        return
    print("T1.2")
    intake.set_velocity(30, PERCENT)
    catapult.set_velocity(80, PERCENT)
    intake.spin(FORWARD)
    catapult.spin(REVERSE)
    # wait(0.25, SECONDS)
def spinsecond():              #CATAPULT
    global pressed2
    print("T1.1")
    if pressed2:
        stopspin()
        # pressed2 = False
        return
    catapult.stop()
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
        intake.set_velocity(100, PERCENT)
        intake.spin(FORWARD)
    if controller1.buttonR2.pressing():
        intake.set_velocity(20, PERCENT)
        catapult.set_velocity(20, PERCENT)
        intake.spin(REVERSE)
        intake.spin(FORWARD)
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
    global yside
    global xside
    y = controller1.axis2.position()
    x = controller1.axis4.position()
    dx = x - x_pos
    dy = y - y_pos
    if dy | dx:
        print(x, y)
        print(dx, x_pos, dy, y_pos)
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
    c = (left + right)/2
    # if (x > 0):                      #this is for reseting the pointer mechanism after the joystick has passed the center
    #     if xside == 0:
    #         yside = 1
    #     if xside < 0:
    #         xside = 1
    #         left = c
    #         right = c
    #         dx = x
    # if (x < 0):
    #     if xside == 0:
    #         xside = -1
    #     if xside > 0:
    #         xside = -1
    #         left = c
    #         right = c
    #         dx = x
    # if (y > 0):
    #     if (yside == 0):
    #         yside = 1
    #     elif (yside < 0):
    #         yside = -1
    #         left -= c
    #         right -= c
    #         dy = y
    # if (y < 0):
    #     if yside == 0:
    #         yside = -1
    #     if yside > 0:
    #         yside = -1
    #         left -= c
    #         right -= c
    #         dy = y
    if ((abs(dx) > 2) & (abs(dx) < 95)):
        te = sign
        if (x > 0):
            sign = 1
        elif (x < 0):
            sign = -1
        pxc = calibrator * (abs(dx) / 100)
        # if te != sign:
        #     pxc = 1
    if (abs(dy) > 2) & (abs(dy) < 95):
        te = sign
        if (y > 0):
            sign = 1
        elif y < 0:
            sign = -1
        pyc = calibrator * (abs(dy) / 100)
        # if te != sign:
        #     pyc = 1
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
    # left1 = const * (y + x)
    # right1 = const * (y - x)
    if not (not (dx or dy)):
        print("   " + str(left) + "(" + str(dx) + " - " + str(y + x) + ", " + str(x_pos) + ": " + str(x_pos == x) + "), " + str(right) + "(" + str(dy) + " - " + str(y - x) + ", " + str(y_pos) + ": " + str(y_pos == y) + ")")
    # -----------------
    l.set_velocity(-1 * left, PERCENT)
    r.set_velocity(-1 * right, PERCENT)
    l.spin(FORWARD)   #PLS UNCOMMENT THIS BACK ON ONCE DONE WITH TESTING (PREVENTS MOTORS FROM MOVING DURING TESTING)
    r.spin(FORWARD)
    wait(7.5, MSEC)
    print()
    

def driver_control():
    controller1.axis2.changed(joystick)
    controller1.axis4.changed(joystick)
    wings()
    # intacata()
    while True:
        intacata()
        #catapulty() #Shouldn't be here, but just backup
        continue


def autonomous():
    t.set_velocity(100, PERCENT)
    t.spin(FORWARD)
    wait(3, SECONDS)
    t.set_velocity(0, PERCENT)

competition = Competition(driver_control, autonomous)