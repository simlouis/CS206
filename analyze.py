import numpy
import matplotlib.pyplot as pyplot

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")

# print(backLegSensorValues)

pyplot.plot(backLegSensorValues, linewidth=4, label="BackLeg")
pyplot.plot(frontLegSensorValues, label="FrontLeg")

pyplot.legend(bbox_to_anchor=(0.75, 1))
pyplot.show()