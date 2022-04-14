import numpy
import pyrosim.pyrosim as pyrosim
import pyrosim.neuron as neuron


class SENSOR:
    def __init__(self, link_name):
        self.link_name = link_name
        self.values = numpy.zeros(1500)

    def get_value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.link_name)
        if t == 1499:
            pass
            # print(self.values)

    def save_values(self):
        numpy.save("data/sensorValues.npy", self.values)
