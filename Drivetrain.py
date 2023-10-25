from utils.sparkmaxutils import configure_leader, configure_follower, rev
import wpilib
import wpilib.drive


class Robot(wpilib.TimedRobot):
    def robotInit(self):
        self._motor_left = rev.CANSparkMax(3, rev.CANSparkMax.MotorType.kBrushless)
        configure_leader(self._motor_left, "brake")

        self._motor_left_follower = rev.CANSparkMax(4,
                                                    rev.CANSparkMax.MotorType.kBrushless)
        configure_follower(self._motor_left_follower, self._motor_left, "brake")

        self._motor_right = rev.CANSparkMax(1,
                                            rev.CANSparkMax.MotorType.kBrushless)
        configure_leader(self._motor_right, "brake")

        self._motor_right_follower = rev.CANSparkMax(2,
                                                     rev.CANSparkMax.MotorType.kBrushless)
        configure_follower(self._motor_right_follower, self._motor_right, "brake")

        self._drive = wpilib.drive.DifferentialDrive(self._motor_left, self._motor_right)
        wpilib.SmartDashboard.putData("Drive", self._drive)

        self.joystick = wpilib.Joystick(0)

    def teleopPeriodic(self) -> None:
        self._drive.arcadeDrive(-1 * self.joystick.getY(), -1 * self.joystick.getX())


if __name__ == "__main__":
    wpilib.run(Robot)
