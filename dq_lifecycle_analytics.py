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

dataset = pd.read_csv('lifecycle.csv')

#cash = dataset.iloc[:,1]
trimmed_ds = dataset.iloc[:,[0,1,2,3,6]] #.values

sparrow_1 = (trimmed_ds[trimmed_ds['clientid'] == "sparrow_14"])
#sparrow_2 = trimmed_ds[trimmed_ds['clientid'] == "sparrow_2"]
#sparrow_3 = trimmed_ds[trimmed_ds['clientid'] == "sparrow_3"]
#sparrow_test = trimmed_ds[trimmed_ds['clientid'] == "sparrow_test"]


sparrow_1['timestamp'] = pd.to_datetime(sparrow_1['timestamp'],  unit = 'ms')
#sparrow_2['timestamp'] = pd.to_datetime(sparrow_2['timestamp'],  unit = 'ms')
#sparrow_3['timestamp'] = pd.to_datetime(sparrow_3['timestamp'],  unit = 'ms')
#sparrow_test['timestamp'] = pd.to_datetime(sparrow_test['timestamp'],  unit = 'ms')

#sparrow_3.sort('timestamp', inplace = True)

sparrow_1['timestamp'] = datetime_from_utc_to_local(sparrow_1['timestamp'])
#sparrow_2['timestamp'] = datetime_from_utc_to_local(sparrow_2['timestamp'])
#sparrow_3['timestamp'] = datetime_from_utc_to_local(sparrow_3['timestamp'])
#sparrow_test['timestamp'] = datetime_from_utc_to_local(sparrow_test['timestamp'])

# connection_encoder(sparrow_1)
# connection_encoder(sparrow_2)
# connection_encoder(sparrow_3)




# sns.set_style("whitegrid")
# plt.rc('xtick', labelsize=15) 
# plt.rc('ytick', labelsize=15) 

# fig, ax = plt.subplots(figsize=(15, 6))
# # d = data[data['obs_id']==2]
# sns.lineplot(sparrow_1['timestamp'], sparrow_1['eventtype'] )

# ax.set_title('Salinity over Time', fontsize = 20, loc='center', fontdict=dict(weight='bold'))
# ax.set_xlabel('Year', fontsize = 16, fontdict=dict(weight='bold'))
# ax.set_ylabel('Salinity', fontsize = 16, fontdict=dict(weight='bold'))
# plt.tick_params(axis='y', which='major', labelsize=16)
# plt.tick_params(axis='x', which='major', labelsize=16)
# plt.rc('font', size=12)
# fig, ax = plt.subplots(figsize=(50, 10))

# # Specify how our lines should look
# ax.plot(sparrow_1.timestamp, sparrow_1.eventtype, color='tab:orange')

# # Same as above
# ax.set_xlabel('Time')
# ax.set_ylabel('Connection')
# ax.set_title('LifeCycle')
# ax.grid(True)
# ax.legend(loc='upper left');



# # Helpers to format and locate ticks for dates
# from matplotlib.dates import DateFormatter, DayLocator

# # Set the x-axis to do major ticks on the days and label them like '07/20'
# ax.xaxis.set_major_locator(DayLocator())
# ax.xaxis.set_major_formatter(DateFormatter('%Y/%m/%d %X'))


#le = LabelEncoder()
# for i in range(len(sparrow_1)):
#     sparrow_1[i]['eventtype']  = connection_encoder(sparrow_1[i]['eventtype']) #le.fit_transform(sparrow_1['eventtype'])
# #sparrow_1['timestamp'] = sparrow_1['timestamp'].dt.tz_localize('Asia/Kuala_Lumpur')
#sparrow_1['timestamp']= sparrow_1['timestamp'].dt.tz_convert(tz = 'Asia/Kuala_Lumpur')

#sparrow_1['timestamp'] = datetime_from_utc_to_local(sparrow_1['timestamp'])
#sparrow_1['timestamp'] = sparrow_1.['timestamp'].transform(lambda x: x.dt.tz_localize(x.name))
#tz_convert('Asia/Shanghai')
# if re.match(r'^sparrow', ds[0]):
#     print(ds[ds[0]])
    
    
#trimmed_ds = trimmed_ds[trimmed_ds['clientid'].startswith("sparrow")]
#filtered_ds = []
#for i in range(0, len(trimmed_ds)):
    #print(i)
    #print(len(trimmed_ds))
    #temp_str = str(trimmed_ds[i,0])
    #if temp_str.startswith("sparrow"):
        #filtered_ds = trimmed_ds[i].transpose()
       # print(trimmed_ds[i,0])
       
# result_s=pd.to_datetime(timestamps,unit='ms')
# actual_date = datetime_from_utc_to_local(result_s)
# print(actual_date)

#dt = actual_date + cash
