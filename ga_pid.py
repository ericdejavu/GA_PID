# -*- coding:utf-8 -*-
from pid import *
from genetic_algorithm import *
from const_str import *

class GAPID:
    def __init__(self):
        self.GA = GeneticAlgorithm()
        self.PID = PID()
        # give two possible pid value to optimize GA
        Adam_dna = {}
        Eva_dna = {}
        self.GA.population_pool(Eva_dna)
        self.GA.init_dna(Adam_dna)

    def get_score(self):
        self.current_score = self.tune_pid()
        # get score from hardware
        pass

    def tune_pid(self):
        pid = self.GA.run()
        self.PID.tune(pid)
        return self.GA.dna['score']
