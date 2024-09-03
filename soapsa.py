import time
import sys
import math
import json
import os
import random
import numpy as np
from re import sub

import copy

import itertools


def evaluate (m, k, sol):
    weight = [0] * k
    for i in range(len(m)):
        weight[sol[i]] += m[i]

    return max(weight) - min(weight)
                                                                                                                                                                                                            
def solution(m, k):
    bestdist = [i % k for i in range(len(m))]
    bestval = evaluate (m, k, bestdist)

    T = 60
    a1 = 5.0
    cur = bestdist
    while(T > 1e-5):
        tmp = copy.deepcopy(cur)
        for rep in range(100):
            i = random.randrange(0, len(m))
            j = random.randrange(0, k)
            tmp[i] = j
            curval = evaluate (m, k, cur)
            tmpval = evaluate (m, k, tmp)
            if curval > tmpval:
                 cur[i] = j
            elif(math.exp((curval - tmpval) / (a1 * T)) > random.uniform(0, 1)):
                cur[i] = j
            else:
                tmp[i] = cur[i]
            if bestval > tmpval:
              bestdist = copy.deepcopy(tmp)
              bestval = tmpval

        T *= 0.99

    return bestval


def WriteCase(m, k, result, cnt):
  tfname = "case" + "%02d"%(cnt) + ".txt"
  f = open(tfname, 'w')
  a = str(m) + "," + str(k) + "\n" 
  f.write (a)
  f.close()

  sfname = "sol" + "%02d"%(cnt) + ".txt"
  f = open(sfname, 'w')
  f.write (str(result) + "\n")
  f.close()

m = [1,4,2,5]
k = 2
seq = 99
print("scene ", seq)
result = solution(m, k)
WriteCase(m, k, result, seq)

m = [2,1,4,5,3,1]
k = 3
seq = 98
print("scene ", seq)
result = solution(m, k)
WriteCase(m, k, result, seq)

sval = 0
random.seed(sval)

seqst = sval * 10 + 1
for k in range(10):
  seq = seqst + k
  print(seq)
  random.seed(seq)
  n = random.randrange(6, 12)
  m = [random.randrange(10, 50) for i in range(n)]
  k = min(random.randrange(3, 5), int(n/2))
  print("scene ", seq)
  result = solution(m, k)
  WriteCase(m, k, result, seq)


