from tkinter import *
import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud
from stop_words import get_stop_words

# Stopwords festlegen
stop_words = get_stop_words('german')
stopwords = ['nan', '|', 'Gelesen'] + list(stop_words)

# Importieren der Csv-Dateien mit den Daten
messages_huberta = pd.read_csv('messages_huberta.csv', on_bad_lines='skip')
gesuchte_elemente_huberta = pd.read_csv('gesuchte_elemente_huberta.csv', on_bad_lines='skip')
webverlauf_huberta = pd.read_csv('webverlauf_huberta.csv', on_bad_lines='skip')
messages_siegfried = pd.read_csv('messages_siegfried.csv', on_bad_lines='skip')
gesuchte_elemente_siegfried = pd.read_csv('gesuchte_elemente_siegfried.csv', on_bad_lines='skip')
webverlauf_siegfried = pd.read_csv('webverlauf_siegfried.csv', on_bad_lines='skip')

# Auswählen der CSV-Spalte für Analyse
messages_huberta['Text'] = messages_huberta['Text'].astype('str')
gesuchte_elemente_huberta['Wert'] = gesuchte_elemente_huberta['Wert'].astype('str')
webverlauf_huberta['Titel'] = webverlauf_huberta['Titel'].astype('str')
messages_siegfried['Text'] = messages_siegfried['Text'].astype('str')
gesuchte_elemente_siegfried['Wert'] = gesuchte_elemente_siegfried['Wert'].astype('str')
webverlauf_siegfried['Titel'] = webverlauf_siegfried['Titel'].astype('str')

# Umwandeln von CSV-Spalte in Liste für Weiterverarbeitung
m_h = [word for message in messages_huberta['Text'] for word in message.split(' ')]
g_e_h = [word for message in gesuchte_elemente_huberta['Wert'] for word in message.split(' ')]
wv_h =[word for message in webverlauf_huberta['Titel'] for word in message.split(' ')]
m_s = [word for message in messages_siegfried['Text'] for word in message.split(' ')]
g_e_s = [word for message in gesuchte_elemente_siegfried['Wert'] for word in message.split(' ')]
wv_s =[word for message in webverlauf_siegfried['Titel'] for word in message.split(' ')]

def button_action():
    entry_text = eingabefeld.get()
    file_name = eingabefeld2.get()
    if (entry_text == ""):
        cloud_label.config(text="Welche Dateien sollen verwendet werden?")
    else:
        words = []
        entrys = entry_text.split(' ')
        for entry in entrys:
            words += globals()[entry]

        # WordCloud wird erstellt
        wordCloud = WordCloud(stopwords=stopwords, max_words=20)
        wordCloud.generate_from_text(text=' '.join(words))
        fig, axs = plt.subplots(figsize=(16, 6))
        fig.suptitle('WordCloud von ' + file_name, fontsize=16)
        axs.imshow(wordCloud.to_array())
        plt.savefig(file_name + '.png', bbox_inches='tight') # Abspeichern des Plots

        # Cloud im Fenster anzeigen
        global cloud
        cloud = PhotoImage(file=file_name +'.png')
        label_cloud = Label(master=fenster, image=cloud)
        label_cloud.grid(row = 4, column = 0, columnspan = 2)
        label_cloud.config(image=cloud)

fenster = Tk()
fenster.title("WordCloud Generator")

my_label = Label(fenster, text="Welche Datei soll verwendet werden? ")
label2 = Label(fenster, text='Unter welchem Namen soll das Bild gespeichert werden?')

cloud_label = Label(fenster)

eingabefeld = Entry(fenster, bd=5, width=40)
eingabefeld2 = Entry(fenster, bd=5, width=40)

generate_button = Button(fenster, text="WordCloud generieren", command=button_action)
exit_button = Button(fenster, text="Beenden", command=fenster.quit)

my_label.grid(row = 0, column = 0)
label2.grid(row = 1, column = 0)
eingabefeld.grid(row = 0, column = 1)
eingabefeld2.grid(row=1, column= 1)
generate_button.grid(row = 2, column = 0)
exit_button.grid(row = 2, column = 1)
cloud_label.grid(row = 3, column = 0, columnspan = 2)

mainloop()