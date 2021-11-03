import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dialog Beispiele")
        layout = QVBoxLayout()

        button1 = QPushButton("QMessageBox: Information")
        button2 = QPushButton("QMessageBox: About")
        button3 = QPushButton("QMessageBox: AboutQT")
        button4 = QPushButton("QMessageBox: Warning")
        button5 = QPushButton("QMessageBox: Critical")
        button6 = QPushButton("QMessageBox: Question")


        button1.clicked.connect(self.button1_clicked)
        button2.clicked.connect(self.button2_clicked)
        button3.clicked.connect(self.button3_clicked)
        button4.clicked.connect(self.button4_clicked)
        button5.clicked.connect(self.button5_clicked)
        button6.clicked.connect(self.button6_clicked)

        style = """ QPushButton{ font-size:36px; background-color: #89CFF0;  }
                    QPushButton:pressed {font-size: 32px; background-color: #89CFF0 }"""

        button1.setStyleSheet(style)
        button2.setStyleSheet(style)
        button3.setStyleSheet(style)
        button4.setStyleSheet(style)
        button5.setStyleSheet(style)
        button6.setStyleSheet(style)

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.addWidget(button5)
        layout.addWidget(button6)


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

app = QApplication ([])
f = Fenster()
app.exec()