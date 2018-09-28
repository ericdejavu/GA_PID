# -*- coding:utf-8 -*-
from const_str import *
import random,json,MySQLdb

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

    def __del__(self):
        self.db.close()

    def db_init(self):
        self.columns = self.dna.keys()
        with open('private/mysql.json') as f:
            json.dump(sqli,f)
        self.db = MySQLdb.connect(sqli['host'],sqli['user'],sqli['passwd'],sqli['db'],charset=sqli['charset'])
        self.cursor = db.cursor()
        create_table_body = ', '.join([column + COLUMN_TYPE for column in columns])
        create_table_sql = CREATE_TABLE_FH + create_table_body[:-2] + CREATE_TABLE_END
        self.cursor.execute(create_table_sql)

    def save(self):
        try:
            save_body_keys = ', '.join([column for column in self.columns])[:-2]
            save_body_values = ', '.join([str(value) for self.dna[column] in self.columns])[:-2]
            insert_sql = INSERT_HEAD+'('+save_body_keys+INSERT_MID+'('+save_body_values+INSERT_END
            self.cursor.execute(insert_sql)
            self.db.commit()
        except:
            print '[-] db is not init'


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
        self.save()
        sorted(self.population_pool,lambda x,y:cmp(x['score'],y['score']))
        for i,dna in enumerate(self.population_pool[:]):
            if dna['score'] < self.tense_score:
                self.population_pool = self.population_pool[:i]
                break
        self.waterfall(CONST_K)

    def run(self):
        self.next_generation()
        self.reaper()
        return self.dna
