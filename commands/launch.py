import commands2

from commands.extendlauncher import ExtendLauncher
from subsystems.launcher import Launcher
from commands.retractlauncher import RetractLauncher


class Launch(commands2.SequentialCommandGroup):
    def __init__(self, launcher: Launcher):
        super().__init__(
            ExtendLauncher(launcher),
            commands2.WaitCommand(0.1),
            RetractLauncher(launcher)
        )

