import pybullet as p
import time as t
import pybullet_data

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0.0, 0.0, -9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("boxes.sdf")

for i in range(10000):
    p.stepSimulation()
    t.sleep(1 / 60)
    # print(i)

p.disconnect()

