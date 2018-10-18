# -*- coding:utf-8 -*-
from const_str import *
import random,data_record

class GeneticAlgorithm:
    def __init__(self):
        self.population_pool    = []
        self.max_population     = MAX_POPULATION
        self.score              = INIT
        self.dna                = {ORIGIN:{}, BEHAVE:{SCORE:self.score}}
        self.mutantion          = INIT
        self.tense_score        = TENSE_SCORE
        self.generation_count   = INIT
        self.control_mode       = TCP_CONGESTION_CONTROL
        self.grow_mode          = LINEAR_INC
        self.tickets            = {'waterfall_cnt':INIT}

    # call before run function blow
    # def init_dna(self,dna):
    #     self.dna = dna
    #     self.data_record = data_record.DataRecord(dna)

    def random_mutante(self):
        return random.choice(self.dna[ORIGIN].keys())

    def mutant(self):
        self.mutantion = random.uniform(-2,2)
        self.dna[ORIGIN][self.random_mutante()] += self.mutantion


    def next_generation(self):
        if len(self.population_pool) >= 1:
            mother = random.choice(self.population_pool)
            parent = [mother,self.dna]
            population_pool.append(self.dna)
            for key in self.dna.keys():
                self.dna[key] = random.choice(parent)[key]
        self.generation_count += 1
        if random.random() < MUTANT_RATE:
            self.mutant()

    # act as tcp control
    def waterfall(self,k):
        if self.control_mode == TCP_CONGESTION_CONTROL:
            if self.tickets['waterfall_cnt'] > WATERFALL_THRESHOLD:
                self.grow_mode = EXPONENTIAL_GROWTH

            if self.grow_mode == LINEAR_INC:
                self.tense_score += k*TENSE_SCORE
            elif self.grow_mode == EXPONENTIAL_GROWTH:
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
        # self.data_record.save(self.dna)
        sorted(self.population_pool,lambda x,y:cmp(x[BEHAVE][SCORE],y[BEHAVE][SCORE]))
        for i,dna in enumerate(self.population_pool[:]):
            if dna[BEHAVE][SCORE] < self.tense_score:
                self.population_pool = self.population_pool[:i]
                break
        self.waterfall(CONST_K)



    def run(self):
        self.next_generation()
        self.reaper()
        return self.dna
