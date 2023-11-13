from utils.safesubsystem import SafeSubsystem
import rev
import ports


class Inclinator(SafeSubsystem):

    def __init__(self):
        super().__init__()
        self.motor_inclinator = rev.CANSparkMax(ports.moteur_inclinator, rev.CANSparkMax.MotorType.kBrushless)

    def up(self):
        self.motor_inclinator.set(1)

    def down(self):
        self.motor_inclinator.set(-1)

    def stop(self):
        self.motor_inclinator.stopMotor()
