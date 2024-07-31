import pokemon_class as mon
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()
        self.setWindowTitle("Pokedex")

        button = QPushButton("Button")
        button.setCheckable(True)
        button.clicked.connect(self.on_click)

        self.setCentralWidget(button)

    def on_click(self):
        print("Clicked")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()