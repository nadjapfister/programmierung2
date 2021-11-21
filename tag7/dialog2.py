import PyQt5
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Dialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        label = QLabel("Dies ist ein Label")
        button = QPushButton("Ok")
        layout = QVBoxLayout()

        self.setWindowTitle("Dialog")

        layout.addWidget(label)
        layout.addWidget(button)
        self.setLayout(layout)
        button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.close


class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dialog Beispiele")
        layout = QVBoxLayout()

        buttons = []

        buttons.append(QPushButton("QMessageBox: Information"))
        buttons.append(QPushButton("QMessageBox: About"))
        buttons.append(QPushButton("QMessageBox: AboutQT"))
        buttons.append(QPushButton("QMessageBox: Warning"))
        buttons.append(QPushButton("QMessageBox: Critical"))
        buttons.append(QPushButton("QMessageBox: Question"))
        buttons.append(QPushButton("Open file"))
        buttons.append(QPushButton("Open Multiple files"))
        buttons.append(QPushButton("save file"))
        buttons.append(QPushButton("input Dialog"))
        buttons.append(QPushButton("QColor Dialog"))
        buttons.append(QPushButton("QFontDialog"))
        buttons.append(QPushButton("Custom Dialog"))


        buttons[0].clicked.connect(self.button1_clicked)
        buttons[1].clicked.connect(self.button2_clicked)
        buttons[2].clicked.connect(self.button3_clicked)
        buttons[3].clicked.connect(self.button4_clicked)
        buttons[4].clicked.connect(self.button5_clicked)
        buttons[5].clicked.connect(self.button6_clicked)
        buttons[6].clicked.connect(self.button7_clicked)
        buttons[7].clicked.connect(self.button8_clicked)
        buttons[8].clicked.connect(self.button9_clicked)
        buttons[9].clicked.connect(self.button10_clicked)
        buttons[10].clicked.connect(self.button11_clicked)
        buttons[11].clicked.connect(self.button12_clicked)
        buttons[12].clicked.connect(self.button13_clicked)
  

        style = """ QPushButton{ font-size:36px; background-color: #89CFF0;  }
                    QPushButton:pressed {font-size: 32px; background-color: #89CFF0 }"""

        for button in buttons:
            button.setStyleSheet(style)
            layout.addWidget(button)

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        self.show()

    def button1_clicked(self):
        QMessageBox.information(self, "Titel", "<h1> Hello World </h1> Python macht spass <br/> Ein Zeilenumbruch")

    def button2_clicked(self):
        QMessageBox.about(self, "Fenstertitel", "Dieses Programm wurde mit PYQT5 erstellt")

    def button3_clicked(self):
        QMessageBox.aboutQt(self)

    def button4_clicked(self):
        QMessageBox.warning(self, "Titel", "Disk ist voll")

    def button5_clicked(self):
        QMessageBox.critical(self, "Stop", "Das Konfigurations-File konnte nidcht geladen werden. DAs Prdogramm muss beendet werden.")
        self.close()   

    def button6_clicked(self):
        antwort = QMessageBox.question(self, "Frage", "Ist Python eine gute Sprache?", QMessageBox.Yes, QMessageBox.No)

        if antwort == QMessageBox.Yes:
            QMessageBox.information(self, "Python", "ja, eh ich mags")

        else:
            QMessageBox.critical(self, "schade", "Ok, das Programm wird beendet")
            self.close()

    def button7_clicked(self):
        dateifilter = "textdatei (*.txt *.ttt);; Python File (*.py)"
        #path = QStandardPaths.StandardLocation(0)

        # QFileDialog.getOpenFileName(self, "Datei öffnen", "", "textdatei (*.txt *.ttt);; Python File (*.py)")

        filename, filter = QFileDialog.getOpenFileName(self, "Datei öffnen", "", dateifilter)

        if filename != "":
            QMessageBox.information(self, f"<h1>{filename}</h1><h2>{filter}</h2>")
        else:
            QMessageBox.warning(self, "Kein File", "kein File ausgewählt")

    def button8_clicked(self):
        filenamen, filter = QFileDialog.getOpenFileName(self, "Dateien öffnen", "", "Text (*.txt);; Python File (*.py)")
        print(filenamen)

    def button9_clicked(self):
        filename, filter = QFileDialog.getSaveFileName(self, "Speichern", "", "Python (*.py)")
        print(filename, filter)

        # file = open (File, "w)")

    def button10_clicked(self):
        wert, ok = QInputDialog.getItem(self, "Auswahl", "Welches land ist schöner", ["ch", "de", "au"], 1, True)
        #wert, ok = QInputDialog.getDouble(self, "Titel", "text")
        #wert, ok = QInputDialog.getInt(self, "titel", "text", 20, 10, 30)

        if ok:
            print(wert)

    def button11_clicked(self):
        farbe = QColorDialog.getColor()
        print(farbe.red(), farbe.green(), farbe.blue())

    def button12_clicked(self):
        font = QFontDialog.getFont()

    def button13_clicked(self):
        d = Dialog(self)
        d.exec()


        

app = QApplication ([])
f = Fenster()
app.exec()