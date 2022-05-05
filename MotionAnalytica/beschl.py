import math

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

x = 1 #bool
column_x = 'accelerometerAccelerationX(G)'
column_y = 'accelerometerAccelerationY(G)'
column_z = 'accelerometerAccelerationZ(G)'
timestamp = 'accelerometerTimestamp_sinceReboot(s)'

mode = 1 #1 is acceleleration, 2 is speed, 3 is distance


data_ = ["1_Ole_1250cm_30Hz.csv",
         "2_Ole_1400cm_100Hz.csv",
         "3_Ole_600cm_100Hz.csv",
         "4_Ole_600cm_100Hz.csv",
         "5_Ole_1700cm_100Hz.csv",
         "6_Ole_1600cm_100Hz.csv"]
data = ["../data/2022_05_05_firstTry/csv/" + x for x in data_]

while x == 1:
    try:
        """bez = input('Welche Daten sollen verwendet werden? ') + ".csv"""""
        bez = input('Welche Daten sollen verwendet werden? ')
        file = data[int(bez)-1]
        print(file)
        df = pd.read_csv(file)
        df.info()
        x = 0
    except:
        print("Falscher Dateiname")

"""plt.plot(df[timestamp], df['Linear Acceleration x (m/s^2)'], label='x')
plt.plot(df[timestamp], df['Linear Acceleration y (m/s^2)'], label='y')
plt.plot(df[timestamp], df['Linear Acceleration z (m/s^2)'], label='z')"""

"""trapz = np.trapz(df[timestamp], df['accelerometerAccelerationX(G)'])
print(f'{-trapz:.2f}')"""


##erste Integration
df['geschw_x'] = np.cumsum(df[column_x]*(df[timestamp][1]-df[timestamp][0]))
df['geschw_y'] = np.cumsum(df[column_y]*(df[timestamp][1]-df[timestamp][0]))
df['geschw_z'] = np.cumsum(df[column_z]*(df[timestamp][1]-df[timestamp][0]))

##zweite Integration
df['dist_x'] = np.cumsum(df['geschw_x']*(df[timestamp][1]-df[timestamp][0]))
df['dist_y'] = np.cumsum(df['geschw_y']*(df[timestamp][1]-df[timestamp][0]))
df['dist_z'] = np.cumsum(df['geschw_z']*(df[timestamp][1]-df[timestamp][0]))

#df['time_diff'] = np.diff(df[timestamp][0:len(df)-1])

if mode == 1:
    plt.title("Beschleunigung: " + file)
    plt.plot(df[timestamp], df[column_x], label='x')
    plt.plot(df[timestamp], df[column_y], label='y')
    plt.plot(df[timestamp], df[column_z], label='z')
elif mode == 2:
    plt.title("Geschwindigkeit: " + file)
    plt.plot(df[timestamp], df['geschw_x'], label='x')
    plt.plot(df[timestamp], df['geschw_y'], label='y')
    plt.plot(df[timestamp], df['geschw_z'], label='z')
elif mode == 3:
    plt.title("Distanz: " + file)
    plt.plot(df[timestamp], df['dist_x'], label='x')
    plt.plot(df[timestamp], df['dist_y'], label='y')
    plt.plot(df[timestamp], df['dist_z'], label='z')


plt.legend()
plt.show()
