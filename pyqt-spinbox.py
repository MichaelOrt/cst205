import sys
from PyQt5.QtWidgets import QApplication, QWidget, \
        QDial, QHBoxLayout, QVBoxLayout, QGridLayout, \
        QSpinBox, QLabel
from PyQt5.QtGui import QIcon, QPixmap

class Form(QWidget):
    def __init__(self):
        super().__init__()

        self.dial = QDial()
        self.dial.setNotchesVisible(True)
        self.spinbox = QSpinBox()

        self.picture = QLabel()
        self.pixmap = QPixmap("images/chualar_sign.jpg")
        self.picture.setPixmap(self.pixmap)

        layout = QGridLayout()
        layout.addWidget(self.picture, 0, 0)
        layout.addWidget(self.dial, 1, 0)
        layout.addWidget(self.spinbox, 1, 1)

        self.setLayout(layout)
        self.setGeometry(100,100,800,400) 
        self.setWindowTitle("Signals and Slots")
        self.dial.valueChanged.connect(self.spinbox.setValue)
        self.spinbox.valueChanged.connect(self.dial.setValue)

app = QApplication(sys.argv)
ex = Form()
ex.show()
sys.exit(app.exec_())