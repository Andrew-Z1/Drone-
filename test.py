from codrone_edu.drone import *
import time

# Initialize drone
drone = Drone()
drone.pair()
print("Command Options: ")
print("""
w: throttle up
s: throttle down
a: yaw left
d: yaw right
i: pitch forward
k: pitch backward
j: roll left
l: roll right
q: quit
""")

# Takeoff and set default power
drone.takeoff()
power = 40  # Default throttle power

# Main control loop
while True:
    # Reset controls to 0
    drone.set_throttle(0)
    drone.set_roll(0)
    drone.set_yaw(0)
    drone.set_pitch(0)

    # Get user input for control direction
    direction = input("Input a command: ")

    # Process the input to control the drone
    if direction == "w":
        drone.set_throttle(power)
    elif direction == "s":
        drone.set_throttle(-power)
    elif direction == "a":
        drone.set_yaw(-power)
    elif direction == "d":
        drone.set_yaw(power)
    elif direction == "i":
        drone.set_pitch(power)
    elif direction == "k":
        drone.set_pitch(-power)
    elif direction == "j":
        drone.set_roll(-power)
    elif direction == "l":
        drone.set_roll(power)
    elif direction == "q":
        time.sleep(1)  # Wait before landing
        drone.land()  # Land the drone
        break  # Exit the loop
    else:
        print("Not a command")

    # Make the drone move for 1 second based on the current control
    drone.move(1)

# Print done after exiting the loop
print("Done")
drone.close()  # Close the drone connection
