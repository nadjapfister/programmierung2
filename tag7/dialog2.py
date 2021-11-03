import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


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
        buttons.append(QPushButton("Open dialog"))
        buttons.append(QPushButton("8"))
        buttons.append(QPushButton("9"))
        buttons.append(QPushButton("10"))


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
        QFileDialog.getOpenFileName(self, "Datei öffnen", "", "textdatei (*.txt *.ttt)")

    def button8_clicked(self):
        pass

    def button9_clicked(self):
        pass

    def button10_clicked(self):
        pass

app = QApplication ([])
f = Fenster()
app.exec()