# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 00:02:34 2020

@author: Pollock
"""

import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import time

def datetime_from_utc_to_local(utc_datetime):
    now_timestamp = time.time()
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    return utc_datetime + offset

def connection_encoder(arr):
    for i in range(0, len(arr)):
        if arr.iloc[i, 2] == 'connected':
            arr.iloc[i, 2] = 1
        elif arr.iloc[i, 2] == 'disconnected': 
            arr.iloc[i, 2] = 0

dataset = pd.read_csv('cash.csv')

#cash = dataset.iloc[:,1]
trimmed_ds = dataset.iloc[:,[0,1,2,3,4]] #.values

sparrow_1 = (trimmed_ds[trimmed_ds['terminal'] == "sparrow_9"])
sparrow_2 = trimmed_ds[trimmed_ds['terminal'] == "sparrow_8"]
sparrow_3 = trimmed_ds[trimmed_ds['terminal'] == "sparrow_7"]



sparrow_1['timestamp'] = pd.to_datetime(sparrow_1['timestamp'],  unit = 's')
sparrow_2['timestamp'] = pd.to_datetime(sparrow_2['timestamp'],  unit = 's')
sparrow_3['timestamp'] = pd.to_datetime(sparrow_3['timestamp'],  unit = 's')

sparrow_1['timestamp'] = datetime_from_utc_to_local(sparrow_1['timestamp'])
sparrow_2['timestamp'] = datetime_from_utc_to_local(sparrow_2['timestamp'])
sparrow_3['timestamp'] = datetime_from_utc_to_local(sparrow_3['timestamp'])