from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import time as t


class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.world = WORLD()
        self.robot = ROBOT()
        p.setGravity(0.0, 0.0, -9.8)
        self.robot.prepare_to_sense()

    def __del__(self):
        p.disconnect()

    def run(self):
        for i in range(1000):
            p.stepSimulation()
            self.robot.sense(i)
            self.robot.think()
            self.robot.act(i)
            t.sleep(1 / 1000)
            # print(i)
