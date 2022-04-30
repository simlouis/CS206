import os
# from hillclimber import HILL_CLIMBER
from parallelHillClimber import PARALLEL_HILL_CLIMBER


phc = PARALLEL_HILL_CLIMBER()
phc.evolve()
phc.save_data()
phc.show_best()

