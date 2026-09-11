import dpdata 
import numpy as np
#data = dpdata.LabeledSystem('./relaxation', fmt = 'cp2k/aimd_output') 
data = dpdata.LabeledSystem("./relaxation", cp2k_output_name="aimd.out", fmt="cp2kdata/md")
print('# the data contains %d frames' % len(data))           #输出OUTCAR数据文件包含的帧数，这里从屏幕输出可以看出是200帧
index_validation = np.random.choice(len(data),size=40,replace=False) #随机选取40帧作为验证数据，其余为训练数据
index_training = list(set(range(len(data)))-set(index_validation))
data_training = data.sub_system(index_training)
data_validation = data.sub_system(index_validation)
data_training.to_deepmd_npy('training_data')
data_validation.to_deepmd_npy('validation_data')
print('# the training data contains %d frames' % len(data_training)) 
print('# the validation data contains %d frames' % len(data_validation))
