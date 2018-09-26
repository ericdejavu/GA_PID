from pid import *
from genetic_algorithm import *
from const_str import *

class GAPID:
    def __init__(self):
        self.GA = GeneticAlgorithm()
        self.PID = PID()
        Adam_dna = {}
        Eva_dna = {}
        self.GA.population_pool(Eva_dna)
        self.GA.dna = Adam_dna
