# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 22:23:47 2021

@author: Pollock
"""

import pandas as pd
from datetime import datetime
import time

def datetime_from_utc_to_local(utc_datetime):
    now_timestamp = time.time()
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    return utc_datetime + offset


dataset = pd.read_csv('online_transaction.csv')

