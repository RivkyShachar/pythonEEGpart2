import numpy as np
import sklearn



def doLDA(values):
    xxx = np.array(values)
    yyy = np.array(values)
    val = sklearn.lda.LDA()
    val.fit(xxx,yyy)
    return val


'''
 %% FLDA (not as classifier) 
  acc_m = zeros(num_electrodes,1);
%yyy=round(rand(num_question,1));
max_elecs = 14; % how many dementions we will need. 
projected_lines_data = zeros(num_question,num_electrodes);
max_indexs = zeros(1,max_elecs);
checking_number = zeros(num_electrodes,1);

for electrode_index = 1:num_electrodes
    electroda = electrode_index;
    xxx = CLIS_features(electroda:num_electrodes:end,1:end-1);
    yyy = CLIS_features(electroda:num_electrodes:end,end:end);
    [projected_line M_struct(electrode_index)] = lda2(xxx,yyy);
    projected_lines_data(:,electrode_index) = projected_line;
'''