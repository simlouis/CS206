import math
import random
import pybullet as p
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import matplotlib.pyplot as pyplot

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0.0, 0.0, -9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

backLegAmplitude = numpy.pi / 4
backLegFrequency = 5
backLegPhaseOffset = 0

frontLegAmplitude = numpy.pi / 6
frontLegFrequency = 5
frontLegPhaseOffset = numpy.pi / 2

backLegTargetAngles = backLegAmplitude * numpy.sin(numpy.linspace(backLegFrequency * 0 + backLegPhaseOffset,
                                                                  backLegFrequency * (2 * numpy.pi) +
                                                                  backLegPhaseOffset, 1000))

frontLegTargetAngles = frontLegAmplitude * numpy.sin(numpy.linspace(frontLegFrequency * 0 + frontLegPhaseOffset,
                                                                    frontLegFrequency * (2 * numpy.pi) +
                                                                    frontLegPhaseOffset, 1000))
# numpy.save("data/targetAngles.npy", targetAngles)

for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName="Torso_BackLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=backLegTargetAngles[i],
        maxForce=50
    )

    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName="Torso_FrontLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=frontLegTargetAngles[i],
        maxForce=50
    )

    print(backLegSensorValues[i])
    t.sleep(1 / 240)

numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)

p.disconnect()
