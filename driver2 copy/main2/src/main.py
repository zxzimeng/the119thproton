#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default

# Robot configuration code
inertial = Inertial(Ports.PORT17)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration
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
catapult = Motor(Ports.PORT6, GearSetting.RATIO_36_1, False)
biden = DigitalOut(brain.three_wire_port.a)
trump = DigitalOut(brain.three_wire_port.b)
controller1 = Controller(PRIMARY)


motor_group_l = MotorGroup(Left1, Left2, Left3)
motor_group_r = MotorGroup(Right1, Right2, Right3)
motor_group_t = MotorGroup(Left1, Left2, Left3, Right1, Right2, Right3)

distance_per_degree = 3.14159*4/360
wait(30, MSEC)

def drive(distance):
    global distance_per_degree
    global motor_group_l
    global motor_group_r
    global motor_group_t

    #calculate how much degress to spin wheel
    spin_rotation = abs(distance/distance_per_degree)


    #reset encoders
    if distance>0:
        motor_group_t.set_velocity(30, PERCENT)
        motor_group_t.spin_for(REVERSE, spin_rotation, DEGREES)
    else:
        motor_group_t.set_velocity(30, PERCENT)
        motor_group_t.spin_for(FORWARD, spin_rotation, DEGREES)

    


def driver_control():
    pass
    




def pre_autonomous():
    inertial.calibrate()


def autonomous():
    drive(16)
    motor_group_l.set_velocity(30, PERCENT)
    motor_group_l.spin_for(REVERSE, 150, DEGREES, wait=False)
    motor_group_r.set_velocity(30, PERCENT)
    motor_group_r.spin_for(FORWARD, 150, DEGREES,wait=True)
    drive(-12)
    trump.set(True)

    start = brain.timer.time(SECONDS)
    finish = start+1*60
    catapult.set_max_torque(100, PERCENT)
    intake.set_max_torque(100, PERCENT)

    while brain.timer.time(SECONDS)<finish:
        catapult.set_velocity(70, PERCENT)
        intake.set_velocity(70*0.6, PERCENT)
        catapult.spin(REVERSE)
        intake.spin(FORWARD)
    
    intake.stop()
    catapult.stop()



competition = Competition(driver_control, autonomous)