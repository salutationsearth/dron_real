from codrone_edu.drone import *
import time
import json

drone = Drone()
drone.pair()
dataset = "color_data"
colors = ["green", "blue", "red"]
data_dict = {
    "green": None,
    "blue": None,
    "red": None
}

for color in colors:
    data = []
    samples = 500
    for i in range(1):
        print("Sample: ", i+1)
        next = input("Press enter to calibrate " + color)
        print("0% ", end="")
        for j in range(samples):
            color_data = drone.get_color_data()[0:9]
            data.append(color_data)
            time.sleep(0.005)
            if j % 10 == 0:
                print("-", end="")
        print(" 100%")
    drone.new_color_data(color, data, dataset)

    data_dict[color] = data

print("Done calibrating.")

json.dump(data_dict, open("drone_color_data.json", "w+"))
