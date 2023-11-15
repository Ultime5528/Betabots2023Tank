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
