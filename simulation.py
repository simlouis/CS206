from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import time as t


class SIMULATION:
    def __init__(self, directOrGUI):

        if directOrGUI == "DIRECT":
            p.connect(p.DIRECT)
        else:
            p.connect(p.GUI)

        self.physicsClient = p.connect(p.DIRECT)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.world = WORLD()
        self.robot = ROBOT()
        p.setGravity(0.0, 0.0, -9.8)
        self.robot.prepare_to_sense()

    def run(self):
        for i in range(1000):
            p.stepSimulation()
            self.robot.sense(i)
            self.robot.think()
            self.robot.act(i)
            t.sleep(1 / 240)

    def get_fitness(self):
        self.robot.get_fitness()

    def __del__(self):
        p.disconnect()
