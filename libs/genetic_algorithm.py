from const_str import *
import random

class GeneticAlgorithm:
    def __init__(self):
        self.population_pool    = []
        self.max_population     = MAX_POPULATION
        self.dna                = {}
        self.score              = INIT
        self.mutantion          = INIT
        self.tense_score        = TENSE_SCORE
        self.generation_count   = INIT
        self.control_mode       = TCP_CONGESTION_CONTROL
        self.grow_mode          = LINEAR_INC
        self.tickets            = {'waterfall_cnt':INIT}

    def mutant(self):
        self.mutantion = random.uniform(-2,2)
        random.choice(self.dna) += self.mutantion


    def next_generation(self):
        if len(self.population_pool) >= 1:
            mother = random.choice(self.population_pool)
            parent = [mother,self.dna]
            population_pool.append(self.dna)
            for key in self.dna.keys():
                self.dna[key] = random.choice(parent)[key]
        self.generation_count += 1
        if random.random() < 0.2:
            self.mutant()

    # act as tcp control
    def waterfall(self,k):
        if self.control_mode == TCP_CONGESTION_CONTROL:
            if self.tickets['waterfall_cnt'] > WATERFALL_THRESHOLD:
                self.grow_mode = EXPONENTIAL_GROWTH

            if self.grow_mode == LINEAR_INC:
                self.tense_score += k*TENSE_SCORE
            elif self.grow_mode = EXPONENTIAL_GROWTH:
                self.tense_score += TENSE_SCORE**(1/k)

            if self.tense_score > MAX_SCORE:
                self.tense_score = MAX_SCORE

            # reaper kill the all
            if len(self.population_pool) == KILL_ALL:
                self.tense_score = TENSE_SCORE
                self.control_mode = LINEAR_INC
                self.tickets['waterfall_cnt'] = INIT

            self.tickets['waterfall_cnt'] += WATERFALL_INC



    def reaper(self):
        sorted(self.population_pool,lambda x,y:cmp(x['score'],y['score']))
        for i,dna in enumerate(self.population_pool[:]):
            if dna['score'] < self.tense_score:
                self.population_pool = self.population_pool[:i]
                break
        self.waterfall(CONST_K)
