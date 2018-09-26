from const_str import *
import random

class GeneticAlgorithm:
    def __init__(self):
        self.population_pool = []
        self.max_population  = MAX_POPULATION
        self.dna = {}
        self.score      = INIT
        self.mutantion  = INIT
        self.tense_score = TENSE_SCORE
        self.generation_count = INIT

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

    def reaper(self):
        sorted(self.population_pool,lambda x,y:cmp(x['score'],y['score']))
        for i,dna in enumerate(self.population_pool[:]):
            if dna['score'] < self.tense_score:
                self.population_pool = self.population_pool[:i]
                break
        self.tense_score += TENSE_SCORE
