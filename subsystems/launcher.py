import wpilib
from utils.safesubsystem import SafeSubsystem
import ports


class Launcher(SafeSubsystem):
    def __init__(self):
        super().__init__()
        self.piston = wpilib.DoubleSolenoid(
            wpilib.PneumaticsModuleType.CTREPCM,
            ports.launcher_piston_forward,
            ports.launcher_piston_backwards
        )
        self.addChild("piston", self.piston)

    def up_position(self):
        self.piston.set(wpilib.DoubleSolenoid.Value.kForward)

    def down_position(self):
        self.piston.set(wpilib.DoubleSolenoid.Value.kReverse)

    def stop(self):
        self.piston.set(wpilib.DoubleSolenoid.Value.kOff)
