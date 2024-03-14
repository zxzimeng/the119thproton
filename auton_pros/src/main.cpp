#include "main.h"

#include <sys/_stdint.h>

#include <iomanip>
#include <iostream>
#include <string>

#include "ARMS/chassis.h"
#include "ARMS/config.h"
#include "ARMS/flags.h"
#include "pros/adi.hpp"
#include "pros/motors.h"
#include "pros/rtos.hpp"

void print_ascii_header() {
  std::cout
      << "   _    _          _  _  ___    _    _                     _   "
         "         \n"
      << " _| |_ | |_  ___  / |/ || . | _| |_ | |_   ___  _ _  ___ _| |_ "
         "___ ._ _ \n"
      << "  | |  | . |/ ._> | || |`_  /  | |  | . | | . \\| '_>/ . \\ | | "
         "/ . \\| ' | \n"
      << "  |_|  |_|_|\\___. |_||_| /_/   |_|  |_|_| |  _/|_|  \\___/ |_| "
         "\\___/|_|_| \n"
      << "                                          |_|                  "
         "          \n\n\n\n";

  std::cout << "            ___                   ___       \n"
            << "           (   )                 (   )      \n"
            << " ___  ___   | | .-.       .--.    | | .-.   \n"
            << "(   )(   )  | |/   \\     /    \\   | |/   \\  \n"
            << " | |  | |   |  .-. .    |  .-. ;  |  .-. .  \n"
            << " | |  | |   | |  | |    | |  | |  | |  | |  \n"
            << " | |  | |   | |  | |    | |  | |  | |  | |  \n"
            << " | |  | |   | |  | |    | |  | |  | |  | |  \n"
            << " | |  ; '   | |  | |    | '  | |  | |  | |  \n"
            << " ' `-'  /   | |  | |    '  `-' /  | |  | |  \n"
            << "  '.__.'   (___)(___)    `.__.'  (___)(___) \n"
            << "\n\n\n\n";
}
void print_table_header(const std::string& motorType) {
  std::cout << "| " << std::setw(19) << "Timestamp (ms)"
            << " | " << std::setw(15) << motorType + " Direction"
            << " | " << std::setw(11) << "Over Temp"
            << " | " << std::setw(14) << "Over Current"
            << " | " << std::setw(21) << "Actual Velocity (RPM)"
            << " | " << std::setw(19) << "Current Draw (mA)"
            << " | " << std::setw(11) << "Power (W)"
            << " | " << std::setw(11) << "Torque (Nm)"
            << " | " << std::setw(9) << "Efficiency (%)"
            << " | " << std::setw(10) << "Pos (Deg)"
            << " | " << std::setw(15) << "Temperature (°C)"
            << " | " << std::setw(12) << "Voltage (mV)"
            << " |" << std::endl;
  std::cout << std::string(211, '-') << std::endl;
}

void print_table_row(int direction, int over_temp, int over_current,
                     double actual_velocity, double current_draw, double power,
                     double torque, double efficiency, double position,
                     double temperature, double voltage, uint32_t timestamp) {
  std::string direction_str = (direction == 1)   ? "Positive"
                              : (direction == 0) ? "None"
                                                 : "Reverse";
  std::string over_temp_str = (over_temp == 1)   ? "Yes"
                              : (over_temp == 0) ? "None"
                                                 : "No";
  std::string over_current_str = (over_current == 1)   ? "Yes"
                                 : (over_current == 0) ? "None"
                                                       : "No";

  std::cout << "| " << std::setw(20) << timestamp << "| " << std::setw(16)
            << std::left << direction_str << "| " << std::setw(12)
            << over_temp_str << "| " << std::setw(15) << over_current_str
            << "| " << std::setw(22) << actual_velocity << "| " << std::setw(20)
            << current_draw << "| " << std::setw(12) << power << "| "
            << std::setw(12) << torque << "| " << std::setw(15) << efficiency
            << "| " << std::setw(11) << position << "| " << std::setw(16)
            << temperature << " | " << std::setw(12) << voltage << " | "
            << std::endl;
  std::cout << std::string(210, '-') << std::endl;  // Separator line
}

void print_motor_data(const pros::Motor& motor_object,
                      const std::string& motor_name) {
  int dir_generic = motor_object.get_direction();
  int ovr_t_generic = motor_object.is_over_temp();
  int ovr_c_generic = motor_object.is_over_current();
  double v_generic = motor_object.get_actual_velocity();
  double mA_generic = motor_object.get_current_draw();
  double W_generic = motor_object.get_power();
  double Nm_generic = motor_object.get_torque();
  double E_generic = motor_object.get_efficiency();
  double pos_generic = motor_object.get_position();
  double C_generic = motor_object.get_temperature();
  double voltage = motor_object.get_voltage();
  uint32_t timestamp = pros::millis();  // Get the timestamp in milliseconds

  print_table_header(motor_name);
  print_table_row(dir_generic, ovr_t_generic, ovr_c_generic, v_generic,
                  mA_generic, W_generic, Nm_generic, E_generic, pos_generic,
                  C_generic, voltage, timestamp);
}
/**
 * Runs initialization code. This occurs as soon as the program is started.
 *
 * All other competition modes are blocked by initialize; it is recommended
 * to keep execution time for this mode under a few seconds.
 */
void initialize() {
  arms::init();
  pros::lcd::initialize();
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
void autonomous() {}

/**
 * Runs the operator control code. This function will be started in its own task
 * with the default priority and stack size whenever the robot is enabled via
 * the Field Management System or the VEX Competition Switch in the operator
 * control mode.
 *
 * If no competition control is connected, this function will run immediately
 * following initialize().
 *
 * If the robot is disabled or communications is lost, the
 * operator control task will be stopped. Re-enabling the robot will restart the
 * task, not resume it from where it left off.
 */

void opcontrol() {
  // print_ascii_header();
  // const bool CATA_MOTOR_VERBOSE = 1;
  // const bool DRIVECHAIN_VERBOSE = 0;

  // // intake motor on port 4, not reversed
  // pros::Motor m_intake(10, pros::E_MOTOR_GEARSET_36, false,
  //                      pros::E_MOTOR_ENCODER_DEGREES);
  // // cata motor on port 4, reversed
  // pros::Motor m_cata(1, pros::E_MOTOR_GEARSET_36, true,
  //                    pros::E_MOTOR_ENCODER_DEGREES);

  // // left wing on port A
  // pros::ADIDigitalOut w_left('a', false);
  // // right wing on port B
  // pros::ADIDigitalOut w_right('b', false);

  // // target rpm for catapult
  // double rpm_target_cata = 30.0;

  // // voltage for main cata motor
  // double volt_cata = rpm_target_cata / 100.0 * 127.0;
  // double volt_intake = volt_cata;

  // std::cout << volt_intake;
  // spin both motors at their calculated voltage
  // m_intake.move(volt_intake);
  // m_cata.move(volt_cata);

  // while (true) {
  //   if (CATA_MOTOR_VERBOSE) {
  //     print_motor_data(m_cata, "Cata");
  //     print_motor_data(m_intake, "Inta");
  //   }
  //   pros::delay(3000);

  //   //     pros::delay(100);
  // }

  // arms::odom::reset({0, 0}, 0);
  // arms::chassis::turn(90, arms::ASYNC);
  // pros::delay(3000);

  arms::odom::reset({0, 0}, 0);
  arms::chassis::move(90);
  pros::delay(5000);

  // while (true) {
  //   // insert other opcontrol code here
  //   pros::lcd::set_text(0, "X: " +
  //   std::to_string(arms::odom::getPosition().x)); pros::lcd::set_text(1, "Y:
  //   " + std::to_string(arms::odom::getPosition().y)); pros::lcd::set_text(2,
  //   "H: " + std::to_string(arms::odom::getHeading())); pros::lcd::set_text(
  //       3, "Left: " + std::to_string(arms::odom::getLeftEncoder()));
  //   pros::lcd::set_text(
  //       4, "Right: " + std::to_string(arms::odom::getRightEncoder()));
  //   pros::lcd::set_text(
  //       5, "Middle: " + std::to_string(arms::odom::getMiddleEncoder()));
  //   pros::delay(10);
  // }
  // reset odom settings
  // arms::odom::reset({0, 0}, -90);
  // if (master.get_digital_new_press(DIGITAL_A)) {
  // arms::odom::reset({0, 0}, 0);
  // arms::chassis::move(24, arms::ASYNC);
  // pros::delay(5000);
  // }

  // move to matchload position
  // arms::chassis::move({16, 23, 0}, arms::RELATIVE | arms::REVERSE);

  // // deploy wings
  // w_right.set_value(1);

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

  // // retract wing
  // w_right.set_value(0);

  // // turn left 10° so that we can clear the black bar, relative
  // arms::chassis::move({0, 0, 30}, arms::RELATIVE);

  // // move forward and clear the short barriers
  // arms::chassis::move(20);

  // // turn to paralell the middle bar
  // arms::chassis::turn(90);

  // // drive over the middle bar, no pid
  // arms::chassis::move({60, 0}, arms::RELATIVE | arms::THRU);

  // //   // straighten after crossing
  // arms::chassis::turn(90);

  // //   // turn 180 to get ready to deploy wings
  // arms::chassis::turn(180, arms::RELATIVE);

  // // deploy wings
  // w_left.set_value(1);
  // w_right.set_value(1);
}