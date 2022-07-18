import numpy as np
import pandas as pd

from scipy.stats import skew
from scipy.stats import kurtosis
from sklearn.decomposition import FastICA
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix
import math
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier
from matplotlib import pyplot

def doFastICA(EEG_data):
    ica = FastICA(n_components=14,tol=0.1)
    EEG_data = ica.fit_transform(EEG_data)  # Reconstruct signals
    mixing_matrix = ica.mixing_  # Get estimated mixing matrix
    return EEG_data


