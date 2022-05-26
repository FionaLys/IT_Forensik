import os

x = 1
path = ""

while x == 1:
    try:
        folder = input('Welcher Ordner soll gelabelt werden? ')
        path = "../data/" + folder + "/csv/"
        print(path, "ist Pfad: ", os.path.isdir(path))
        x = 0
    except:
        print("Ordner konnte nicht gefunden werden!")

files = os.listdir(path)
print("Die folgenden Dateien sind vorhanden: ", files)

mode = int(input('Welche Datei soll umbenannt werden? (0 für alle, ansonsten Nummer angeben) '))
person = input('Wer hat geworfen? ')
frequency = input('Welche Frequenz wurde verwendet (in Hz)? ')

if mode == 0:
    print("Es werden alle Dateien umbenannt!")
    number = 0
    for file in files:
        number += 1
        oldFilePath = path + file
        distance = input(str(number) + ': Wie weit wurde geworfen (in cm)? ')
        newFilePath = path + str(number) + "_" + person + "_" + distance + "cm_" + frequency + "Hz.csv"
        os.rename(oldFilePath, newFilePath)
        print(newFilePath)
else:
    number = mode #10 ist vor 1
    file = files[number]
    oldFilePath = path + file
    print("Es wird ", oldFilePath, " umbenannt.")
    distance = input(str(number) + ': Wie weit wurde geworfen (in cm)? ')
    newFilePath = path + str(number) + "_" + person + "_" + distance + "cm_" + frequency + "Hz.csv"
    os.rename(oldFilePath, newFilePath)
    print(newFilePath)


print("Alle Dateien wurden umbenannt!")