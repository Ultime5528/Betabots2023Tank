from utils.safecommand import SafeCommand
from subsystems.inclinator import Inclinator
from utils.property import autoproperty
from wpilib import RobotBase

class MoveToLevelOne(SafeCommand):
    encoder_value = autoproperty(10)
    interval = autoproperty(1)
    def __init__(self, inclinator: Inclinator):
        super().__init__()
        self.inclinator = inclinator
        self.addRequirements(self.inclinator)

    def execute(self):
        if(self.encoder_value < self.inclinator.getEncoderPosition()):
            self.inclinator.moveDown()
        elif(self.encoder_value > self.inclinator.getEncoderPosition()):
            self.inclinator.moveUp()
        else:
            self.inclinator.stop()

        self.inclinator.updateEncoderPosition()

    def isFinished(self) -> bool:
        return self.isBetweenValues(self.encoder_value-self.interval, self.encoder_value+self.interval, self.inclinator.getEncoderPosition())

    def end(self, interrupted: bool):
        self.inclinator.stop()

    def isBetweenValues(self, minInterval, maxInterval, value):
        return value >= minInterval and value <= maxInterval