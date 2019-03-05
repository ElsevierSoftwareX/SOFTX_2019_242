import time
from colour import Color
from Libs.Constants import *
from Scripts.Behavior.SimpleBehavior import SimpleBehavior
from Scripts.Behavior.SimpleBehavior.BlinkBehavior.BlinkBehavior import BlinkBehavior
from Scripts.Behavior.SimpleBehavior.BlinkBehavior.BlinkBehaviorEaseIn import BlinkBehaviorEaseIn
from Scripts.Behavior.SimpleBehavior.BlinkBehavior.BlinkBehaviorEaseOut import BlinkBehaviorEaseOut

class BlinkBehaviorEaseInOut(BlinkBehavior, object):
    def __init__(self, bodyRef, blinkColor, brightness, repetitions, duration, defaultColor):
        super(BlinkBehaviorEaseInOut, self).__init__(bodyRef, blinkColor, brightness, repetitions, duration, defaultColor)
        self.subBehaviorDuration = duration/ 2.0
        self.easeInBehavior = BlinkBehaviorEaseIn(self.bodyRef, self.blinkColor, self.brightness, 1, self.subBehaviorDuration, self.defaultColor)
        self.easeOutBehavior = BlinkBehaviorEaseOut(self.bodyRef, self.blinkColor, self.brightness, 1, self.subBehaviorDuration, self.defaultColor)
        self.resetBehaviors()

    def behaviorActions(self):
        super(BlinkBehaviorEaseInOut, self).behaviorActions()
        currDuration = time.time() - self.startTime
        if currDuration <= self.subBehaviorDuration:
            self.easeInBehavior.behaviorActions()
            self.easeOutBehavior.resetBehavior()
        elif currDuration < self.duration:
            self.easeOutBehavior.behaviorActions()
        


    def finishBehavior(self):
        super(BlinkBehaviorEaseInOut, self).finishBehavior()
        self.resetBehaviors()

    def resetBehavior(self):
        super(BlinkBehaviorEaseInOut, self).resetBehavior()
        self.resetBehaviors()

    def resetBehaviors(self):
        self.easeInBehavior.resetBehavior()
        self.easeOutBehavior.resetBehavior()
        self.behaviorInSet = False
        self.behaviorOutSet = False
