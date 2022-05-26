import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

x = 1  # bool
y = 1  # bool
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

fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=400, interval=20, blit=True)
anim.resume()

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
#anim.save('basic_animation.mp4', fps=30)

#plt.show()

