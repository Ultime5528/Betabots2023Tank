from wpilib import RobotController

import rev
import wpilib
import wpilib.drive
from utils.safesubsystem import SafeSubsystem
from utils.sparkmaxutils import configureLeader, configureFollower


class Drivetrain(SafeSubsystem):
    def __init__(self):
        super().__init__()

        self._motor_left = rev.CANSparkMax(4, rev.CANSparkMax.MotorType.kBrushless)
        configureLeader(self._motor_left, "brake")

        self._motor_left_follower = rev.CANSparkMax(3, rev.CANSparkMax.MotorType.kBrushless)
        configureFollower(self._motor_left_follower, self._motor_left, "brake")

        self._motor_right = rev.CANSparkMax(1, rev.CANSparkMax.MotorType.kBrushless)
        configureLeader(self._motor_right, "brake", True)

        self._motor_right_follower = rev.CANSparkMax(2, rev.CANSparkMax.MotorType.kBrushless)
        configureFollower(self._motor_right_follower, self._motor_right, "brake")

        self._drive = wpilib.drive.DifferentialDrive(self._motor_left, self._motor_right)
        self.addChild("DifferentialDrive", self._drive)
        wpilib.SmartDashboard.putData("Drive", self._drive)

    def drive(self, forward: float, turn: float) -> None:
        self._drive.arcadeDrive(forward, turn)
