# -*- coding:utf-8 -*-
from const_str import *

class PID:
    def __init__(self):
        self.kp         = INIT
        self.ki         = INIT
        self.kd         = INIT
        self.out        = INIT
        self.bias       = INIT
        self.p_err      = INIT
        self.sum_err    = INIT
        self.max_ki     = MAX_KI

    def tune(self, (kp, ki, kd), bias=0):
        self.kp = self.limit(kp, self.max_kp)
        self.ki = self.limit(ki, self.max_ki)
        self.kd = self.limit(kd, self.max_ki)
        self.bias = bias

    def set_limit(self, max_err, max_out):
        self.max_out = max_out
        self.max_kp = max_out / max_err
        self.max_kd = self.max_p * 2 / 3
        self.max_sum_err = max_err * 5

    def get_result(self, err):
        p = self.kp*err
        i = self.ki*self.sum_err
        d = self.kd*(err-self.p_err)
        self.p_err = err
        self.sum_err += err
        return p+i+d+self.bias

    def limit(self, value, max):
        if value > max:
            value = max
        elif value < -max:
            value = -max
        return value

    def filter(self, err):
        self.sum_err = self.limit(self.sum_err, self.max_sum_err)
        out = self.get_result(err)
        out = self.limit(out, self.max_out)
        return out

    def run(self, err):
        return self.filter(err)
