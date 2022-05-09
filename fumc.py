from statisticsFunc import mean

from numpy import std


def normy(a):
    return list(map(lambda x: (x - mean(a)) / std(a), a))

