import numpy
import matplotlib.pyplot as pyplot
import constants as c

A_data = numpy.load("A_data.npy")
B_data = numpy.load("B_data.npy")

A_data_mean = []
B_data_mean = []

for i in range(len(A_data)):
    A_data_mean.append(numpy.mean(A_data[i]))

for i in range(len(B_data)):
    B_data_mean.append(numpy.mean(B_data[i]))

pyplot.xlabel("Generation")
pyplot.ylabel("Fitness")

pyplot.plot(A_data_mean, label="Quadruped")
pyplot.plot(B_data_mean, label="Hexapod")

pyplot.legend(bbox_to_anchor=(0.75, 1))
pyplot.savefig("AB_Testing.png")
pyplot.show()
