# Main file for the UI
# use this file to make changes to elements of the UI

# pyuic5 guiLayout.ui > guiLayout.py is the command to turn ui into code
# plainTextEdit to collect text
# textEdit to display text
# pushButton to use as a button
# comboBox to have a drop down choice thing

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi


class MainPage(QDialog):
    def __init__(self):
        super(MainPage, self).__init__()
        loadUi('guiLayout.ui', self)

        self.use = 0
        self.performance = 0
        self.submitButtonHit = False
        self.question1Hit = False
        self.question2Hit = False

        self.pushButton.clicked.connect(self.submitScores)
        self.pushButton_2.clicked.connect(self.submitQuestion1)
        self.pushButton_3.clicked.connect(self.submitQuestion2)

    def submitScores(self):
        if not self.submitButtonHit and not self.question1Hit and not self.question2Hit:

            self.submitButtonHit = True

            scoreCPU = self.plainTextEdit.toPlainText()
            score2D = self.plainTextEdit_2.toPlainText()
            score3D = self.plainTextEdit_3.toPlainText()
            scoreMemory = self.plainTextEdit_4.toPlainText()
            scoreDisk = self.plainTextEdit_5.toPlainText()
            scorePassmark = self.plainTextEdit_6.toPlainText()
            # scores are strings at the moment
            scoresList = [scoreCPU, score2D, score3D, scoreMemory, scoreDisk, scorePassmark]
            # IMPLEMENT INPUT CHECKING HERE
            # assuming inputs are good...
            self.textEdit_8.setText("Scores Entered Correctly? - YES")
            intScoresList = [int(score) for score in scoresList]
            # Quantify self.performance
            PassMark = intScoresList[5]
            if PassMark < 1260:
                self.performance = 1
            elif PassMark < 3500:
                self.performance = 2
            elif PassMark < 5200:
                self.performance = 3
            else:
                self.performance = 4

            # change text for question 1
            self.textEdit_9.setText("What do you wish to use your computer for?")
            self.textEdit_10.setText("Waiting on choice for first question...")
            self.textEdit_11.setText("Final Verdict: Waiting on choice for first question...")

            # fill the comboBox for the question 1
            options = ["Web browsing / Office", "Video Games", "Workstation"]
            for option in options:
                self.comboBox.addItem(option)

    def submitQuestion1(self):
        if self.submitButtonHit and not self.question1Hit and not self.question2Hit:

            self.question1Hit = True
            choice1 = self.comboBox.currentText()
            if choice1 == "Web browsing / Office":
                self.use = 1
            elif choice1 == "Video Games":
                self.use = 2
            elif choice1 == "Workstation":
                self.use = 3

            # change text of verdict box
            self.textEdit_11.setText("Final Verdict: Waiting on choice for second question...")

            if self.use == 1:
                self.submitQuestion2()
                self.textEdit_10.setText("")

            elif self.use == 2:
                self.textEdit_10.setText("At medium settings, what framerate do you hope to achieve?")
                # fill the comboBox for question 2
                options = ["30 fps", "60 fps", "144 fps"]
                for option in options:
                    self.comboBox_2.addItem(option)

            elif self.use == 3:
                self.textEdit_10.setText("What do you use your workstation for?")
                # fill the comboBox for question 2
                options = ["Rendering 1080p Footage", "Rendering 4K Footage", "AutoDesk Applications", "VMs", "Listen bro, I just work here and they give me this hunk of metal"]
                for option in options:
                    self.comboBox_2.addItem(option)

    def submitQuestion2(self):

        if self.submitButtonHit and self.question1Hit and not self.question2Hit:

            self.question2Hit = True
            choice2 = self.comboBox_2.currentText()

            if self.use == 2 and choice2 != "30 fps":
                self.use = 3

            if self.use == 3 and choice2 != "Listen bro, I just work here and they give me this hunk of metal":
                self.use = 4

            if self.performance >= self.use:
                self.textEdit_11.setText("Final Verdict: Your computer is capable of the tasks you require of it.")
            else:
                self.textEdit_11.setText("Final Verdict: Your computer should be upgraded to more adequately fufill the tasks required of it.")

            # this is where it would call the other parts of the program


app = QApplication(sys.argv)
widget = MainPage()
widget.show()
sys.exit(app.exec_())
