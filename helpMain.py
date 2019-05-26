import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.uic import loadUi


class HelpPage(QDialog):
    def __init__(self):
        super(HelpPage, self).__init__()
        loadUi('help.ui', self)
        self.label_2.setPixmap(QPixmap("cpu_picture.jpg"))
        self.label_3.setPixmap(QPixmap("gpu_picture.jpg"))
        self.label_4.setPixmap(QPixmap("ram_picture.jpg"))
        self.label_5.setPixmap(QPixmap("disk_picture.jpg"))
        self.label_6.setPixmap(QPixmap("passmark_picture.png"))
