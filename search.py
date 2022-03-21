import os
# from hillclimber import HILL_CLIMBER
from parallelHillClimber import PARALLEL_HILL_CLIMBER


phc = PARALLEL_HILL_CLIMBER()
phc.evolve()
phc.show_best()

# # for i in range(2):
# os.system("python3 simulate.py GUI 0")
