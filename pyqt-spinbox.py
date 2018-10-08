import sys
from PyQt5.QtWidgets import QApplication, QWidget, \
        QDial, QHBoxLayout, QVBoxLayout, QGridLayout, \
        QSpinBox, QLabel
from PyQt5.QtGui import QIcon, QPixmap

class Form(QWidget):
    def __init__(self, width=200, height=400):
        super().__init__()

        self.dial = QDial()
        self.dial.setNotchesVisible(True)
        self.spinbox = QSpinBox()
        self.width = width
        self.height = height

        self.picture = QLabel()
        self.pixmap = QPixmap("images/chualar_sign.jpg")
        self.picture.setPixmap(self.pixmap)

        layout = QGridLayout()
        layout.addWidget(self.picture, 0, 0)
        layout.addWidget(self.dial, 1, 0)
        layout.addWidget(self.spinbox, 1, 1)

        self.setLayout(layout)
        self.setGeometry(100,100,self.width, self.height) 
        self.setWindowTitle("Signals and Slots")
        self.dial.valueChanged.connect(self.spinbox.setValue)
        self.spinbox.valueChanged.connect(self.dial.setValue)

    def set_size(self, width, height):
        self.width = width
        self.height = height
        self.setGeometry(100,100,self.width, self.height)

app = QApplication(sys.argv)
ex = Form(height=1000, width=200)
# ex.set_size(1000,1000)

ex.show()
sys.exit(app.exec_())