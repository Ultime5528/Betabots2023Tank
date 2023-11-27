from utils.sparkmaxutils import configure_leader, configure_follower, rev
import wpilib
import wpilib.drive
import commands2


class Robot(wpilib.TimedRobot):
    def robotInit(self):
        self._motor_left = rev.CANSparkMax(3, rev.CANSparkMax.MotorType.kBrushless)
       

        self._motor_left_follower = rev.CANSparkMax(4,
                                                    rev.CANSparkMax.MotorType.kBrushless)


        self._motor_right = rev.CANSparkMax(1,
                                            rev.CANSparkMax.MotorType.kBrushless)

        self._motor_right_follower = rev.CANSparkMax(2,
                                                     rev.CANSparkMax.MotorType.kBrushless)

        self._drive = wpilib.drive.DifferentialDrive(self._motor_left, self._motor_right)
        wpilib.SmartDashboard.putData("Drive", self._drive)

        self.joystick = wpilib.Joystick(0)

    def teleopPeriodic(self) -> None:
        self._drive.arcadeDrive(-1 * self.joystick.getY(), -1 * self.joystick.getX())

    def simulationPeriodic(self):
        self._drive_sim.setInputs(
            self._motor_left.get() * RobotController.getInputVoltage(),
            self._motor_right.get() * RobotController.getInputVoltage())
        self._drive_sim.update(0.02)
        self._motor_left_sim.setPosition(
            self._drive_sim.getLeftPosition() / self.encoder_conversion_factor + self._left_encoder_offset)
        self._motor_left_sim.setVelocity(self._drive_sim.getLeftVelocity())
        self._motor_right_sim.setPosition(
            self._drive_sim.getRightPosition() / self.encoder_conversion_factor + self._right_encoder_offset)
        self._motor_right_sim.setVelocity(self._drive_sim.getRightVelocity())
        self._gyro.setSimAngle(self._drive_sim.getHeading().degrees())
        self.sim_vision.processFrame(self._drive_sim.getPose())


if __name__ == "__main__":
    wpilib.run(Robot)
