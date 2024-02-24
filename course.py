from codrone_edu.drone import *
import time


drone = Drone()
drone.pair()

try:
    drone.takeoff()

    # go through arch
    drone.set_pitch(100)
    drone.move(0.5)
    drone.set_pitch(0)

    #go up and loop arch
    drone.set_throttle(75)
    drone.move(2)
    drone.set_throttle(0)

    drone.set_pitch(-100)
    drone.move(0.5)
    drone.set_pitch(0)

    drone.set_throttle(-75)
    drone.move(2)
    drone.set_throttle(0)

    # go to hoop after loop arch
    drone.set_pitch(100)
    drone.move(1.5)
    drone.set_pitch(0)

    # loop hoop
    drone.set_throttle(50)
    drone.move(2)
    drone.set_throttle(0)

    drone.set_pitch(-100)
    drone.move(0.5)
    drone.set_pitch(0)

    drone.set_throttle(-50)
    drone.move(2)
    drone.set_throttle(0)

    drone.set_pitch(80)
    drone.move(0.5)
    drone.set_pitch(0)

    drone.set_yaw(50)
    drone.move(2)
    drone.set_yaw(0)

    drone.set_pitch(50)
    drone.move(0.5)
    drone.set_pitch(0)

    # loop hoop
    drone.set_throttle(50)
    drone.move(2)
    drone.set_throttle(0)

    drone.set_pitch(-100)
    drone.move(0.5)
    drone.set_pitch(0)

    drone.set_throttle(-50)
    drone.move(2)
    drone.set_throttle(0)

    drone.set_pitch(80)
    drone.move(0.5)
    drone.set_pitch(0)

    drone.set_pitch(100)
    drone.move(0.5)
    drone.set_pitch(0)

    #go up and loop arch
    drone.set_throttle(75)
    drone.move(2)
    drone.set_throttle(0)

    drone.set_pitch(-100)
    drone.move(0.5)
    drone.set_pitch(0)

    drone.set_throttle(-75)
    drone.move(2)
    drone.set_throttle(0)

    color = drone.get_color_data()
    drone.set_drone_LED(color)
    print(color)

    drone.move(0)
    time.sleep(5)

    drone.land()

except KeyboardInterrupt:
    drone.land()
