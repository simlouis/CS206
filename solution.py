import numpy as numpy
import pyrosim.pyrosim as pyrosim
import random
import os
import time as t


class SOLUTION:
    def __init__(self, id):
        self.weights = numpy.random.rand(3, 2)
        self.weights = self.weights * 2 - 1
        self.myID = id

    def start_simulation(self, type):
        self.create_world()
        self.create_body()
        self.create_brain()

        os.system("python3 simulate.py {} {}".format(type, self.myID))

    def wait_for_simulation_to_end(self):
        fitnessFileName = "fitness{}.txt".format(self.myID)
        while not os.path.exists(fitnessFileName):
            t.sleep(0.01)
        f = open(fitnessFileName)
        temp = f.readline()
        temp = float(temp)
        self.fitness = temp
        os.system("del {}".format(fitnessFileName))

    def create_world(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()

    def create_body(self):
        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[1, 1, 1])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1, 0, 1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2, 0, 1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[1, 1, 1])

        pyrosim.End()

    def create_brain(self):
        pyrosim.Start_NeuralNetwork("brain{}.nndf".format(self.myID))

        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

        for currentRow in range(3):
            for currentColumn in range(0, 2):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+3, weight=self.weights[currentRow][currentColumn])

        pyrosim.End()

    def mutate(self):
        randRow = random.randint(0, 2)
        randCol = random.randint(0, 1)

        self.weights[randRow, randCol] = numpy.random.rand() * 2 - 1

    def set_id(self, id):
        self.myID = id

