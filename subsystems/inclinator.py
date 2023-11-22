import wpilib
from wpilib import RobotBase
import wpilib.simulation
from utils.safesubsystem import SafeSubsystem
import rev
import ports
from utils.sparkmaxsim import SparkMaxSim


class Inclinator(SafeSubsystem):

    def __init__(self):
        super().__init__()

        self.motor = rev.CANSparkMax(ports.inclinator_motor, rev.CANSparkMax.MotorType.kBrushless)
        self.switch = wpilib.DigitalInput(ports.inclinator_limitswitch)
        self.encoder = self.motor.getEncoder()

        if RobotBase.isSimulation():
            self.sim_motor = SparkMaxSim(self.motor)

    def moveUp(self):
        self.motor.set(1)

        if RobotBase.isSimulation():
            self.sim_motor.setVelocity(1)

    def moveDown(self):
        self.motor.set(-1)

        if RobotBase.isSimulation():
            self.sim_motor.setVelocity(-1)

    def stop(self):
        self.motor.stopMotor()

        if RobotBase.isSimulation():
            self.sim_motor.setVelocity(0)

    def getLimitswitchValue(self):
        return self.switch.get()

    def getEncoderPosition(self):
        if RobotBase.isSimulation():
            return self.encoder.getPosition()
        else:
            return self.encoder.getPosition()

    def updateEncoderPosition(self):
        if RobotBase.isSimulation():
            self.encoder.setPosition(self.encoder.getPosition() + self.encoder.getVelocity())

    def resetEncoderPosition(self):
        self.encoder.setPosition(0)
