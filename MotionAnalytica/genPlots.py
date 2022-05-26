import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

x = 1  # bool
column_x = 'accelerometerAccelerationX(G)'
column_y = 'accelerometerAccelerationY(G)'
column_z = 'accelerometerAccelerationZ(G)'
timestamp = 'accelerometerTimestamp_sinceReboot(s)'
x_min = 0
x_max = 8
y_min = -30
y_max = 15

mode = 1  # 1 is acceleleration, 2 is speed, 3 is distance

while x == 1:
    folder = input('Welcher Ordner soll verwendet werden werden? ')
    dirPath = "../data/" + folder + "/csv/"
    plotDirPath = "../data/" + folder + "/plot/"
    if not os.path.isdir(dirPath):
        print("Ordner existiert nicht")
    else:
        x = 0
    files = os.listdir(dirPath)
    print(files)

"""plt.plot(df[timestamp], df['Linear Acceleration x (m/s^2)'], label='x')
plt.plot(df[timestamp], df['Linear Acceleration y (m/s^2)'], label='y')
plt.plot(df[timestamp], df['Linear Acceleration z (m/s^2)'], label='z')"""

"""trapz = np.trapz(df[timestamp], df['accelerometerAccelerationX(G)'])
print(f'{-trapz:.2f}')"""
filecount = 0

for file in files:
    filecount += 1
    filePath = dirPath + file
    if os.path.isfile(filePath):
        df = pd.read_csv(filePath)
        #df.info()
        x = 0
    else:
        print("Falscher Dateinname")


    # df['time_diff'] = np.diff(df[timestamp][0:len(df)-1])
    df[timestamp] = df[timestamp] - df[timestamp][0]


    if mode == 1:
        modus = "Beschleunigung"
        plt.title(modus + ": " + file)
        plt.plot(df[timestamp], df[column_x], label='x')
        plt.plot(df[timestamp], df[column_y], label='y')
        plt.plot(df[timestamp], df[column_z], label='z')
    else:
        ##erste Integration
        df['geschw_x'] = np.cumsum(df[column_x] * (df[timestamp][1] - df[timestamp][0]))
        df['geschw_y'] = np.cumsum(df[column_y] * (df[timestamp][1] - df[timestamp][0]))
        df['geschw_z'] = np.cumsum(df[column_z] * (df[timestamp][1] - df[timestamp][0]))

        if mode == 2:
            modus = "Geschwindigkeit"
            plt.title(modus + ": " + file)
            plt.plot(df[timestamp], df['geschw_x'], label='x')
            plt.plot(df[timestamp], df['geschw_y'], label='y')
            plt.plot(df[timestamp], df['geschw_z'], label='z')
        else:
            ##zweite Integration
            df['dist_x'] = np.cumsum(df['geschw_x'] * (df[timestamp][1] - df[timestamp][0]))
            df['dist_y'] = np.cumsum(df['geschw_y'] * (df[timestamp][1] - df[timestamp][0]))
            df['dist_z'] = np.cumsum(df['geschw_z'] * (df[timestamp][1] - df[timestamp][0]))

            modus = "Distanz"
            plt.title(modus + ": " + file)
            plt.plot(df[timestamp], df['dist_x'], label='x')
            plt.plot(df[timestamp], df['dist_y'], label='y')
            plt.plot(df[timestamp], df['dist_z'], label='z')

    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)

    plt.legend()

    if not os.path.isdir(plotDirPath):
        os.mkdir(plotDirPath)
        print("Plot-Ordner erstellt: " + plotDirPath)
    plotPath = plotDirPath + file[:-4] + "_" + modus + ".png"
    plt.savefig(plotPath)
    if os.path.isfile(plotPath):
        print(str(filecount) + ": Plot erfolgreich gespeichert!")

    #plt.show() #includes plt.close()
    plt.close()
