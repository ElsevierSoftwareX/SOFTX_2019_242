import sys
import time
import numpy

from colour import Color
import pytweening as tween

from Libs.Constants import *
from Scripts.Behavior.SimpleBehavior.MoveBehavior.MoveBehavior import MoveBehavior


class MoveBehaviorCircle(MoveBehavior):
    def __init__(self, bodyRef, movementSpeed, movementDirection, repetitions, duration):
        MoveBehavior.__init__(self, bodyRef, movementSpeed, movementDirection, repetitions, duration)
    
    def behaviorActions(self):
        MoveBehavior.behaviorActions(self)

        # create array of circle values
        numSamples = 24
        ix = numpy.arange(numSamples)
        radius = 20
        xSignal = numpy.cos(2 * numpy.pi / numSamples * ix) * radius 
        ySignal = numpy.sin(2 * numpy.pi / numSamples * ix) * radius

        past_signal_x = 0
        past_signal_y = 0

        #to do a path backwards we reverse the order of the path points
        if self.currentMovementDirection == MovementDirection.REVERSE:
            xSignal = self.reversePath(xSignal)

        self.followPath(numSamples, [xSignal[self.currentWaypointIndex] - past_signal_x, ySignal[self.currentWaypointIndex] - past_signal_y])

        if self.reachedNewWaypoint(numSamples):
            past_signal_x = xSignal[self.currentWaypointIndex - 1]
            past_signal_y = ySignal[self.currentWaypointIndex - 1]