from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import time as t


class SIMULATION:
    def __init__(self, directOrGUI, solutionID):
        self.directOrGUI = directOrGUI
        self.id = solutionID
        if self.directOrGUI == "DIRECT":
            p.connect(p.DIRECT)
        else:
            p.connect(p.GUI)

        self.physicsClient = p.connect(p.DIRECT)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.world = WORLD()
        self.robot = ROBOT(solutionID)
        p.setGravity(0.0, 0.0, -9.8)
        self.robot.prepare_to_sense()

    def run(self):
        for i in range(2000):
            p.stepSimulation()
            self.robot.sense(i)
            self.robot.think()
            self.robot.act(i)
            if self.directOrGUI == "GUI":
                t.sleep(1 / 240)

    def get_fitness(self):
        self.robot.get_fitness(self.id)

    def __del__(self):
        p.disconnect()
