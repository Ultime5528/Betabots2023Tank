import wpilib
from wpilib import RobotBase
import wpilib.simulation
from utils.safesubsystem import SafeSubsystem
import rev
import ports
from utils.sparkmaxsim import SparkMaxSim
from utils.sparkmaxutils import configureLeader
from utils.property import autoproperty


class Arm(SafeSubsystem):
    speed_up = autoproperty(1)
    speed_down = autoproperty(-1)

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

    def is_at_limit_switch(self):
        return self.switch.get()

    def get_position(self):
        return self.encoder.getPosition()

    def resetEncoderPosition(self):
        self.encoder.setPosition(0)

    def simulationPeriodic(self):
        self.sim_motor.setVelocity(self.motor.get())
        self.sim_motor.setPosition(self.sim_motor.getPosition() + self.motor.get())


