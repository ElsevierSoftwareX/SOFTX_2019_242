from Scripts.Behavior.ComposedBehavior.ComposedBehavior import ComposedBehavior
from Scripts.Behavior.SimpleBehavior.BlinkBehavior.BlinkBehaviorEaseInOut import BlinkBehaviorEaseInOut
from Libs.Constants import *
from colour import Color
import time


class AffectiveBehavior2(ComposedBehavior):
    def __init__(self, bodyRef):
        # standard behaviors
        ComposedBehavior.__init__(self, bodyRef)

        # generic variables
        self.behaviorType = ComposedBehaviorType.AFFECTIVE_EXPRESSION_2
        self.behaviorList.append(BlinkBehaviorEaseInOut(bodyRef, [Color(rgb=(0.7, 0.0, 0.7)), Color(rgb=(1.0, 1.0, 0.0))], ColorBrightness.HIGH, 3, 12, Color(rgb=(0.0, 0.0, 0.0)), True))