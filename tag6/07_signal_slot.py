import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Window (QMainWindow):
    def __init__ (self):
        super().__init__()

        self.setWindowTitle("Grid Layout")

        layout = QVBoxLayout()

        #Widgets erstellen

        button1 = QPushButton("Button1")
        button2 = QPushButton("Button2")
        checkbox = QCheckBox("Hello World")
        self.name = QLineEdit()

        # widget dem Layout hinzufügen

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(checkbox)
        layout.addWidget(self.name)

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)
        self.show()

        #########

        button1.clicked.connect(self.Button1)
        button2.clicked.connect(self.Button2)
        checkbox.stateChanged.connect(self.MyCheckBox)

    def MyCheckBox(self, state):
        if state == Qt.CheckState.Checked:
            print("Checkbox ist gewählt")
        else:
            print("Checkbox ist nicht gewählt")

    def Button1 (self):
        print("Line Edit hat Wert: " + self.name.text())

    def Button2 (self):
        print("Button 2 gedrückt")


app = QApplication([])
fenster = Window()
fenster.raise_()
app.exec()