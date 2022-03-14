import constants as c
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p


class MOTOR:
    def __init__(self, joint_name):
        self.joint_name = joint_name
        # self.prepare_to_act()

    # def prepare_to_act(self):
    #     self.amplitude = c.backLegAmplitude
    #     self.frequency = c.backLegFrequency
    #     self.offset = c.backLegPhaseOffset
    #     if self.joint_name == "Torso_BackLeg":
    #         temp = self.frequency / 2
    #         self.motor_values = self.amplitude * numpy.sin(numpy.linspace(temp * 0 + self.offset,
    #                                                                       temp * (2 * numpy.pi) +
    #                                                                       self.offset, 1000))
    #     else:
    #         self.motor_values = self.amplitude * numpy.sin(numpy.linspace(self.frequency * 0 + self.offset,
    #                                                                       self.frequency * (2 * numpy.pi) +
    #                                                                       self.offset, 1000))

    def set_value(self, robot_id, desiredAngle):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robot_id,
            jointName=self.joint_name,
            controlMode=p.POSITION_CONTROL,
            targetPosition=desiredAngle,
            maxForce=25
        )

