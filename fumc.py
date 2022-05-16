from statistics import mean

import numpy as np
from numpy import std


'''def normy(a):
    return list(map(lambda x: (x - mean(a)) / std(a), a))
'''
def normy(a):
  b = (a-np.mean(a))/(np.std(a))
  return b
