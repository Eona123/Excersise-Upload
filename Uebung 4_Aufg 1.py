import sys
import csv
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createLayout()
        self.createConnects()
        #self.createConnects()              --> wird in diesem GUI nicht verwendet

        menubar = self.menuBar()            #--> MENUBAR erstellen
        filemenu = menubar.addMenu("File")  #--> Variable gesetzt um später darin eine dropdown zu implementieren
        
        save = QAction("Save", self)
        quit = QAction("Quit", self)

        filemenu.addAction(save)            #--> Trigger das etwas passieren kann
        save.triggered.connect(self.txtExport)
        filemenu.addAction(quit)
        quit.triggered.connect(self.menu_quit)

#-----------------------------------------------------------------------------

    def createLayout(self):
        ## Fenstertitel / Layout
        self.setWindowTitle("Mein erstes GUI")

#-----------------------------------------------------------------------------

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
        self.button1 = QPushButton("Save")
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
#-----------------------------------------------------------------------------
        ## Zentrierung der Widgets
        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)

        ## Fenster anzeigen
        self.show()
#----------------------------------------------------------------------------------------
    #Funktionen     
    def createConnects(self):
        self.button1.clicked.connect(self.txtExport) 

    #Musterlösung für CSV export
    def write_file(self):
        formfields = []
        formfields.append(self.prenameLine.text())
        formfields.append(self.nameLine.text())
        formfields.append(self.birthdateLIne.text())
        formfields.append(self.adressLine.text())
        formfields.append(self.plzLine.text())
        formfields.append(self.countries.currentText())

        file = open("ausgabe2.csv","w", encoding="utf-8")
        writer = csv.writer(file, delimiter = ",", lineterminator="\n")
        writ.writerow(formfields)
        file.close()

    def txtExport(self):
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

        
    def menu_quit(self):
        print("Quit")
        self.close()                  #--> Schliesst das fenster
    
#-------------------------------------------------------------------------------------

def main():
    app = QApplication(sys.argv)  
    mainwindow = Fenster()       
    mainwindow.raise_()           
    app.exec_()                   

if __name__ == '__main__':
    main()