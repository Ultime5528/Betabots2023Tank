from typing import Literal

import commands2

from commands.extend import ExtendStrong, ExtendWeak
from subsystems.launcher import Launcher
from commands.retract import Retract


class Launch(commands2.SequentialCommandGroup):
    def __init__(self, launcher: Launcher, strength: Literal["strong", "weak"]):
        assert strength in ("strong", "weak")
        if strength == "strong":
            super().__init__(
                ExtendStrong(launcher),
                commands2.WaitCommand(0.1),
                Retract(launcher)
            )
        else:
            super().__init__(
                ExtendWeak(launcher),
                commands2.WaitCommand(0.1),
                Retract(launcher)
            )


