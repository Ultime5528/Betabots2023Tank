from typing import Callable

from utils.safecommand import SafeCommand
from subsystems.arm import Arm
from utils.property import autoproperty, asCallable


class MoveArm(SafeCommand):
    threshold = autoproperty(0.1)

    @classmethod
    def toLevel1(cls, arm: Arm):
        cmd = cls(arm, lambda: properties.level1_setpoint)
        cmd.setName(cmd.getName() + ".toLevel1")
        return cmd

    @classmethod
    def toLevel2(cls, arm: Arm):
        cmd = cls(arm, lambda: properties.level2_setpoint)
        cmd.setName(cmd.getName() + ".toLevel2")
        return cmd

    def __init__(self, arm: Arm, setpoint: Callable[[], float]):
        super().__init__()
        self.arm = arm
        self.setpoint = asCallable(setpoint)
        self.addRequirements(self.arm)

    def execute(self):
        if self.setpoint() < self.arm.get_position():
            self.arm.moveDown()
        else:
            self.arm.moveUp()

    def isFinished(self) -> bool:
        return self.isBetweenValues(self.setpoint() - self.threshold, self.setpoint() + self.threshold,
                                    self.arm.get_position())

    def end(self, interrupted: bool):
        self.arm.stop()

    def isBetweenValues(self, minInterval, maxInterval, value):
        return value >= minInterval and value <= maxInterval


class _ClassProperties:
    # Elevator Properties #
    level1_setpoint = autoproperty(-20.0, subtable=MoveArm.__name__)
    level2_setpoint = autoproperty(-10.0, subtable=MoveArm.__name__)


properties = _ClassProperties()
