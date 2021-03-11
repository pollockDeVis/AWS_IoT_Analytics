# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 20:22:08 2021

@author: Pollock
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime
import time
import math

filename = "sparrow_"
min_rssi = -60.0
dev_dict = {}
total_devices = 20

dataset = pd.read_csv('wifi_diagnostics.csv')
trimmed_dataset =  dataset.iloc[:,[0,1,2]]

for i in range(1,total_devices):
    DeviceName =  filename + str(i)
    if i == 14:
        sparrow_14 = trimmed_dataset[trimmed_dataset['terminal'] == DeviceName]
    mean_rssi = (trimmed_dataset[trimmed_dataset['terminal'] == DeviceName]).mean()
    print(mean_rssi)
    dev_dict.update({DeviceName: mean_rssi[0] })
    #sparrow_9 = (trimmed_dataset[trimmed_dataset['terminal'] == "sparrow_9"])
    #print(math.floor(sparrow_9.mean()))
print(dev_dict)
keys = dev_dict.keys()
values = dev_dict.values()


#above_thres = np.maximum(dev_dict - min_rssi ,0)

#sparrow_6.sort_values(by = ['__dt'])
#sparrow_6.sort(key=lambda date: datetime.strptime(date, "%y-%m-%b"))
# x_axis = sparrow_6['__dt']
# y_axis = sparrow_6['wifi_rssi']
# plt.plot(x_axis, y_axis)
# print(sparrow_6)

# plt.bar(keys, values)
# plt.xticks(rotation='vertical')
# plt.axhline(y=min_rssi, linewidth=1, color='red')
#plt.hlines(min_rssi, xmin=-2, xmax=total_devices, linestyles='dashed')
#plt.plot( [-2, 20], [-55, -55], color='red')
plt.show()
# if dataset['terminal'] == 'sparrow_9':
#     sparrow
# for i in range(len(dataset)):
#     if dataset[i]['terminal'] == 'sparrow_9':
#         print(dataset[i]['wifi_rssi'])
    

