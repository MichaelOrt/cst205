""" pyqt-experiment.py
Setup a dial, a linked form field, a button, and an image and get input from 
the dial and form.

Author: Wes Modes <wmodes@csumb.edu>
Date: Feb 25, 2019
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, \
        QDial, QHBoxLayout, QVBoxLayout, QGridLayout, QSpinBox, \
        QLabel
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon, QPixmap

class MainWindow(QWidget):
    """Setup GUI window"""
    def __init__(self, width=200, height=400):
        super().__init__()

        # store object variables/attributes
        self.my_width = width
        self.my_height = height

        # create dial widget object
        self.dial = QDial()
        self.dial.setNotchesVisible(True)
        self.spinbox = QSpinBox()

        # create pixmap widget object (as part of a Qlabel widget)
        self.picture = QLabel()
        self.pixmap1 = QPixmap("../images/chualar_sign.jpg")
        self.pixmap2 = QPixmap("../images/bit.jpg")
        self.picture.setPixmap(self.pixmap1)

        # create button widget object 
        self.button = QPushButton("Apply", self)

        # create a layout and place all of our elements
        layout = QGridLayout()
        layout.addWidget(self.picture, 0, 0)
        #layout.setColumnStretch(0, 1)
        layout.addWidget(self.dial, 1, 0)
        layout.addWidget(self.spinbox, 2, 0)
        layout.addWidget(self.button, 1, 1)
        #layout.setRowStretch(1, 1)

        # add our layout to the window
        self.setLayout(layout)
        self.setGeometry(100,100,self.my_width, self.my_height) 
        self.setWindowTitle("Photo Adjustment")

        # link dial and form
        self.dial.valueChanged.connect(self.spinbox.setValue)
        self.spinbox.valueChanged.connect(self.dial.setValue)

        # add listener to button click
        self.button.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
       print("Clicked")

    def set_size(self, width, height):
        self.width = width
        self.height = height
        self.setGeometry(100,100,self.width, self.height)

    def change_pix(self):
        self.picture.setPixmap(self.pixmap2)


app = QApplication(sys.argv)
main_win = MainWindow(height=600, width=600)
main_win.show()
#input("hit enter")
#main_win.change_pix()

sys.exit(app.exec_())