import holodeck
import numpy as np
import cv2
import random

# config = {
#     "name": "MaxDistance",
#     "world": "EuropeanForest",
#     "package_name": "DefaultWorlds",
#     "main_agent": "uav0",
#     "agents": [
#         {
#             "agent_name": "uav0",
#             "agent_type": "UavAgent",
#             "sensors": [
#                 {
#                     "sensor_type": "RGBCamera",
#                     "socket": "CameraSocket"
#                 },
#                 {
#                     "sensor_type": "LocationSensor"
#                 },
#                 {
#                     "sensor_type": "OrientationSensor"
#                 },
#                 {
#                     "sensor_type": "VelocitySensor"
#                 },
#                 {
#                     "sensor_type": "CollisionSensor"
#                 },
#                 {
#                     "sensor_type": "IMUSensor"
#                 },
#                 {
#                     "sensor_type": "AbuseSensor"
#                 },
#                 {
#                     "sensor_type": "DistanceTask",
#                     "configuration": {
#                         "Interval": 5,
#                         "GoalDistance": 500,
#                         "MaximizeDistance": True
#                     }
#                 }
#             ],
#             "control_scheme": 0,
#             "location": [random.randint(0, 50), random.randint(0, 50), 30],
#             "rotation": [random.randint(0, 180), 0, 0]
#         }
#     ],
#     "window_width": 1280,
#     "window_height": 720
# }
env = holodeck.make("UrbanCity-MaxDistance")
print(env.info())
env.reset()
env.agents['uav0'].teleport(np.array([random.randint(-100, 100), random.randint(-100, 100), 30]), np.array([0, 0, random.randint(0, 180)]))
# The UAV takes 3 torques and a thrust as a command.


for i in range(5000):
    if i == 0:
        command = np.array([-1, -2, 5, 20])
    elif i < 250:
        command = np.array([0, 0, 0, 20])
    else:
        command = np.array([0, 0, 0, 20])

    state, reward, terminal, info = env.step(command)
    print(state)
