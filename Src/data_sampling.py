import numpy as np
import pandas as pd
import csv
from random import shuffle
from sklearn.datasets import make_classification
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
from collections import Counter



# # Reading Data


data  = pd.read_csv('Data_processed/dataset.csv',sep=',',names=['Msg','Tag'])
data1 = pd.read_csv('Data_processed/dataset_POS.csv',sep=',',names=['Msg','Tag'])
data2 = pd.read_csv('Data_processed/dataset_stemmed.csv',sep=',',names=['Msg','Tag'])



data.dropna(inplace=True)

data1.dropna(inplace=True)

data2.dropna(inplace=True)



data_X = data['Msg'].to_numpy()
data_Y = data['Tag'].to_numpy()
data1_X = data1['Msg'].to_numpy()
data1_Y = data1['Tag'].to_numpy()
data2_X = data2['Msg'].to_numpy()
data2_Y = data2['Tag'].to_numpy()


data_X  = np.reshape(data_X, (data_X.shape[0],1))
data_Y  = np.reshape(data_Y, (data_Y.shape[0],1))
data1_X = np.reshape(data1_X, (data1_X.shape[0],1))
data1_Y = np.reshape(data1_Y, (data1_Y.shape[0],1))
data2_X = np.reshape(data2_X, (data2_X.shape[0],1))
data2_Y = np.reshape(data2_Y, (data2_Y.shape[0],1))


# # Without POS + Stemming

# ## Random Oversampling



ros = RandomOverSampler()
data_os_Msg, data_os_Tag = ros.fit_sample(data_X, data_Y)



# ## Random Undersampling


ros = RandomUnderSampler()
data_us_Msg, data_us_Tag = ros.fit_sample(data_X, data_Y)


# # POS

# ## Random Oversampling

# In[33]:


ros1 = RandomOverSampler()
data1_os_Msg, data1_os_Tag = ros1.fit_sample(data1_X, data1_Y)


# ## Random Undersampling


ros1 = RandomUnderSampler()
data1_us_Msg, data1_us_Tag = ros1.fit_sample(data1_X, data1_Y)



# # POS + Stemming

# ## Random Oversampling

ros2 = RandomOverSampler()
data2_os_Msg, data2_os_Tag = ros2.fit_sample(data2_X, data2_Y)



print(Counter(data2_os_Tag))


# ## Random Undersampling


ros2 = RandomUnderSampler()
data2_us_Msg, data2_us_Tag = ros2.fit_sample(data2_X, data2_Y)


def write_to_csv(file, msg, tag):
    msg = msg.reshape(msg.shape[0],1)
    tag = tag.reshape(tag.shape[0],1)
    sample_data = np.hstack((msg,tag)).tolist()
    shuffle(sample_data)
    fields = ['Msg','Tag']
    with open(file, 'w') as handle:
        csvwriter = csv.writer(handle)
        csvwriter.writerow(fields)
        for row in sample_data:
            csvwriter.writerow(row)
    pass




write_to_csv("Data_over_sampled/dataset_normal.csv",data_os_Msg, data_os_Tag)
write_to_csv("Data_over_sampled/dataset_POS.csv",data1_os_Msg, data1_os_Tag)
write_to_csv("Data_over_sampled/dataset_stemmed.csv",data2_os_Msg, data2_os_Tag)
write_to_csv("Data_under_sampled/dataset_normal.csv",data_us_Msg, data_us_Tag)
write_to_csv("Data_under_sampled/dataset_POS.csv",data1_us_Msg, data1_us_Tag)
write_to_csv("Data_under_sampled/dataset_stemmed.csv",data2_us_Msg, data2_us_Tag)

