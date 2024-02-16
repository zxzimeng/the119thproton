import vex;
from vex import *;

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
inertial = Inertial(Ports.PORT17)


l = vex.MotorGroup(Left1, Left2, Left3)
r = vex.MotorGroup(Right1, Right2, Right3)
t = vex.MotorGroup(Left1, Left2, Left3, Right1, Right2, Right3)

distance_per_degree = 3.14159*4/360
wait(30, MSEC)

def drive(distance):
    global distance_per_degree
    global l
    global r
    #set velocity
    l.set_velocity(60, PERCENT)
    r.set_velocity(60, PERCENT)

    #calculate how much degress to spin wheel
    spin_rotation = distance/distance_per_degree

    #reset encoders

    l.spin_for(l_target_rotation, rotationUnits=RotationUnits.DEG)
    r.spin_for(r_target_rotation, rotationUnits=RotationUnits.DEG)

def spin_in_place(relative_heading):
    #reset encoders
    l.set_rotation(0)
    r.set_rotation(0)
    #set velocity
    v_l = 60
    v_r = -60
    l.set_velocity(60)
    r.set_velocity(60)
    #set brake type
    l.set_stopping(brake)
    r.set_stopping(brake)
    #reset heading
    inertial.reset_heading(0)
    inertial.reset_rotation(0)

    initial_heading = inertial.angle()
    target_heading = initial_heading+relative_heading

    if relative_heading < 0:
        v_l*=-1
        v_r*=-1
    
    while inertial.yaw() < target_heading:
        l.spin()
        r.spin()
    
    l.stop()
    r.stop()


def driver_control():
    drive(5)

def pre_autonomous():
    inertial.start_calibrating()


def autonomous():
    pass

competition = Competition(driver_control, autonomous)