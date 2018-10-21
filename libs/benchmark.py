# -*- coding:utf-8 -*-
from const_str import *
import time

# #### 定义
# - **峰值**(pick)
#   第一次超出设定值后的所到达的极值
# - **稳定性**(stable)
#   在设定值不变的情况下，第二次到达设定值之后所有数据的均方差
# - **反应时间**(react time)
#   第一次到达设定值所用的时间
# - **响应时间**(response time)
#   第二次到达设定值所使用的时间
# - **动态稳定性**(dynamic stable)
#   在设定固定数量的节点值后，每次到达当前设定值后到第二个设定值时,计算当前的所有数据微分后的均方差，以及微分零点附近加减dv的所用时间
# #### 评分参数
# - **静态评分** (static_score)
#   stable = sum( ( f(x) - avg( f(x) ) )**2 ) / n
#   static_score = 1 / (1 + pick*stable) * 1.0
# - **执行能力评分** (executable_score)
#   executable_score = react_time + response_time
# - **动态稳定性评分** (dynamic_stable_score)
#   df(x) = f(current_x) - f(prev_x)
#   stable = sum( ( df(x) - avg( df(x) ) )**2  ) / n
#   zero_time = sum( between(df(x), -dv, dv) ? time1 - time2:0)
#   dynamic_stable_score = 1 / (1 + zero_time*stable) * 1.0
# ------------------------------------------------------------


class BenchMark:
    def __init__(self):
        self.clear()

    def clear(self,set_data = SET_DATA,init_data = INIT_DATA):
        self.datas = []
        self.peak = 0
        self.set_data = set_data
        self.init_data = init_data
        self.expect_action_type = PASSBY_UP if set_data - init_data > 0 else PASSBY_DOWN
        self.online_rough_time = time.time()
        self.time_check_flags = {REACT:False, RESPONESE:False}
        self.sum_val = 0
        self.avg = 0
        self.sum_static_val = 0
        self.offset_execute = 0
        self.after_execute_len = 0

    # # offline means stop the machine than analyze data from database
    #   it should run on the server
    # def offline_analyze(self):
    #     pass

    # online judge process task like highly unstable or slow movement
    def online_update(self,data):
        self.prepare(data)
        self.datas.append(data)
        if not self.check_time():
            self.after_execute_len = len(self.datas) - self.offset_execute + 1
            self.lazy_sum(data)
            self.lazy_avg(data)

    def lazy_sum(self, data):
        self.sum_val += data

    def lazy_avg(self,data):
        self.avg = self.sum_val / self.after_execute_len
        self.sum_static_val += (data - self.avg)**2

    def check_time(self):
        return not self.time_check_flags[REACT] or not self.time_check_flags[RESPONESE]

    def get_peak(self,data):
        if self.expect_action_type == PASSBY_UP:
            self.peak = self.peak if data < self.peak else data
        else:
            self.peak = self.peak if data > self.peak else data

    def prepare(self,data):
        is_ready = False
        if self.check_time():
            where_is = self.check_pass_set_data(data)
            self.get_peak(data)
            if not self.time_check_flags[REACT] and self.expect_action_type == where_is:
                self.react_rough_time = time.time() - self.online_rough_time
                self.online_rough_time = time.time()
                self.time_check_flags[REACT] = True
            elif self.time_check_flags[REACT]:
                self.offset_execute = len(self.datas)
                self.response_rough_time = time.time() - self.online_rough_time
                self.time_check_flags[RESPONESE] = True
        else:
            is_ready = True
        return is_ready

    def check_pass_set_data(self,data):
        l = len(self.datas)
        if l < 2:
            return
        pre_data = self.datas[l-1]
        check1 = pre_data - self.set_data
        check2 = data - self.set_data
        passby = False
        if check1 <= 0 <= check2:
            passby = PASSBY_UP
        elif check2 <= 0 <= check1:
            passby = PASSBY_DOWN
        return passby

    # online judge
    # 越大越好
    def get_static_score(self):
        static_score = 0
        if not self.check_time():
            stable = self.sum_static_val / self.after_execute_len * 1.0
            static_score = 1.0 / (1 + abs(self.peak-self.set_data) + stable)
        return static_score


    def get_executable_score(self):
        executable_score = 0
        if not self.check_time():
            executable_score = self.react_rough_time + self.response_rough_time
        return executable_score


    # def get_dynamic_stable_score(self):
    #     pass

    def banch_settings(self):
        pass

    def run(self):
        pass
