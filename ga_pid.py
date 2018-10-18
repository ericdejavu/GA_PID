# -*- coding:utf-8 -*-
from libs import *
from fake.sim_io import *



class GAPID:
    def __init__(self):
        self.GA = GeneticAlgorithm()
        self.PID = PID()
        self.graph = Graph()
        # give two possible pid value to optimize GA
        Adam_dna = {}
        Eva_dna = {}
        self.GA.population_pool.append(Eva_dna)
        # self.GA.init_dna(Adam_dna)

    def get_score(self):
        self.current_score = self.tune_pid()
        # get score from hardware
        pass

    def tune_pid(self):
        pid = self.GA.run()
        self.PID.tune(pid)
        return self.GA.dna['score']

    def init_test(self,pid):
        self.PID.clear()
        self.PID.set_limit(max_err=180.0, max_out=100.0)
        self.PID.tune(pid)
        print self.PID.get()
        self.angle = 0
        self.preangle = 0
        self.v = 0
        self.angle_set = 90


    def pid_test(self, dt, k):
        err = self.angle_set - self.angle
        out = self.PID.run(err)
        self.angle += sim(self.v, out, dt, set_val=self.angle_set)
        self.v = self.angle - self.preangle
        self.preangle = self.angle

        if self.angle < 0:
            self.angle = 0
        elif self.angle > 180:
            self.angle = 180
        return self.angle,out

    def run_test(self):
        datas = []
        for j in range(6,9):
            lx,ly = [],[]
            kp = j*0.1
            self.init_test({'kp':0.6,'ki':0.0001,'kd':2.0})
            for i in range(500):
                cache_out = self.pid_test(0.01, k)
                # print i,cache_out
                lx.append(i)
                ly.append(cache_out[0])
            datas.append([lx,ly,str(kp)])

        print self.PID.get()
        print self.PID.get_max()
        self.graph.draw(datas)

ga_pid = GAPID()
ga_pid.run_test()
