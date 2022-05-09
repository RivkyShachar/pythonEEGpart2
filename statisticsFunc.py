import statistics
from audioop import rms
import pandas as pd
import numpy as np
import scipy
from scipy.stats import iqr

NUM_OF_STATISTICS_FITURES = 10


def features(values):
    statisticsArr = [0] * NUM_OF_STATISTICS_FITURES
    statisticsArr[0] = min(values)
    statisticsArr[1] = statistics.variance(values)
    statisticsArr[2] = max(values)
    statisticsArr[3] = statistics.mean(values)
    statisticsArr[4] = pd.skew(values)
    statisticsArr[5] = np.percentile(values, 25)
    statisticsArr[6] = np.percentile(values, 50)
    statisticsArr[7] = iqr(values)
    statisticsArr[8] = scipy.stats.kurtosis(values)
    statisticsArr[9] = rms(values)
    return statisticsArr


'''
        CLIS_features(k,1) = min(CLIS_answers(j,1:end-1));
        CLIS_features(k,2) = var(CLIS_answers(j,1:end-1));
        CLIS_features(k,3) = max(CLIS_answers(j,1:end-1));
        CLIS_features(k,4) = mean(CLIS_answers(j,1:end-1));
        CLIS_features(k,5) = skewness(CLIS_answers(j,1:end-1));
        CLIS_features(k,6) = prctile(CLIS_answers(j,1:end-1),25);
        CLIS_features(k,7) = prctile(CLIS_answers(j,1:end-1),50);
        CLIS_features(k,8) = iqr(CLIS_answers(j,1:end-1));
        CLIS_features(k,9) = kurtosis(CLIS_answers(j,1:end-1));
        CLIS_features(k,10) = rms(CLIS_answers(j,1:end-1));
        CLIS_features(k,num_features)= CLIS_answers(j,end);
'''
