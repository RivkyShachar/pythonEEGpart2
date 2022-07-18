import LDAfunc
import statisticsFunc

import fastica

import fumc

import numpy as np
import pandas as pd
#import seaborn as sns
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

NUM_OF_ELECTRODES = 14
NUM_OF_VALUES_FOR_EACH_ELEC = 512


def readDataFromFileAndNormy(file1, numOfQuestions=20):
    I = pd.read_csv(file1, skiprows=1,header=None)# skiprows=1 reads from row 1
    data=I.iloc[:,3:17]
    data = np.array(data, dtype=float)  # reads all the rows from column 3 till 17
    print(data.shape) #gives me the dimensions of hte matrix
    for x in range(0, data.shape[0], NUM_OF_VALUES_FOR_EACH_ELEC): #data.shape[0] is how many rows there are, meaning how many questions. every question has 512 electrodes, we do the normy for every question separately
        for i in range(data.shape[1]): # loop to do the normy for all the electordes
            data[x:x+NUM_OF_VALUES_FOR_EACH_ELEC,i]=fumc.normy(data[x:x+NUM_OF_VALUES_FOR_EACH_ELEC,i])
    # datawrite=pd.DataFrame(data,columns=['AF3', 'F7', 'F3', 'FC5', 'T7', 'P7', 'O1', 'O2', 'P8', 'T8', 'FC6', 'F4', 'F8', 'AF4']) # change the array to data frame format in order to wrtie to csv file
    # datawrite.to_csv('checkEEG.csv',index=False,na_rep='Unknown')# write to s csv file
    # LI=pd.read_csv('checkEEG.csv')
    # print(LI)





    # print(data[:,0])
    # data[:,0]=fumc.normy(data[:,0])
    # print(data[:,0])
    '''data = [[[]] * NUM_OF_ELECTRODES] * numOfQuestions
    next(file1)
    for i in range(numOfQuestions):
        for j in range(NUM_OF_ELECTRODES):
            data[i][j] = file1.readline()[3:17]
            #data[i][j] = fumc.normy(data[i][j])'''
    '''for i in range(NUM_OF_ELECTRODES):
        print(i)
        data[:, i] = fumc.normy(data[:, i])
        print(i+'1')'''
    return data


def callFastICA(data, numOfQuestions=20):
    # np.isnan(data).any()
    # np.isinf(data).any()
    for x in range(0, data.shape[0], NUM_OF_VALUES_FOR_EACH_ELEC):
        data[x:x+NUM_OF_VALUES_FOR_EACH_ELEC,:] = fastica.doFastICA(data[x:x+NUM_OF_VALUES_FOR_EACH_ELEC,:])  # need to do here fast ica
    return data



def statisticalFeatures(data, numOfQuestions=20):
    for x in range(0, data.shape[0], NUM_OF_VALUES_FOR_EACH_ELEC):
        for j in range(NUM_OF_ELECTRODES):
            data[x:x+NUM_OF_VALUES_FOR_EACH_ELEC,j] = statisticsFunc.features(data[x:x+NUM_OF_VALUES_FOR_EACH_ELEC,j])
            #problem that it gets an array of 10, and supposed to fit in place of 512

def callLDA(data, numOfQuestions=20):
    for i in range(numOfQuestions):
        for j in range(NUM_OF_ELECTRODES):
            data[i][j] = LDAfunc.doLDA(data[i][j])


def main(fileName, numOfQuestions=20):
    print('41')
    file1 = open(fileName, 'r')
    print('43')
    data = readDataFromFileAndNormy(file1)
    print('45')
    file1.close()
    print('47')
    data = callFastICA(data)
    print('49')
    data=statisticalFeatures(data)
    print('51')
    #data=LDAfunc()
    #data=SVMfunc()
    return data


if __name__ == '__main__':
    #doFirsPartOfTheProject read 20 questions
    fileName = "EEGLogger.csv"
    theRange=main(fileName)
    #now we start recording every question seperatlly
    #on every question we record and put it in an other file
    #then we read from that file and do fastICA on this question
    #then do if



"""
# we have a file with the data
# read from the file and put the data in variables
# norm the data electrodes.
#
#
#
# read electrodes data
# arrange the data to elecrodes variables.
"""

"""
AF3 = a[3]
F7 = a[4]
F3 = a[5]
FC5 = a[6]
T7 = a[7]
P7 = a[8]
O1 = a[9]
O2 = a[10]
P8 = a[11]
T8 = a[12]
FC6 = a[13]
F4 = a[14]
F8 = a[15]
AF4 = a[16]
elecName = ["AF3", "F7", "F3", "FC5", "T7", "P7", "O1", "O2", "P8", "T8", "FC6", "F4", "F8", "AF4"]
elec_arr = [AF3, F7, F3, FC5, T7, P7, O1, O2, P8, T8, FC6, F4, F8, AF4]
NumOfRunning = 20
PoR_train_avg = [0]*NumOfRunning
PoR_test_avg = [0]*NumOfRunning
for i in range(NumOfRunning):
    num_electrodes = 14
    PoR_flag = 1
    while (PoR_flag)
        [CLIS_ica(:,:), W, T] = fastICA(elec_arr(:,:), num_electrodes, 'kurtosis', 1);
        elec_arr = CLIS_ica;
        % [NoE, len] = size(elec_arr);
        % for ww = 1:NoE
        % elec_arr(ww,:) = dwt(elec_arr(ww,:), 'sym4');
        % end
        % % arrange
        data
        % indecies
        of
        marker
        non - zero
        index1 = (find(marker~=0))';
        val_marker = marker(index1);
"""

'''
%% Statistical features extraction 
num_features = 10; 
num_question_eff = num_question;
CLIS_features = zeros(num_question_eff*num_electrodes,num_features);
j=1;
k=1;
for i=1:num_question_eff*num_electrodes
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
        k=k+1;
        j=j+1;
'''
