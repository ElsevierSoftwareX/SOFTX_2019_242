import sys
import time

import numpy

from Libs.Constants import *
from Scripts.Behavior.SimpleBehavior.SimpleBehavior import SimpleBehavior


class MoveBehavior(SimpleBehavior):
    def __init__(self, bodyRef, movementSpeed, movementDirection, repetitions, duration, keepBehaviorSetting=False, startDelay = 0.0):
        SimpleBehavior.__init__(self, bodyRef, repetitions, duration, keepBehaviorSetting, startDelay)
        self.behaviorType = BehaviorType.MOVE  # Configuration.Behaviors

        self.waypoints = numpy.array([])

        self.movementSpeed = 0
        self.alreadyStartedSegment = False

        self.currentWaypointIndex = 0
        self.animationIntervalTime = duration

        self.movementType = ShapeType.NONE
        self.initialMovementDirection = movementDirection

        if self.initialMovementDirection == MovementDirection.ALTERNATING:
            self.currentMovementDirection = MovementDirection.FORWARD
        else:
            self.currentMovementDirection = self.initialMovementDirection
            

        self.movementSpeed = numpy.clip(movementSpeed, 0, 90)

        self.startTime = time.time()


    def behaviorActions(self):
        return

    # Body body
    def finishBehavior(self):
        SimpleBehavior.finishBehavior(self)
        self.bodyRef.resetWheelSetup()
        self.currentBehaviorRepetition = 0
        return

    def reversePath(self, path):
        print "----------------------"
        print path
        inversedPath = [-x for x in path]
        print inversedPath
        reversedPath = list(reversed(inversedPath))
        return reversedPath

    def followPath(self, pathLength, nextWaypoint):

        if not self.alreadyStartedSegment:
            self.alreadyStartedSegment = True
            self.bodyRef.setWheelMovement(nextWaypoint, self.movementSpeed)
            # print "Movement " + str(self.movementType) + " going to " + str(self.currentMovementWaypoint + 1) + " of " + str(pathLength) + " waypoints"
        
        if self.reachedNewWaypoint(pathLength):
            self.currentWaypointIndex += 1
            self.alreadyStartedSegment = False

        # account for last waypoint
        if self.checkForBehaviorEnd(pathLength): 
            if self.maxBehaviorRepetitions!=0:
                if self.currentBehaviorRepetition == self.maxBehaviorRepetitions:
                    self.finishBehavior()
                    return
                    print("Behavior ended")

                if self.currentBehaviorRepetition > self.maxBehaviorRepetitions:
                    return

                self.currentBehaviorRepetition += 1

            # if this movement is alternating then change it after each repetition
            if self.initialMovementDirection == MovementDirection.ALTERNATING:
                if self.currentMovementDirection == MovementDirection.FORWARD:
                    self.currentMovementDirection = MovementDirection.REVERSE
                else:
                    self.currentMovementDirection = MovementDirection.FORWARD
        
            self.startTime = time.time()
            print "Repetition " + str(self.currentBehaviorRepetition + 1) + " out of " + str(self.maxBehaviorRepetitions)
            
            self.currentWaypointIndex = 0
            self.alreadyStartedSegment = False
        return

    def reachedNewWaypoint(self, pathLength):
        timePerWaypoint = float(self.animationIntervalTime) / (pathLength)
        return time.time() - self.startTime >= timePerWaypoint * (self.currentWaypointIndex + 1) and self.currentWaypointIndex < pathLength
  
    def checkForBehaviorEnd(self, pathLength):
        return self.currentWaypointIndex >= pathLength