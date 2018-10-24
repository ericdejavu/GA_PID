# -*- coding:utf-8 -*-
from application import *
from fake.sim_io import *



class GAPID:
    def __init__(self):
        self.GA = GeneticAlgorithm()
        self.PID = PID()
        self.graph = Graph()
        # give two possible pid value to optimize GA
        Adam_dna = {
            ORIGIN:{'kp':0.4,'ki':0.0001,'kd':1.0},
            BEHAVE:{
                STATIC_SCORE:INIT,
                EXECUTABLE_SCORE:INIT
            }
        }
        Eva_dna = {
            ORIGIN:{'kp':0.8,'ki':0.0001,'kd':1.5},
            BEHAVE:{
                STATIC_SCORE:INIT,
                EXECUTABLE_SCORE:INIT
            }
        }
        self.GA.population_pool.append(Eva_dna)
        self.benchmark = BenchMark()
        self.PID.set_limit(max_err=180.0, max_out=100.0)
        self.GA.init_dna(Adam_dna,self.PID.max_params)

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
        self.angle = 0
        self.preangle = 0
        self.v = 0
        self.angle_set = 90
        self.init_bench()

    def init_bench(self):
        self.benchmark.clear(self.angle_set,self.angle)

    def bench_run(self,data):
        self.benchmark.online_update(data)

    def bench_score(self):
        self.GA.dna[BEHAVE][STATIC_SCORE] = self.benchmark.get_static_score()
        self.GA.dna[BEHAVE][EXECUTABLE_SCORE] = self.benchmark.get_executable_score()
        if self.GA.dna[BEHAVE][STATIC_SCORE] > 0.0001 and self.GA.dna[ORIGIN]['kd'] < 0:
            self.benchmark.print_bench()

    def pid_test(self, dt, k):
        err = self.angle_set - self.angle
        out = self.PID.run(err)
        self.angle += sim(self.v, out, dt, set_val=self.angle_set)

        self.bench_run(self.angle)
        self.v = self.angle - self.preangle
        self.preangle = self.angle

        if self.angle < 0:
            self.angle = 0
        elif self.angle > 180:
            self.angle = 180
        return self.angle, out

    def run_test(self):
        print 'run benchmark ...'
        datas = []
        for j in range(200):
            lx,ly = [],[]
            # print j,' --------------'
            # print self.GA.dna[ORIGIN]
            self.init_test(self.GA.dna[ORIGIN])
            for i in range(500):
                cache_out = self.pid_test(0.01, k)
                # print i,cache_out
                lx.append(i)
                ly.append(cache_out[0])
            self.bench_score()
            datas.append([lx,ly,str(self.GA.dna)])
            self.GA.run()

        datas = []

        for dna in self.GA.population_pool:
            lx,ly = [],[]
            self.init_test(dna[ORIGIN])
            for i in range(500):
                cache_out = self.pid_test(0.01, k)
                # print i,cache_out
                lx.append(i)
                ly.append(cache_out[0])
            datas.append([lx,ly,""])
        print '-- alive population_pool size --:',len(datas)

        self.graph.draw(datas)

ga_pid = GAPID()
ga_pid.run_test()
