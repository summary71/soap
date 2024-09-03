from __future__ import print_function
from datetime import datetime
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

def solution(m, k):
    # 모든 골드바의 분배를 저장하는 리스트를 초기화합니다.
    all_distributions = list(itertools.product(range(k), repeat=len(m)))

    # 최소 무게와 최대 무게의 차이를 최대로 설정합니다.
    min_difference = float('inf')

    for distribution in all_distributions:
        # 각 포대의 무게를 저장하는 리스트를 초기화합니다.
        weights = [0] * k
        for i in range(len(m)):
            # 골드바를 해당 포대에 추가합니다.
            weights[distribution[i]] += m[i]
        
        # 최소 무게와 최대 무게의 차이를 계산합니다.
        difference = max(weights) - min(weights)
        # 만약 이 차이가 현재의 최소 차이보다 작다면, 이 차이를 새로운 최소 차이로 설정합니다.
        if difference < min_difference:
            min_difference = difference
            print(weights, difference)

    return min_difference


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


