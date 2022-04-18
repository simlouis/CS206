import os
import constants as c
import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK


class ROBOT:

    def __init__(self, solutionID):
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.prepare_to_sense()
        self.prepare_to_act()
        self.nn = NEURAL_NETWORK("brain{}.nndf".format(solutionID))
        os.system("del brain{}.nndf".format(solutionID))
        os.system("del fitness{}.txt".format(solutionID))

    def prepare_to_sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def sense(self, t):
        for i in pyrosim.linkNamesToIndices:
            self.sensors[i].get_value(t)

    def prepare_to_act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName].set_value(self.robotId, desiredAngle)

    def think(self):
        self.nn.Update()

    def get_fitness(self, solutionID):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        base = basePositionAndOrientation[0]
        zCoordinateOfLinkZero = base[2]
        # zCoordinateOfLinkZero = p.getLinkState(self.robotId, 2)[0][0]

        filename = "tmp{}.txt".format(solutionID)
        f = open(filename, "w")
        f.write(str(zCoordinateOfLinkZero))
        f.close()
        os.system("rename {} fitness{}.txt".format(filename, solutionID))

