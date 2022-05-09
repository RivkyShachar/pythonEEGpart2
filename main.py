import fumc
NUM_OF_ELECTRODES=14

def readDataFromFile(file1,numOfQuestions=20):
    for i in range(numOfQuestions):
        for j in range(NUM_OF_ELECTRODES):
            data[i][j]=file1.readline()




def main(fileName,numOfQuestions=20):
    file1=open(fileName,'r')
    data=readDataFromFile(file1,numOfQuestions)
    file1.close()


if __name__ == '__main__':
    main(fileName,numOfQuestions)

# we have a file with the data
# read from the file and put the data in variables
# norm the data electrodes.
#
#
#
a = [1, 2, 3, 4][3, 4, 5, 6]
for i in range(2, 17):
    a = fumc.normy(a(i))
# read electrodes data
# arrange the data to elecrodes variables.
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
