from Scripts.Behavior.ComposedBehavior.ComposedBehavior import ComposedBehavior
from Scripts.Behavior.SimpleBehavior.BlinkBehavior.BlinkBehaviorEaseInOut import BlinkBehaviorEaseInOut
from colour import Color
from Libs.Constants import *
import time


class PunkIdleBehavior(ComposedBehavior):
    def __init__(self, bodyRef):
        # standard behaviors
        ComposedBehavior.__init__(self, bodyRef)

        # generic variables
        self.behaviorType = ComposedBehaviorType.PUNK_IDLE
        self.behaviorList.append(BlinkBehaviorEaseInOut(bodyRef, [bodyRef.getStimulusColor()], ColorBrightness.HIGH, 1, 2.0, Color(rgb=(0.0, 0.0, 0.0)), False))
