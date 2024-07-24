from lib.graph import Graph
from lib.matrix import *
from lib.cube import *
from lib.algorithms import *
from lib.divisor import Divisor
import numpy as np
import math


d = {}

with open("data.txt","r") as f:
    key =2
    for line in f:
        if line == "\n":
            break
        d[key] = line.strip().strip("[]").split(", ")
        
        for i in range(len(d[key])):
            d[key][i] = int(d[key][i])
        key += 1


for i in range(len(d.items())-4):
    l = d[i+2]
    print(l)
    print(math.gcd(*l))