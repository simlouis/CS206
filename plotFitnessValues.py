import numpy
import matplotlib.pyplot as pyplot
import constants as c

Quad_parent_data = numpy.load("A_parent_data.npy")
Quad_children_data = numpy.load("A_children_data.npy")
Hex_parent_data = numpy.load("B_parent_data.npy")
Hex_children_data = numpy.load("B_children_data.npy")

ax = pyplot.subplots()

Quad_avg_children = []
for i in range(len(Quad_children_data)):
    Quad_avg_children.append(numpy.mean(Quad_children_data[i]))

Quad_avg_children.sort(reverse=True)

Hex_avg_children = []
for i in range(len(Hex_children_data)):
    Hex_avg_children.append(numpy.mean(Hex_children_data[i]))

Hex_avg_children.sort(reverse=True)

pyplot.scatter(range(len(Quad_avg_children)), Quad_avg_children, label="Quadruped Avg Child Fitness")
pyplot.scatter(range(len(Hex_avg_children)), Hex_avg_children, label="Hex Avg Child Fitness")

Hex_parent_mean = []
for i in range(len(Quad_parent_data)):
    Hex_parent_mean.append(numpy.mean(Hex_parent_data[i]))

Hex_parent_mean.sort(reverse=True)
pyplot.plot(Hex_parent_mean, label="Hexapod Parent's Average")

Quad_parent_mean = []
for i in range(len(Quad_parent_data)):
    Quad_parent_mean.append(numpy.mean(Quad_parent_data[i]))

Quad_parent_mean.sort(reverse=True)
pyplot.plot(Quad_parent_mean, label="Quadrupeds Parent's Average")


pyplot.xticks([0, 1, 2, 3, 4])
pyplot.xlabel("Parent")
pyplot.ylabel("Fitness")
pyplot.title("Average Fitnesses")
pyplot.legend(loc='upper right', fontsize=8)
pyplot.savefig("Final_Graph.png")
pyplot.show()
