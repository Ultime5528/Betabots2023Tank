import wpilib
from wpilib import RobotBase
import wpilib.simulation
from utils.safesubsystem import SafeSubsystem
import rev
import ports
from utils.sparkmaxsim import SparkMaxSim


class Arm(SafeSubsystem):

    def __init__(self):
        super().__init__()

        self.motor = rev.CANSparkMax(ports.inclinator_motor, rev.CANSparkMax.MotorType.kBrushless)
        self.switch = wpilib.DigitalInput(ports.inclinator_limitswitch)
        self.encoder = self.motor.getEncoder()

        if RobotBase.isSimulation():
            self.sim_motor = SparkMaxSim(self.motor)

    def moveUp(self):
        self.motor.set(1)

    def moveDown(self):
        self.motor.set(-1)

    def stop(self):
        self.motor.stopMotor()

    def is_down(self):
        return self.switch.get()

    def get_position(self):
        return self.encoder.getPosition()

    def resetEncoderPosition(self):
        self.encoder.setPosition(0)

    def simulationPeriodic(self):
        self.sim_motor.setVelocity(self.motor.get())
        self.sim_motor.setPosition(self.sim_motor.getPosition() + self.motor.get())