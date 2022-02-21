import numpy
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, link_name):
        self.link_name = link_name
        self.values = numpy.zeros(1000)

    def get_value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.link_name)
        if t == 999:
            print(self.values)

    def save_values(self):
        numpy.save("data/sensorValues.npy", self.values)
