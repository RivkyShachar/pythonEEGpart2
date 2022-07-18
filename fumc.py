from statistics import mean

import numpy as np
import pandas
import pandas as pd
from numpy import std


'''def normy(a):
    return list(map(lambda x: (x - mean(a)) / std(a), a))
'''
def normy(a):
  if np.std(a)==0.0:#if all the values are the same std==0
    b=a-np.mean(a)
  else:
    b = (a-np.mean(a))/(np.std(a))
  return b



import csv
col_list=["AF3", "F7", "F3", "FC5", "T7", "P7", "O1", "O2", "P8", "T8", "FC6", "F4", "F8", "AF4"]
filename = open('EEGLogger.csv', 'r')
data = [[[]] * 14] * 20
# creating dictreader object
file = csv.DictReader(filename)

# creating empty lists


# iterating over each row and append
# values to empty list
for col in file:
  data[0][0].append(col['Timestamp'])
  #data[0][1].append(col[col_list[1]])
