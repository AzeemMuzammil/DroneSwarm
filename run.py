from email.policy import default
import json
import os
from multiprocessing import Process, Queue
import threading
import subprocess
from unittest import case
from src.utils import ConvexHull
from math import sqrt
# os.system('python3 main.py')
# os.system('python3 main_1.py')
# os.system('python3 main_2.py')
# os.system('python3 main_3.py'), "python3 main_4.py","python3 main_5.py","python3 main_6.py",


scripts = (
    "python3 main_1.py",
    "python3 main_2.py",
    "python3 main_3.py", "python3 main_4.py")

# scripts1 = (
# "/home/halaldeen-ms/dev/DroneSwarm/main_1.py",\
# "/home/halaldeen-ms/dev/DroneSwarm/main_2.py",\
# "/home/halaldeen-ms/dev/DroneSwarm/main_3.py","/home/halaldeen-ms/dev/DroneSwarm/main_4.py",
# "/home/halaldeen-ms/dev/DroneSwarm/main_5.py","/home/halaldeen-ms/dev/DroneSwarm/main_6.py")


def worker():
    while True:
        item = q.get()
        os.system(item)


q = Queue()
for i in scripts:
    t = Process(target=worker)
    t.start()

for item in scripts:
    q.put(item)

q.join()


# processes = []


# for script in scripts:
#     p = subprocess.Popen(["python3" ,scripts1])
#     processes.append(p)

# for p in processes:
#     p.wait()

# polygon_tiles = [(1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (5, 3), (5, 4), (4, 4), (3, 4), (2, 4), (1, 4), (1, 3)]

# no_of_drones = input("Enter the number of Drones: ")

# drone_current_positions = []

# for i in range(0, int(no_of_drones)):
#     drone_current_positions.append(tuple([i * 3, 0]))


# while True:
#     command_string = input("Enter Command: ")

#     if (command_string.split(" ")[0]) == "takeoff":
#         for i in range(1, int(no_of_drones) + 1):
#             json_name = f"task_file/main_{i}.json"

#             with open(json_name, "r") as file:
#                 data = json.load(file)
#                 task_id = 0
#                 # if len(data) == 0:
#                 #     task_id = 1
#                 # else:
#                 #     task_id = int(data[len(data) - 1]["taskId"]) + 1
#                 entry = {
#                     "taskType": "TAKE_OFF",
#                     "taskMode": "VUT",
#                     "taskId": task_id,
#                     "heightInMeters": int(command_string.split(" ")[1])
#                 }
#                 data.append(entry)

#             with open(json_name, "w") as file:
#                 json.dump(data, file)

#     elif (command_string.split(" ")[0]) == "wait":
#         for i in range(1, int(no_of_drones) + 1):
#             json_name = f"task_file/main_{i}.json"

#             with open(json_name, "r") as file:
#                 data = json.load(file)
#                 task_id = 0
#                 # if len(data) == 0:
#                 #     task_id = 1
#                 # else:
#                 #     task_id = int(data[len(data) - 1]["taskId"]) + 1
#                 entry = {
#                     "taskType": "WAIT",
#                     "taskMode": "SEQ",
#                     "taskId": task_id,
#                     "waitTime": int(command_string.split(" ")[1])
#                 }
#                 data.append(entry)

#             with open(json_name, "w") as file:
#                 json.dump(data, file)

#     elif (command_string.split(" ")[0]) == "goto":

#         polygon_tiles_string = " ".join(command_string.split(" ")[1:])
#         polygon_tiles = []

#         for tup in polygon_tiles_string.replace(" ", "").split('),('):
#             tup = tup.replace(')', '').replace('(', '')
#             polygon_tiles.append(tuple(map(lambda x: int(x), tup.split(','))))

#         outline = ConvexHull().trace(polygon_tiles)
#         if (int(no_of_drones) != len(outline)):
#             print("The No of Drones is not matched with the shapes requirement.")
#         else:
#             polygon_coor = []
#             for coordinate in outline:
#                 new_tup = tuple(map(lambda x: x * 3, coordinate))
#                 polygon_coor.append(new_tup)

#             # print(polygon_coor)

#             dist_from_each_drones = {}
#             for i in range(0, len(drone_current_positions)):
#                 lengths = []
#                 for j in polygon_coor:
#                     length = sqrt(((drone_current_positions[i][0] - j[0]) ** 2) + (
#                         (drone_current_positions[i][1] - j[1]) ** 2))
#                     lengths.append(length)
#                 dist_from_each_drones[i] = lengths

#             # print(dist_from_each_drones)

#             dist_drone_pos = {}

#             for i in range(0, len(dist_from_each_drones)):
#                 min_key = -1
#                 min_val = float('inf')

#                 for key in dist_from_each_drones.keys():
#                     values = dist_from_each_drones[key]
#                     val = values[i]
#                     if (min_val > val):
#                         min_val = val
#                         min_key = key

#                 dist_drone_pos[min_key] = polygon_coor[i]
#                 del dist_from_each_drones[min_key]

#             print(dist_drone_pos)

#             for i in range(1, int(no_of_drones) + 1):
#                 json_name = f"task_file/main_{i}.json"

#                 with open(json_name, "r") as file:
#                     data = json.load(file)
#                     task_id = 0
#                     # if len(data) == 0:
#                     #     task_id = 1
#                     # else:
#                     #     task_id = int(data[len(data) - 1]["taskId"]) + 1
#                     entry = {
#                         "taskType": "GO_TO",
#                         "taskMode": "SEQ",
#                         "taskId": task_id,
#                         "nextLocation": {
#                             "north": dist_drone_pos[i - 1][0],
#                             "east": 0.0,
#                             "alt": dist_drone_pos[i - 1][1]
#                         }
#                     },
#                     data.append(entry)

#                 with open(json_name, "w") as file:
#                     json.dump(data, file)

#     elif (command_string.split(" ")[0]) == "land":
#         for i in range(1, int(no_of_drones) + 1):
#             json_name = f"task_file/main_{i}.json"

#             with open(json_name, "r") as file:
#                 data = json.load(file)
#                 task_id = 0
#                 # if len(data) == 0:
#                 #     task_id = 1
#                 # else:
#                 #     task_id = int(data[len(data) - 1]["taskId"]) + 1
#                 entry = {
#                     "taskType": "LAND",
#                     "taskMode": "NUT",
#                     "taskId": task_id
#                 }
#                 data.append(entry)

#             with open(json_name, "w") as file:
#                 json.dump(data, file)
