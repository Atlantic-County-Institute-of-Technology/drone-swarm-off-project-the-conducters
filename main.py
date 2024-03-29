# Meant to go with Frostpunk's: The City Must Survive

# Import specified packages
from codrone_edu.drone import *
import time
import random


# Drone's connection to the program
drone = Drone()
drone.pair()
# drone.takeoff()

# Function made to have the drone spiral up and down, it works spiraling up but not down.
def Spiral(seconds, upDown):
    global roll, throttle
    if upDown == "up":
        throttle = 50
        roll = 20
    elif upDown == "down":
        throttle = -50
        roll = -20
    for x in range(3):
        drone.go(roll, 0, throttle, 15, seconds)
    drone.set_yaw(-100)
    drone.move(1)
    drone.land()

# Function meant to make the drone sway left and right for a specific amount of times
def Sway(amountSway):
    for x in range(amountSway):
        drone.set_roll(50)
        drone.move(.5)
        time.sleep(1)
        drone.set_roll(-50)
        drone.move(1.5)
        time.sleep(1.5)

# Meant for the drone to go up and down
def UpDown(upDown):
    for x in range(upDown):
        drone.go(0, 0, 0, 90, upDown)
        drone.hover(0.5)
        drone.go(0,0,0,-90, upDown)
        drone.hover(0.5)




# Music 2:03 - 2:23, initial phase
    # code that section, light code basic movment

drone.takeoff()
drone.hover(1)
# Sway(2)

Spiral(2, "up")




# 2:17-2:18 is where it starts to move, left and right

drone.hover(2)

Spiral(2, "down")
# UpDown(4)




# Music 2:23 - 3:30, build up
    # code that section, spirals, circle, squares

# Music 3:30 - 3:50, crazy stuff
    # code that section, flips

# Music 3:50 - 4:10, calm down return to initial phase
    # code that section, slow down to basic music, small cicles and land.



# Ends the drone's sequence
drone.land()
drone.close()
