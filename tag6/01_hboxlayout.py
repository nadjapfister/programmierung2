from PyQt5.QtCore import center
from PyQt5.QtWidgets import *

class Fenster(QMainWindow):
    def __init__ (self):
        super().__init__()

        #self.setGeometry(20,120,640,480)
        self.setMinimumWidth(1240)
        self.setMinimumHeight(780)
        self.setWindowTitle("Dies ist ein Fenster")
        
        layout = QHBoxLayout() #horizontal
        #layout = QVBoxLayout() #vertikal

        button1 = QPushButton("Hello Word")
        button2 = QPushButton("OK")
        button3 = QPushButton("Abbrechen")

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)

        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)
        self.show()


app = QApplication([])
fenster = Fenster()
fenster.raise_()
app.exec()

