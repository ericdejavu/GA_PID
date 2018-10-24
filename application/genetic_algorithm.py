# -*- coding:utf-8 -*-
from const_str import *
import random,data_record
import copy

class GeneticAlgorithm:
    def __init__(self):
        self.population_pool    = []
        self.max_population     = MAX_POPULATION
        self.score              = INIT
        self.dna                = {
            ORIGIN: {},
            BEHAVE: {
                STATIC_SCORE:INIT,
                EXECUTABLE_SCORE:INIT,
                DYNAMIC_STABLE_SCORE:INIT
            }
        }
        self.max_params         = {}
        self.mutantion          = INIT
        self.tense_score        = TENSE_SCORE
        self.generation_count   = INIT
        self.control_mode       = TCP_CONGESTION_CONTROL
        self.grow_mode          = LINEAR_INC
        self.tickets            = {'waterfall_cnt':INIT}

    # call before run function blow
    def init_dna(self,dna,max_params):
        self.dna = dna
        self.max_params = max_params
        # self.data_record = data_record.DataRecord(dna)

    def random_mutante(self):
        return random.choice(self.dna[ORIGIN].keys())

    def mutant(self):
        origin_param = self.random_mutante()
        self.mutantion = random.uniform(-self.max_params[origin_param],self.max_params[origin_param])
        if self.dna[ORIGIN][origin_param] < 0:
            self.dna[ORIGIN][origin_param] += abs(self.mutantion)
        else:
            self.dna[ORIGIN][origin_param] += self.mutantion


    def next_generation(self):
        if len(self.population_pool) >= 1:
            copy_dna = copy.deepcopy(self.dna)
            self.population_pool.append(copy_dna)
            while True:
                mother = random.choice(self.population_pool)
                father = copy.deepcopy(self.dna)
                parent = [mother,father]
                for key in self.dna[ORIGIN].keys():
                    self.dna[ORIGIN][key] = random.choice(parent)[ORIGIN][key]
                self.generation_count += 1
                if random.random() < MUTANT_RATE:
                    self.mutant()
                for key in self.dna[ORIGIN].keys():
                    if self.dna[ORIGIN][key] != father[ORIGIN][key]:
                        self.dna[BEHAVE] = {
                            STATIC_SCORE:INIT,
                            EXECUTABLE_SCORE:INIT,
                            DYNAMIC_STABLE_SCORE:INIT
                        }
                        # print 'next_generation:',self.dna[ORIGIN]
                        return

    # act as tcp control
    def waterfall(self,k):
        if self.control_mode == TCP_CONGESTION_CONTROL:
            if self.tickets['waterfall_cnt'] > WATERFALL_THRESHOLD:
                self.grow_mode = EXPONENTIAL_GROWTH

            if self.grow_mode == LINEAR_INC:
                self.tense_score +=  k * TENSE_SCORE
            elif self.grow_mode == EXPONENTIAL_GROWTH:
                self.tense_score -= TENSE_SCORE**(1/k)

            if self.tense_score > MAX_SCORE:
                self.tense_score = MAX_SCORE

            # reaper kill the all
            if len(self.population_pool) == KILL_ALL:
                self.tense_score = TENSE_SCORE
                self.control_mode = LINEAR_INC
                self.tickets['waterfall_cnt'] = INIT

            self.tickets['waterfall_cnt'] += WATERFALL_INC
            if self.tense_score > NORMAL_TENSE_SCORE:
                self.tense_score = NORMAL_TENSE_SCORE


    def reaper(self):
        # self.data_record.save(self.dna)
        # sorted(self.population_pool,lambda x,y:cmp(x[BEHAVE][EXECUTABLE_SCORE],y[BEHAVE][EXECUTABLE_SCORE]))
        # print 'tense_score:',self.tense_score
        # print self.population_pool
        for dna in self.population_pool[:]:
            if dna[BEHAVE][STATIC_SCORE] < self.tense_score and len(self.population_pool) > MIN_POPULATION:
                # print 'STATIC_SCORE:',dna[BEHAVE][STATIC_SCORE]
                self.population_pool.remove(dna)

        dna_pool = [population[ORIGIN] for population in self.population_pool]
        dna_pool.reverse()
        for dna in self.population_pool[:]:
            dna_pool.pop()
            if dna[ORIGIN] in dna_pool:
                # print 'pool:',dna_pool
                # print 'population_pool:',self.population_pool
                # print 'ORIGIN:',dna[ORIGIN]
                self.population_pool.remove(dna)

        # print '-- len -- :',len(self.population_pool)
        self.waterfall(CONST_K)



    def run(self):
        self.reaper()
        self.next_generation()
        return self.dna
