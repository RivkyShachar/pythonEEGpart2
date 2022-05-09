
from statistics import mean

from numpy import std


def normy(a):
    return (a - mean(a)) / std(a)
