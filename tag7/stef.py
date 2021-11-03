from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dialog Beispiele")
        layout = QVBoxLayout()

        buttons = []

        buttons.append(QPushButton("QMessageBox: Information"))
        buttons.append(QPushButton("QMessageBox: About"))
        buttons.append(QPushButton("QMessageBox: Warining"))
        buttons.append(QPushButton("QMessageBox: Critical"))
        buttons.append(QPushButton("QMessageBox: Question"))
        buttons.append(QPushButton("6"))
        buttons.append(QPushButton("7"))
        buttons.append(QPushButton("8"))
        buttons.append(QPushButton("9"))

        buttons[0].clicked.connect(self.button1_clicked)
        buttons[1].clicked.connect(self.button2_clicked)
        buttons[2].clicked.connect(self.button3_clicked)
        buttons[3].clicked.connect(self.button4_clicked)
        buttons[4].clicked.connect(self.button5_clicked)
        buttons[5].clicked.connect(self.button6_clicked)
        buttons[6].clicked.connect(self.button7_clicked)
        buttons[7].clicked.connect(self.button8_clicked)
        buttons[8].clicked.connect(self.button9_clicked)

        style = """QPushButton {font-size: 36px; background-color: #00AA00; }
                   QPushButton:pressed {font-size: 32px; background-color: #AA0000;}"""
        for button in buttons:
            button.setStyleSheet(style)
            layout.addWidget(button)

        center = QWidget()

        center.setLayout(layout)
        

        self.setCentralWidget(center)

        self.show()


    def button1_clicked(self):
        QMessageBox.information(self, "Titel", "<h1> Hello Wolrd </h1> Python macht Spass <br> Dies ist eine Zeile")
    
    def button2_clicked(self):
        QMessageBox.about(self, "Titel", "Dieses Programm wurde mit PyQT5 erstellt")

    def button3_clicked(self):
        QMessageBox.warning(self, "Titel", "Disc ist voll")

    def button4_clicked(self):
        QMessageBox.critical(self, "Titel", "Halt STOP")
        self.close()

    def button5_clicked(self):
        antwort = QMessageBox.question(self, "Titel", "Ist Python eine gute Sprache?" , QMessageBox.Yes, QMessageBox.No)

        if antwort == QMessageBox.Yes:
            QMessageBox.information(self, "Python", "Ja, das ist klar")

        else:
            QMessageBox.critical(self, "Buhhh!!!", "Ok, das Prgramm wird beendet")
            self.close()

    def button6_clicked(self):
        pass

    def button7_clicked(self):
        pass

    def button8_clicked(self):
        pass

    def button9_clicked(self):
        pass

app = QApplication([])
f = Fenster()
app.exec()
