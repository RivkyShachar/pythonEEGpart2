from statistics import mean

import numpy as np
import pandas
import pandas as pd
from numpy import std


'''def normy(a):
    return list(map(lambda x: (x - mean(a)) / std(a), a))
'''
import numpy as np

def normy(a):
  b = (a-np.mean(a))/(np.std(a))
  return b

a=[[5,5,5,5,5],[6,7,8,9,9],[2,2,2,2,2]]
arr=np.array(a,dtype=float)
print(arr)
print(normy(arr[:,1]))
print(arr)
print("----------")
arr.astype(float)
b = np.array(normy((arr[:, 1])))
arr[:,1]=b
print(arr.astype(float))



# import csv
# col_list=["AF3", "F7", "F3", "FC5", "T7", "P7", "O1", "O2", "P8", "T8", "FC6", "F4", "F8", "AF4"]
# filename = open('EEGLogger.csv', 'r')
# data = [[[]] * 14] * 20
# # creating dictreader object
# file = csv.DictReader(filename)
#
# # creating empty lists
#
#
# # iterating over each row and append
# # values to empty list
# for col in file:
#   data[0][0].append(col['Timestamp'])
#   #data[0][1].append(col[col_list[1]])
