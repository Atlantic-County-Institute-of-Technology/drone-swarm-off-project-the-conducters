from codrone_edu.drone import *

import time
import math 

drone = Drone()
drone.pair()
drone.takeoff()

def xCoordinates():
    xAxis = 0
    increment = 0.1
    direction = 1
    while True:
        print(xAxis)
        
        xAxis += increment * direction
        xAxis = round(xAxis, 2)
        
        if xAxis >= 1:
            direction = -1
            xAxis = 1
        elif xAxis <= -1:
            direction = 1
            xAxis = -1
        yAxisPositive = (math.sqrt( 2 * ((-2 * (xAxis**2)) + math.sqrt((8*(xAxis)**2) + 1) - 1) ) / 2)
        yAxisNegative = -1 * (math.sqrt( 2 * ((-2 * (xAxis**2)) + math.sqrt((8*(xAxis)**2) + 1) - 1) ) / 2)

        if direction == 1 and xAxis >= 0:
            yAxis = yAxisNegative
            print("Going forward in positive")
            drone.move_forward(distance=xAxis,units='ft', speed=1)
            drone.move_right(distance=yAxis, units='ft', speed=1)
        elif direction == -1 and xAxis >=0:
            yAxis = yAxisPositive
            print("Returning")
            drone.move_backward(distance=xAxis,units='ft', speed=1)
            drone.move_left(distance=yAxis, units='ft', speed=1)
        elif direction == -1 and xAxis <= 0:
            yAxis = yAxisNegative
            print("Negative Region Returning")
            drone.move_backward(distance=xAxis,units='ft', speed=1)
            drone.move_right(distance=yAxis, units='ft', speed=1)
        elif direction == 1 and xAxis <= 0:
            yAxis = yAxisPositive
            print("Negative Region Positive")
            drone.move_forward(distance=xAxis,units='ft', speed=1)
            drone.move_left(distance=yAxis, units='ft', speed=1)
        print(f'This is the y axis: {yAxis}')
        time.sleep(1)
    

xCoordinates()
