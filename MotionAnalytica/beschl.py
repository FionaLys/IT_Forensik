import math

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import os

x = 1  # bool
y = 1  # bool
column_x = 'accelerometerAccelerationX(G)'
column_y = 'accelerometerAccelerationY(G)'
column_z = 'accelerometerAccelerationZ(G)'
timestamp = 'accelerometerTimestamp_sinceReboot(s)'

mode = 1  # 1 is acceleleration, 2 is speed, 3 is distance

while x == 1:
    while y == 1:
        folder = input('Welcher Ordner soll verwendet werden werden? ')
        dirPath = "../data/" + folder + "/csv/"
        plotDirPath = "../data/" + folder + "/plot/"
        if not os.path.isdir(dirPath):
            print("Ordner existiert nicht")
        else:
            y = 0
    files = os.listdir(dirPath)
    print(files)
    bez = input('Welche Datei sollen verwendet werden (Nummer der Datei)? ')
    file = files[int(bez) - 1]
    print(file)
    filePath = dirPath + file;
    if os.path.isfile(filePath):
        df = pd.read_csv(filePath)
        df.info()
        x = 0
    else:
        print("Falscher Dateinname")
"""plt.plot(df[timestamp], df['Linear Acceleration x (m/s^2)'], label='x')
plt.plot(df[timestamp], df['Linear Acceleration y (m/s^2)'], label='y')
plt.plot(df[timestamp], df['Linear Acceleration z (m/s^2)'], label='z')"""

"""trapz = np.trapz(df[timestamp], df['accelerometerAccelerationX(G)'])
print(f'{-trapz:.2f}')"""

##erste Integration
df['geschw_x'] = np.cumsum(df[column_x] * (df[timestamp][1] - df[timestamp][0]))
df['geschw_y'] = np.cumsum(df[column_y] * (df[timestamp][1] - df[timestamp][0]))
df['geschw_z'] = np.cumsum(df[column_z] * (df[timestamp][1] - df[timestamp][0]))

##zweite Integration
df['dist_x'] = np.cumsum(df['geschw_x'] * (df[timestamp][1] - df[timestamp][0]))
df['dist_y'] = np.cumsum(df['geschw_y'] * (df[timestamp][1] - df[timestamp][0]))
df['dist_z'] = np.cumsum(df['geschw_z'] * (df[timestamp][1] - df[timestamp][0]))

# df['time_diff'] = np.diff(df[timestamp][0:len(df)-1])

if mode == 1:
    modus = "Beschleunigung"
    plt.plot(df[timestamp], df[column_x], label='x')
    plt.plot(df[timestamp], df[column_y], label='y')
    plt.plot(df[timestamp], df[column_z], label='z')
elif mode == 2:
    modus = "Geschwindigkeit"
    plt.title(modus + ": " + file)
    plt.plot(df[timestamp], df['geschw_x'], label='x')
    plt.plot(df[timestamp], df['geschw_y'], label='y')
    plt.plot(df[timestamp], df['geschw_z'], label='z')
else:
    modus = "Distanz"
    plt.title(modus + ": " + file)
    plt.plot(df[timestamp], df['dist_x'], label='x')
    plt.plot(df[timestamp], df['dist_y'], label='y')
    plt.plot(df[timestamp], df['dist_z'], label='z')

plt.legend()
plt.show()

if input('Speichern? ') == 'J':
    if not os.path.isdir(plotDirPath):
        os.mkdir(plotDirPath)
        print("Plot-Ordner erstellt: " + plotDirPath)
    plotPath = plotDirPath + file[:-4] + "_" + modus + ".png"
    plt.savefig(plotPath)
    if os.path.isfile(plotPath):
        print("Plot erfolgreich gespeichert!")
else:
    print("Plot wird nicht gespeichert!")
