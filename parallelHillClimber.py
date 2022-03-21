from solution import SOLUTION
import constants as c
import copy
import os


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        os.system("del tmp*.txt")
        self.parents = {}
        self.children = {}
        self.nextAvailableID = 0
        for i in range(0, c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def evolve(self):
        self.evaluate(self.parents)

        for currentGeneration in range(c.numberOfGenerations):
            self.evolve_for_one_generation()

    def evolve_for_one_generation(self):
        self.spawn()

        self.mutate()

        self.evaluate(self.children)

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

    def evaluate(self, solutions):
        for i in range(c.populationSize):
            solutions[i].start_simulation("DIRECT")
        for i in range(c.populationSize):
            solutions[i].wait_for_simulation_to_end()

    def select(self):
        for i in self.parents:
            if self.children[i].fitness < self.parents[i].fitness :
                self.parents[i] = self.children[i]

    def print(self):
        for i in self.parents:
            print("\nParent Fitness: {}, Child Fitness: {}\n".format(self.parents[i].fitness, self.children[i].fitness))

    def show_best(self):
        for i in range(0, len(self.parents.keys()) - 1):
            if self.parents[i].fitness < self.parents[i + 1].fitness:
                best = self.parents[i]
            else:
                best = self.parents[i + 1]

        best.start_simulation("GUI")

