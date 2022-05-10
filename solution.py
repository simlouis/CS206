import numpy as numpy
import pybullet as p
import pyrosim.pyrosim as pyrosim
import random
import os
import time as t
import constants as c


class SOLUTION:
    def __init__(self, id):
        self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons)
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
        temp = float(f.readline())
        self.fitness = temp
        os.system("del {}".format(fitnessFileName))

    def create_world(self):
        pyrosim.Start_SDF("world.sdf")

        # Left Wall
        left_x = -2
        left_y = -2
        for i in range(10):
            cube = pyrosim.Send_Cube(name="Left_Cube" + str(i), pos=[left_x, left_y, 1], size=[1, 1, 1], mass=100)
            left_x -= 1.5
            left_y += 1

        # Right Wall
        right_x = 2
        right_y = 2
        for i in range(10):
            pyrosim.Send_Cube(name="Right_Cube" + str(i), pos=[right_x, right_y, 1], size=[1, 1, 1], mass=100)
            right_x -= 1.5
            right_y += 1

        pyrosim.End()

    def create_body(self):
        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1, 1, 1])

        # Upper legs
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",
                           position=[0, 0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])

        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute",
                           position=[0, -0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])

        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute",
                           position=[0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[1.0, 0.2, 0.2])

        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute",
                           position=[-0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[1.0, 0.2, 0.2])

        # pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute",
        #                    position=[-0.5, 0, 1], jointAxis="0 1 0")
        # pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, -0.25, 0], size=[1.0, 0.2, 0.2])
        #
        # pyrosim.Send_Joint(name="Torso_LeftLegSecond", parent="Torso", child="LeftLegSecond", type="revolute",
        #                    position=[-0.5, 0, 1], jointAxis="0 1 0")
        # pyrosim.Send_Cube(name="LeftLegSecond", pos=[-0.5, 0.25, 0], size=[1.0, 0.2, 0.2])
        #
        # pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute",
        #                    position=[0.5, 0, 1], jointAxis="0 1 0")
        # pyrosim.Send_Cube(name="RightLeg", pos=[0.5, -0.25, 0], size=[1.0, 0.2, 0.2])
        #
        # pyrosim.Send_Joint(name="Torso_RightLegSecond", parent="Torso", child="RightLegSecond", type="revolute",
        #                    position=[0.5, 0, 1], jointAxis="0 1 0")
        # pyrosim.Send_Cube(name="RightLegSecond", pos=[0.5, 0.25, 0], size=[1.0, 0.2, 0.2])

        # Lower legs
        pyrosim.Send_Joint(name="FrontLeg_FrontLowerLeg", parent="FrontLeg", child="FrontLowerLeg", type="revolute",
                           position=[0, 1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="BackLeg_BackLowerLeg", parent="BackLeg", child="BackLowerLeg", type="revolute",
                           position=[0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", parent="LeftLeg", child="LeftLowerLeg",
                           type="revolute", position=[-1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="RightLeg_RightLowerLeg", parent="RightLeg", child="RightLowerLeg",
                           type="revolute", position=[1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        # pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", parent="LeftLeg", child="LeftLowerLeg",
        #                    type="revolute", position=[-1, 0, 0], jointAxis="0 1 0")
        # pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, -0.25, -0.5], size=[0.2, 0.2, 1])
        #
        # pyrosim.Send_Joint(name="LeftLegSecond_LeftLowerLegSecond", parent="LeftLegSecond", child="LeftLowerLegSecond",
        #                    type="revolute", position=[-1, 0, 0], jointAxis="0 1 0")
        # pyrosim.Send_Cube(name="LeftLowerLegSecond", pos=[0, 0.25, -0.5], size=[0.2, 0.2, 1])
        #
        # pyrosim.Send_Joint(name="RightLeg_RightLowerLeg", parent="RightLeg", child="RightLowerLeg",
        #                    type="revolute", position=[1, 0, 0], jointAxis="0 1 0")
        # pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, -0.25, -0.5], size=[0.2, 0.2, 1])
        #
        # pyrosim.Send_Joint(name="RightLegSecond_RightLowerLegSecond", parent="RightLegSecond",
        #                    child="RightLowerLegSecond", type="revolute", position=[1, 0, 0], jointAxis="0 1 0")
        # pyrosim.Send_Cube(name="RightLowerLegSecond", pos=[0, 0.25, -0.5], size=[0.2, 0.2, 1])

        pyrosim.End()

    def create_brain(self):
        pyrosim.Start_NeuralNetwork("brain{}.nndf".format(self.myID))

        # Quadruped
        pyrosim.Send_Sensor_Neuron(name=0, linkName="BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="RightLowerLeg")

        # Motor neurons
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=5, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name=6, jointName="Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name=7, jointName="Torso_RightLeg")
        pyrosim.Send_Motor_Neuron(name=8, jointName="BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron(name=9, jointName="FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron(name=10, jointName="LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron(name=11, jointName="RightLeg_RightLowerLeg")

        # # Hexaped
        # # Sensor Neurons
        # pyrosim.Send_Sensor_Neuron(name=0, linkName="BackLowerLeg")
        # pyrosim.Send_Sensor_Neuron(name=1, linkName="FrontLowerLeg")
        # pyrosim.Send_Sensor_Neuron(name=2, linkName="LeftLowerLeg")
        # pyrosim.Send_Sensor_Neuron(name=3, linkName="LeftLowerLegSecond")
        # pyrosim.Send_Sensor_Neuron(name=4, linkName="RightLowerLeg")
        # pyrosim.Send_Sensor_Neuron(name=5, linkName="RightLowerLegSecond")
        #
        # # Motor neurons
        # pyrosim.Send_Motor_Neuron(name=6, jointName="Torso_BackLeg")
        # pyrosim.Send_Motor_Neuron(name=7, jointName="Torso_FrontLeg")
        # pyrosim.Send_Motor_Neuron(name=8, jointName="Torso_LeftLeg")
        # pyrosim.Send_Motor_Neuron(name=9, jointName="Torso_LeftLegSecond")
        # pyrosim.Send_Motor_Neuron(name=10, jointName="Torso_RightLeg")
        # pyrosim.Send_Motor_Neuron(name=11, jointName="Torso_RightLegSecond")
        # pyrosim.Send_Motor_Neuron(name=12, jointName="BackLeg_BackLowerLeg")
        # pyrosim.Send_Motor_Neuron(name=13, jointName="FrontLeg_FrontLowerLeg")
        # pyrosim.Send_Motor_Neuron(name=14, jointName="LeftLeg_LeftLowerLeg")
        # pyrosim.Send_Motor_Neuron(name=15, jointName="LeftLegSecond_LeftLowerLegSecond")
        # pyrosim.Send_Motor_Neuron(name=16, jointName="RightLeg_RightLowerLeg")
        # pyrosim.Send_Motor_Neuron(name=17, jointName="RightLegSecond_RightLowerLegSecond")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(0, c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+c.numSensorNeurons, weight=self.weights[currentRow][currentColumn])

        pyrosim.End()

    def mutate(self):
        randRow = random.randint(0, 2)
        randCol = random.randint(0, 1)

        self.weights[randRow, randCol] = numpy.random.rand() * 2 - 1

    def set_id(self, id):
        self.myID = id

