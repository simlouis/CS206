import numpy

from solution import SOLUTION
import constants as c
import copy
import os
import numpy as np


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        os.system("del tmp*.txt")
        self.parents = {}
        self.children = {}
        self.nextAvailableID = 0
        self.pop_size = 0
        self.gen_size = 0
        for i in range(0, c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        self.matrix = np.empty((c.numberOfGenerations, c.populationSize))

    def evolve(self):
        self.evaluate(self.parents, currentGen=0)

        for currentGeneration in range(c.numberOfGenerations):
            self.evolve_for_one_generation(currentGeneration)

    def evolve_for_one_generation(self, currentGeneration):
        self.spawn()

        self.mutate()

        self.evaluate(self.children, currentGeneration)

        self.print()

        self.select()

    def spawn(self):
        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].set_id(self.nextAvailableID)
            self.nextAvailableID += 1

    def mutate(self):
        for i in self.children:
            self.children[i].mutate()

    def evaluate(self, solutions, currentGen):
        for i in range(c.populationSize):
            solutions[i].start_simulation("DIRECT")
        for i in range(c.populationSize):
            solutions[i].wait_for_simulation_to_end()
            self.matrix[currentGen, self.pop_size] = solutions[i].fitness
            self.pop_size += 1
        self.pop_size = 0

    def select(self):
        for i in self.parents:
            if self.children[i].fitness < self.parents[i].fitness:
                self.parents[i] = self.children[i]

    def print(self):
        for i in self.parents:
            print("\nParent Fitness: {}, Child Fitness: {}\n".format(self.parents[i].fitness, self.children[i].fitness))

    def show_best(self):
        best_key = 0
        best = self.parents[0].fitness
        for i in range(0, len(self.parents.keys()) - 1):
            if self.parents[i].fitness < best:
                best = self.parents[i].fitness
                best_key = i

        self.parents[best_key].start_simulation("GUI")

    def save_data(self):
        # numpy.savetxt("data.txt", self.matrix)
        with open('B_data.npy', 'wb') as file:
            np.save(file, self.matrix)
