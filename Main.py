import sys
from Drone import Drone
import time
#here you should interact with the drone
 
drone = Drone("192.168.10.1",8889)
drone.connect()
drone.takeOff()



time.sleep(1)

drone.forward(30)

drone.takeTheStairsWithCurve(20, 25, 5, -90, 3) # stepHeight, stepDepth, numSteps, turnAngle, numSections



drone.land()
drone.end()


