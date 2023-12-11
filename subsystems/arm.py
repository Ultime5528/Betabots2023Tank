import rev
import wpilib
import wpilib.simulation
import wpiutil
from wpilib import RobotBase

import ports
from utils.property import autoproperty, defaultSetter
from utils.safesubsystem import SafeSubsystem
from utils.sparkmaxsim import SparkMaxSim
from utils.sparkmaxutils import configureLeader


class Arm(SafeSubsystem):
    speed_up = autoproperty(1.0)
    speed_down = autoproperty(-1.0)

    def __init__(self):
        super().__init__()

        self.motor = rev.CANSparkMax(ports.arm_motor, rev.CANSparkMax.MotorType.kBrushless)
        configureLeader(self.motor, "brake")
        self.switch = wpilib.DigitalInput(ports.arm_limitswitch)
        self.encoder = self.motor.getEncoder()

        if RobotBase.isSimulation():
            self.sim_motor = SparkMaxSim(self.motor)

    def moveUp(self):
        self.motor.set(self.speed_up)

    def moveDown(self):
        self.motor.set(self.speed_down)

    def stop(self):
        self.motor.stopMotor()

    def is_down(self):
        return not self.switch.get()

    def get_position(self):
        return self.encoder.getPosition()

    def resetEncoderPosition(self):
        self.encoder.setPosition(0)

    def simulationPeriodic(self):
        self.sim_motor.setVelocity(self.motor.get())
        self.sim_motor.setPosition(self.sim_motor.getPosition() + self.motor.get())

    def initSendable(self, builder: wpiutil.SendableBuilder) -> None:
        super().initSendable(builder)
        builder.addDoubleProperty("Position", self.get_position, defaultSetter)
