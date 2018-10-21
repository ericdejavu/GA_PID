# -*- coding:utf-8 -*-
import random

# k 输出增益
k = 2750
p = 5
v_max = p/10.0
noise_range = 0.5

# {'ki': 0.1730263652030822, 'kp': 201.77981190260044, 'kd': 332.4939952908603}
# best setting {'kp':0.6,'ki':0.0001,'kd':2.0}

def sim(v, out, dt, set_val=90):
    # print '-------v:'+str(v*dt)
    # print '-------k*out:'+str(k*out*dt**2)
    noise = noise_range-random.random()*noise_range*2
    angle = v + k*out*dt**2 + noise
    return angle
