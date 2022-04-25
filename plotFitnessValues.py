import numpy
import matplotlib.pyplot as pyplot
import constants as c

A_data = numpy.load("A_data.npy")
B_data = numpy.load("data.npy")

A_data_mean = numpy.empty((0, c.numberOfGenerations))

# for i in range(len(A_data)):


pyplot.xlabel("Number of Generations")
pyplot.ylabel("Fitness")

pyplot.plot(A_data)
# pyplot.plot(B_data)

pyplot.legend(bbox_to_anchor=(0.75, 1))
pyplot.show()
