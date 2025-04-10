import sys
import csv
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QDesktopServices
import urllib.parse 
query = 'Hellö Wörld@' 
a = urllib.parse.quote(query)

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createLayout()
        self.createConnects()

        menubar = self.menuBar()            #--> MENUBAR erstellen
        filemenu = menubar.addMenu("File")  #--> Variable gesetzt um später darin eine dropdown zu implementieren
        editmenu = menubar.addMenu("View")

        save = QAction("Save", self)
        karte = QAction("Karte", self)

        filemenu.addAction(save)            #--> Trigger das etwas passieren kann
        save.triggered.connect(self.write_file)
        editmenu.addAction(karte)
        karte.triggered.connect(self.open_Web)


#-----------------------------------------------------------------------------
    def createLayout(self):
        ## Fenstertitel / Layout
        self.setWindowTitle("Aufgabe 5")
        self.setMinimumSize(800,200)

        layout = QGridLayout()                          #Formlayout ist mit Zeilen --> .addRow
                                                        #GrdiLayout ist immer mit Boxen denen man eine Koordinate gibt --> .addWidget
        self.prenameLabel = QLabel("Vorname:", )
        self.prenameLine = QLineEdit()
        self.nameLabel = QLabel("Name:")
        self.nameLine = QLineEdit()
        self.birthdateLabel = QLabel("Geburtstag:")
        self.birthdateLIne = QDateEdit()
        self.adressLabel = QLabel("Adresse:")
        self.adressLine = QLineEdit()
        self.plzLabel = QLabel("Post Leitzahl:")
        self.plzLine = QLineEdit()
        self.landLabel = QLabel("Land:")

        #Auswahl vorgeben durch ComboBox
        self.countries = QComboBox() 
        self.countries.addItems(["Schweiz", "Deutschland", "Österreich"])
        self.button1 = QPushButton("Auf Karte zeigen")
        self.button2 = QPushButton("Laden")
        self.button3 = QPushButton("Speichern")
#-----------------------------------------------------------------------------
        layout.addWidget(self.prenameLabel, 0, 0)       ###-->mit Koordinaten die POSITION bestimmen
        layout.addWidget(self.prenameLine, 0, 1)
        layout.addWidget(self.nameLabel, 1, 0)       ###-->mit Koordinaten die POSITION bestimmen
        layout.addWidget(self.nameLine, 1, 1)
        layout.addWidget(self.birthdateLabel, 2, 0)
        layout.addWidget(self.birthdateLIne, 2, 1)
        layout.addWidget(self.adressLabel, 3, 0)
        layout.addWidget(self.adressLine, 3, 1)
        layout.addWidget(self.plzLabel, 4, 0)
        layout.addWidget(self.plzLine, 4, 1)
        layout.addWidget(self.landLabel, 5, 0)
        layout.addWidget(self.countries, 5, 1)
        layout.addWidget(self.button1, 6, 0, 1, 2)
        layout.addWidget(self.button2, 7, 0, 1, 2)
        layout.addWidget(self.button3, 8, 0, 1, 2)
#-----------------------------------------------------------------------------
        ## Zentrierung der Widgets
        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)
        self.show()
#-----------------------------------------------------------------------------
    def createConnects(self):
        self.button1.clicked.connect(self.open_Web)  
        self.button2.clicked.connect(self.open_oldFolder)      
        self.button3.clicked.connect(self.write_file)
 

    #Musterlösung für CSV export
    def write_file(self):
        formfields = []
        formfields.append(self.prenameLine.text())
        formfields.append(self.nameLine.text())
        formfields.append(self.birthdateLIne.text())
        formfields.append(self.adressLine.text())
        formfields.append(self.plzLine.text())
        formfields.append(self.countries.currentText())

        document, filter = QFileDialog.getSaveFileName(self, 
        "Datei Sepeichern",
        "C:/Users/adrie/SynologyDrive/13_FHNW/2.Semester/05_GeoProg",
        "Text Datei (*.csv)")
        file = open(document, "w", encoding="utf-8", newline="\n")
        writer = csv.writer(file, delimiter = ";", lineterminator = "\n")
        writer.writerow(formfields)
        file.close()


    def open_Web(self):
        link = "https://www.google.ch/maps/place/Hofackerstrasse+30+4132+Muttenz+Schweiz" 
        QDesktopServices.openUrl(QUrl(link))
    
    def open_oldFolder(self):
        dateien, filter = QFileDialog.getOpenFileName(self, 
        "Datei Sepeichern",
        "C:/Users/adrie/SynologyDrive/13_FHNW/2.Semester/05_GeoProg",
        "Text Datei (*.csv)")
        opend_file = open(dateien, "r", encoding="utf-8", newline="\n")
        reader = csv.reader(opend_file, delimiter = ";", lineterminator = "\n")
        
        for i in reader:
            self.prenameLine.setText(i[0])
            self.nameLine.setText(i[1])
            self.birthdateLIne.setDate(QDate.fromString(i[2], "yyyy-MM-dd"))
            self.adressLine.setText(i[3])
            self.plzLine.setText(i[4])
            self.countries.setCurrentText(i[5])
    

def main():
    app = QApplication(sys.argv)  
    mainwindow = Fenster()       
    mainwindow.raise_()           
    app.exec_()                   

if __name__ == '__main__':
    main()