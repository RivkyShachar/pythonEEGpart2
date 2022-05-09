import LDAfunc
import statisticsFunc

import fastica

import fumc

NUM_OF_ELECTRODES = 14
NUM_OF_VALUES_FOR_EACH_ELEC = 512


def readDataFromFileAndNormy(file1, numOfQuestions=20):
    data = [[[]] * NUM_OF_ELECTRODES] * numOfQuestions
    for i in range(numOfQuestions):
        for j in range(NUM_OF_ELECTRODES):
            data[i][j] = file1.readline()
            data[i][j] = fumc.normy(data[i][j])
    return data


def callFastICA(data, numOfQuestions=20):
    for i in range(numOfQuestions):
        data[i] = data[i]  # need to do here fast ica
    return data


def statisticalFeatures(data, numOfQuestions=20):
    for i in range(numOfQuestions):
        for j in range(NUM_OF_ELECTRODES):
            data[i][j] = statisticsFunc.features(data[i][j])

def callLDA(data, numOfQuestions=20):
    for i in range(numOfQuestions):
        for j in range(NUM_OF_ELECTRODES):
            data[i][j] = LDAfunc.doLDA(data[i][j])


def main(fileName, numOfQuestions=20):
    file1 = open(fileName, 'r')
    data = readDataFromFileAndNormy(file1)
    file1.close()
    data = callFastICA(data)
    data=statisticalFeatures(data)


if __name__ == '__main__':
    fileName = "recording.csv"
    main(fileName)
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
