import matplotlib.pyplot as plt
from matplotlib import cm
import random

class Graph:
    def __init__(self):
        self.colors = ['r','b','g','y','c','k']


    def draw(self, datas):
        plt.title('pid angle tune graph')
        plt.xlabel('time(ms)')
        plt.ylabel('angle')

        for lx,ly,label in datas:
            plt.plot(lx, ly, random.choice(self.colors),label=label)

        # plt.xticks(lx, lx, rotation=0)

        plt.legend(bbox_to_anchor=[0.3, 1])
        plt.grid()
        plt.show()
