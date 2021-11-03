import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Window (QMainWindow):
    def __init__ (self):
        super().__init__()

        self.setWindowTitle("Grid Layout")

        #layout = QGridLayout()
        layout_start = QVBoxLayout()
        layout2 = QHBoxLayout()

        #Widgets erstellen
        button1 = QPushButton("Button1")
        button2 = QPushButton("Button2")
        button3 = QPushButton("Button3") 

        # widget dem Layout hinzufügen
        layout_start.addWidget(button1)
        layout2.addWidget(button2)
        layout2.addWidget(button3)

        layout_start.addLayout(layout2)

        center = QWidget()
        center.setLayout(layout_start)

        self.setCentralWidget(center)
        self.show()


app = QApplication([])
fenster = Window()
fenster.raise_()
app.exec()