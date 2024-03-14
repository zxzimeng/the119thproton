#include "main.h"

#include "ARMS/config.h"

/**
 * A callback function for LLEMU's center button.
 *
 * When this callback is fired, it will toggle line 2 of the LCD text between
 * "I was pressed!" and nothing.
 */

/**
 * Runs initialization code. This occurs as soon as the program is started.
 *
 * All other competition modes are blocked by initialize; it is recommended
 * to keep execution time for this mode under a few seconds.
 */
void initialize() {
  pros::lcd::initialize();
  arms::init();
}

/**
 * Runs while the robot is in the disabled state of Field Management System or
 * the VEX Competition Switch, following either autonomous or opcontrol. When
 * the robot is enabled, this task will exit.
 */
void disabled() {}

/**
 * Runs after initialize(), and before autonomous when connected to the Field
 * Management System or the VEX Competition Switch. This is intended for
 * competition-specific initialization routines, such as an autonomous selector
 * on the LCD.
 *
 * This task will exit when the robot is enabled and autonomous or opcontrol
 * starts.
 */
void competition_initialize() {}

/**
 * Runs the user autonomous code. This function will be started in its own task
 * with the default priority and stack size whenever the robot is enabled via
 * the Field Management System or the VEX Competition Switch in the autonomous
 * mode. Alternatively, this function may be called in initialize or opcontrol
 * for non-competition testing purposes.
 *
 * If the robot is disabled or communications is lost, the autonomous task
 * will be stopped. Re-enabling the robot will restart the task, not re-start it
 * from where it left off.
 */
void autonomous() {
  arms::odom::reset({0, 0}, 0);
  arms::chassis::move(24, arms::ASYNC);
  pros::delay(5000);  // intake motor on port 4, not reversed
  // pros::Motor m_intake(10, pros::E_MOTOR_GEARSET_36, false,
  //                      pros::E_MOTOR_ENCODER_DEGREES);
  // // cata motor on port 4, reversed
  // pros::Motor m_cata(1, pros::E_MOTOR_GEARSET_36, true,
  //                    pros::E_MOTOR_ENCODER_DEGREES);

  // // left wing on port A
  // pros::ADIDigitalOut w_left('a', false);
  // // right wing on port B
  // pros::ADIDigitalOut w_right('b', false);

  // arms::odom::reset({0, 0}, 0);
  // arms::chassis::move({-15, -19}, arms::REVERSE);
  // arms::chassis::turn(110);

  // w_right.set_value(1);

  // // target rpm for catapult
  // double rpm_target_cata = 70.0;

  // // voltage for main cata motor
  // double volt_cata = rpm_target_cata / 100.0 * 127.0;
  // double volt_intake = volt_cata;

  // int32_t now = pros::millis();
  // int8_t wait_time = 30;  // catapulting time in seconds
  // int32_t target = now + wait_time * 1000;

  // m_intake.move(volt_intake);
  // m_cata.move(volt_cata);

  // while (pros::millis() < target) {
  //   continue;
  // }

  // m_cata.move(0);
  // m_intake.move(0);

  // w_right.set_value(0);

  // arms::chassis::move(30, arms::RELATIVE | arms::THRU);

  // arms::chassis::turn(90);
  // arms::chassis::move(62, arms::RELATIVE | arms::THRU);

  // arms::chassis::move(-10, arms::RELATIVE | arms::THRU | arms::REVERSE);

  // arms::chassis::move(-10, arms::RELATIVE | arms::THRU | arms::REVERSE);
  // arms::chassis::turn(-130, arms::RELATIVE);

  // w_right.set_value(1);
  // w_left.set_value(1);

  // arms::chassis::move(-30, arms::RELATIVE | arms::THRU | arms::REVERSE);
  // arms::chassis::move(10, arms::RELATIVE | arms::THRU);
  // arms::chassis::move(-30, arms::RELATIVE | arms::THRU | arms::REVERSE);
}
/**
 * Runs the operator control code. This function will be started in its own
 * task with the default priority and stack size whenever the robot is enabled
 * via the Field Management System or the VEX Competition Switch in the
 * operator control mode.
 *
 * If no competition control is connected, this function will run immediately
 * following initialize().
 *
 * If the robot is disabled or communications is lost, the
 * operator control task will be stopped. Re-enabling the robot will restart
 * the task, not resume it from where it left off.
 */
void opcontrol() {
  while (true) {
    // insert other opcontrol code here
    pros::lcd::set_text(0, "X: " + std::to_string(arms::odom::getPosition().x));
    pros::lcd::set_text(1, "Y: " + std::to_string(arms::odom::getPosition().y));
    pros::lcd::set_text(2, "H: " + std::to_string(arms::odom::getHeading()));
    pros::lcd::set_text(
        3, "Left: " + std::to_string(arms::odom::getLeftEncoder()));
    pros::lcd::set_text(
        4, "Right: " + std::to_string(arms::odom::getRightEncoder()));
    pros::lcd::set_text(
        5, "Middle: " + std::to_string(arms::odom::getMiddleEncoder()));
    pros::delay(10);
  }
}
