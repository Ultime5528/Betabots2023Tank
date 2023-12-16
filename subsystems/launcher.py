import wpilib
from utils.safesubsystem import SafeSubsystem
import ports


class Launcher(SafeSubsystem):
    def __init__(self):
        super().__init__()
        self.piston_strong = wpilib.DoubleSolenoid(
            wpilib.PneumaticsModuleType.CTREPCM,
            ports.launcher_piston_strong_forward,
            ports.launcher_piston_strong_backwards
        )
        self.addChild("piston_strong", self.piston_strong)

    def extend_strong(self):
        self.piston_strong.set(wpilib.DoubleSolenoid.Value.kForward)

    def retract(self):
        self.piston_strong.set(wpilib.DoubleSolenoid.Value.kReverse)

    def stop(self):
        self.piston_strong.set(wpilib.DoubleSolenoid.Value.kOff)
