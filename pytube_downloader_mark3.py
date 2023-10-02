import requests
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube


window = Tk()
window.title('Youtube Downloader')
window.columnconfigure(0, weight=1)
folderName = ""

window.geometry('600x300')

def internet_connection():
    try:
        response = requests.get("https://www.youtube.com/", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def save():
    global folderName
    folderName = filedialog.askdirectory()
    label_4.config(text="Selected Folder: " + folderName)
    if len(folderName)>1:
        label_4.config(text= folderName, fg ='green')
    else:
        label_4.config(text='Folder Not Selected', fg='red')

def download():
    url = entry_1.get()
    choice = comboBox.get()
    if internet_connection():
        label_5.config(text='there is internet', fg='green')
    else:
        label_5.config(text='there is no internet', fg='red')

    if len (url) > 1:
        yt = YouTube(url)
        if choice == pilihan[0]:
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()
        elif choice == pilihan[1]:
            select = yt.streams.filter(progressive= True).first()
        elif choice == pilihan[2]:
            select = yt.streams.filter(only_audio= True).first()
        select.download(folderName)
        label_2.config(text='Download Complete', fg='green')

label_1 = Label(window, text='Youtube Downloader', fg='blue', font=('arial', 10, 'bold'))
label_1.grid()

label_1a = Label(window, text='', fg='blue', font=('arial', 10, 'bold'))
label_1a.grid()

label_1b = Label(window, text='Masukan link Youtube', fg='blue', font=('arial', 10, 'bold'))
label_1b.grid()

entryVar = StringVar()
entry_1 = Entry(window, width=50, textvariable=entryVar)
entry_1.grid()

button_save = Button(window, width=10, text='Save Folder', bg='lightblue', command=save)
button_save.grid()

label_4 = Label(window, text="Selected Folder: ")
label_4.grid()

pilihan = ["720", "360", "only sound"]
comboBox = ttk.Combobox(window, values=pilihan)
comboBox.grid()

button_download = Button(window, width=10, text='Download', bg='lightgreen', command=download)
button_download.grid()

label_2 = Label(window, text="")
label_2.grid()

label_5 = Label(window, text="Internet Status: ", fg='green')
label_5.grid()

window.mainloop()