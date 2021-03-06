import sys
import time
import numpy

from colour import Color
import pytweening as tween

from Core.Enumerations import *
from Core.Behavior.SimpleBehavior.MoveBehavior.MoveBehavior import MoveBehavior


class MoveBehaviorForwardAndBack(MoveBehavior, object):
    def __init__(self, controlRef, movementSpeed, movementDirection, repetitions, duration):
        super(MoveBehaviorForwardAndBack, self).__init__(controlRef, movementSpeed, movementDirection, repetitions, duration)
        self.waypoints = numpy.array([[1, 0], [-1, 0]])
    
    def behaviorActions(self):
        super(MoveBehaviorForwardAndBack, self).behaviorActions()
        #To do a path backwards we invert the points and their order
        if self.currentMovementDirection == MovementDirection.REVERSE:
            self.waypoints = self.reversePath(self.waypoints)
            
        self.followPath(len(self.waypoints), self.waypoints[self.currentWaypointIndex])