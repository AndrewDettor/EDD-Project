# Main file for the UI
# Use this file to make changes to elements of the UI

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
        # Below is basically like the main method for this class (I think)
        # This code probably doesn't belong here and maybe should be after the class definition

        # get scores after submit button is hit
        scoresList = self.pushButton.clicked.connect(self.submitScores)

        # IMPLEMENT INPUT CHECKING HERE, DON'T PROCEED UNTIL INPUTS ARE GOOD

        # assuming inputs are good...
        self.textEdit_8.setText("Scores Entered Correctly? - YES")

        # turn scoresList's elements into ints
        intScoresList = [int(score) for score in scoresList]

        # Quantify preformance
        PassMark = intScoresList[5]
        performance = 0
        if PassMark < 1260:
            performance = 1
        elif PassMark < 3500:
            performance = 2
        elif PassMark < 5200:
            performance = 3
        else:
            performance = 4

        # change text for question 1
        self.textEdit_9.setText("What do you wish to use your computer for?")
        self.textEdit_10.setText("Waiting on choice for first question...")
        self.textEdit_11.setText("Final Verdict: Waiting on choice for first question...")

        # fill the comboBox for the question 1
        options = ["Web browsing / Office", "Video Games", "Workstation"]
        for option in options:
            self.comboBox.addItem(option)

        # get choice for question 1
        choice1 = self.pushButton_2.clicked.connect(self.submitQuestion1)

        if choice1 == "Web browsing / Office":
            use = 1
        elif choice1 == "Video Games":
            use = 2
        elif choice1 == "Workstation":
            use = 3

        # change text of verdict box
        self.textEdit_11.setText("Final Verdict: Waiting on choice for second question...")

        # change text for question 2
        if use == 2:
            self.textEdit_10.setText("At medium settings, what framerate do you hope to achieve?")
            # fill the comboBox for question 2
            options = ["30 fps", "60 fps", "144 fps"]
            for option in options:
                self.comboBox_2.addItem(option)

            # get choice for question 2
            choice2 = self.pushButton_3.clicked.connect(self.submitQuestion2)

            if choice2 != "30 fps":
                use = 3

        elif use == 3:
            self.textEdit_10.setText("What do you use your workstation for?")
            # fill the comboBox for question 2
            options = ["Rendering 1080p Footage", "Rendering 4K Footage", "AutoDesk Applications", "VMs", "Listen bro, I just work here and they give me this hunk of metal"]
            for option in options:
                self.comboBox_2.addItem(option)

            # get choice for question 2
            choice2 = self.pushButton_3.clicked.connect(self.submitQuestion2)

            if choice2 != "Listen bro, I just work here and they give me this hunk of metal":
                use = 4

        if performance >= use:
            self.textEdit_11.setText("Final Verdict: Your computer is capable of the tasks you require of it.")
        else:
            self.textEdit_11.setText("Final Verdict: Your computer should be upgraded to more adequately fufill the tasks required of it.")

        # this is where it would call the other parts of the program

    def submitScores(self):
        scoreCPU = self.plainTextEdit.toPlainText()
        score2D = self.plainTextEdit_2.toPlainText()
        score3D = self.plainTextEdit_3.toPlainText()
        scoreMemory = self.plainTextEdit_4.toPlainText()
        scoreDisk = self.plainTextEdit_5.toPlainText()
        scorePassmark = self.plainTextEdit_6.toPlainText()
        # scores are strings at the moment
        return [scoreCPU, score2D, score3D, scoreMemory, scoreDisk, scorePassmark]

    def submitQuestion1(self):
        return self.comboBox.currentText()

    def submitQuestion2(self):
        return self.comboBox_2.currentText()

# how to open a separate window
#    def move(self):
#        from OtherPage import SecondPage
#        # from file name import the class name of the second page
#        theclass = SecondPage()
#        theclass.exec_()


app = QApplication(sys.argv)
widget = MainPage()
widget.show()
sys.exit(app.exec_())
