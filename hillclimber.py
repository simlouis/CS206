from solution import SOLUTION
import constants as c
import copy
import os


class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    def evolve(self):
        self.parent.evaluate("GUI")

        for currentGeneration in range(c.numberOfGenerations):
            self.evolve_for_one_generation()

    def evolve_for_one_generation(self):
        self.spawn()

        self.mutate()

        self.child.evaluate("DIRECT")

        self.print()

        self.select()

    def spawn(self):
        self.child = copy.deepcopy(self.parent)

    def mutate(self):
        self.child.mutate()

    def select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    def print(self):
        print("Parent Fitness: {}, Child Fitness: {}".format(self.parent.fitness, self.child.fitness))

    def show_best(self):
        os.system("python3 simulate.py GUI")

