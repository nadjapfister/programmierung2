from PyQt5.QtWidgets import *

class Fenster(QMainWindow):
    def __init__ (self):
        super().__init__()
        
        #layout = QHBoxLayout() #horizontal
        layout = QVBoxLayout() #vertikal

        label = QLabel("Hello Word")
        edit = QLineEdit()
        button = QPushButton("OK")
        calendar = QCalendarWidget()

        layout.addWidget(label)
        layout.addWidget(edit)
        layout.addWidget(button)
        layout.addWidget(calendar)

        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)
        self.show()


app = QApplication([])
fenster = Fenster()
fenster.raise_()
app.exec()

