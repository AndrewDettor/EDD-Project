# Main file for the UI
# Use this file to make changes to elements of the UI

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi


class MainPage(QDialog):
    def __init__(self):
        super(MainPage, self).__init__()
        loadUi('INSERT_NAME_OF_FILE.ui', self)
        # attaching a function to a button in your interface
        self.fillCombobox()
        self.pushButton_2.clicked.connect(self.retrieveText)
        self.pushButton.clicked.connect(self.takeText)
        self.pushButton_3.clicked.connect(self.move)

    def move(self):
        from OtherPage import SecondPage
        # from file name import the page
        theclass = SecondPage()
        theclass.exec_()

    def takeText(self):
        x = self.comboBox.currentText()
        self.textEdit.setText(x)

    def fillCombobox(self):
        cities = ["NY", "SF", "LA", "Chicago"]
        for x in cities:
            self.comboBox.addItem(x)

    def retrieveText(self):
        words = self.plainTextEdit.toPlainText()
        self.textEdit_2.setText(words)


# pyuic5 guiLayout.ui > guiLayout.py is the command to turn ui into code
# plainTextEdit to collect text
# textEdit to display text
# pushButton to use as a button
# comboBox to have a drop down choice thing

app = QApplication(sys.argv)
widget = MainPage()
widget.show()
sys.exit(app.exec_())
