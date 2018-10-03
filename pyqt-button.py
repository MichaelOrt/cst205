import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import pyqtSlot

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        vbox = QVBoxLayout()

        self.my_btn = QPushButton("Button 1", self)
        self.my_lbl = QLabel('Button not clicked')
        self.my_btn.clicked.connect(self.on_click)
        vbox.addWidget(self.my_btn)
        vbox.addWidget(self.my_lbl)
        self.setLayout(vbox)

    @pyqtSlot()
    def on_click(self):
       self.my_lbl.setText('Button clicked')
       print("Clicked")

app = QApplication(sys.argv)
main_win = MainWindow()
main_win.show()
sys.exit(app.exec_())