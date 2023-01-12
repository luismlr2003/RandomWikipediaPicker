import webbrowser #Webbroser Bibliothek
from tkinter import * #Tk-Framework
from tkinter import ttk #Tk-Framework

#App version
app_ver = 'v1.0.0'

#Öffnet eine zufällige Wikipedia Seite
def openRandomWikiPage():
    url = 'https://en.wikipedia.org/wiki/Special:Random' #Random wiki url
    webbrowser.open_new_tab(url) #Öffnet einen neuen Browser tab
    
#Öffnet das Hauptfenster
def openApp():
    app = Tk() #Tk-Framework initialisieren
    app.title("Random Wiki-Picker " + app_ver) #Fenstertitel setzen
    app.geometry("335x35") #Fenstergröße setzen
    app.resizable(0, 0) #Verbietet das Neuskalieren der App   
    app_frame = ttk.Frame(app, padding=5) #Erstellt einen neuen AppFrame
    app_frame.grid() #Initialisiert das FrameGrid
    ttk.Label(app_frame, text='Made by Luis Müller. ' + app_ver).grid(column=0, row=0) #Infolabel
    ttk.Button(app_frame, text="Click to open random wiki page", command=openRandomWikiPage).grid(column=1, row=0) #Button
    app.mainloop() #Startet den main thread

#Ruft die Methode zum Öffnen der App ab.
openApp()