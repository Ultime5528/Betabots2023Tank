from utils.safecommand import SafeCommand
from subsystems.arm import Arm
from utils.property import autoproperty

#this command aims for the middle flowers
class MoveArm(SafeCommand):
    threshold = autoproperty(0.1)

    def __init__(self, arm: Arm, setpoint: float):
        super().__init__()
        self.arm = arm
        self.setpoint = setpoint
        self.addRequirements(self.arm)

    def execute(self):
        if self.setpoint < self.arm.get_position():
            self.arm.moveDown()
        else:
            self.arm.moveUp()

    def isFinished(self) -> bool:
        return self.isBetweenValues(self.setpoint - self.threshold, self.setpoint + self.threshold,
                                    self.arm.get_position())

    def end(self, interrupted: bool):
        self.arm.stop()

    def isBetweenValues(self, minInterval, maxInterval, value):
        return value >= minInterval and value <= maxInterval