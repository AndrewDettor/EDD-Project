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
            self.textEdit_8.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Scores Entered Correctly? - YES</span></p></body></html>")

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
            self.textEdit_9.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">What do you wish to use your computer for?</span></p></body></html>")

            self.textEdit_10.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Waiting on choice for first question...</span></p></body></html>")

            self.textEdit_11.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Final Verdict: Waiting on choice for first question...</span></p></body></html>")

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

            self.textEdit_11.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Final Verdict: Waiting on choice for second question...</span></p></body></html>")

            if self.use == 1:
                self.submitQuestion2()

                self.textEdit_10.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"></span></p></body></html>")

            elif self.use == 2:
                self.textEdit_10.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">At medium settings, what framerate do you hope to achieve?</span></p></body></html>")

                # fill the comboBox for question 2
                options = ["30 fps", "60 fps", "144 fps"]
                for option in options:
                    self.comboBox_2.addItem(option)

            elif self.use == 3:
                self.textEdit_10.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">What do you use your workstation for?</span></p></body></html>")

                # fill the comboBox for question 2
                options = ["Rendering 1080p Footage", "Rendering 4K Footage", "AutoDesk Applications", "VMs", "No clue"]
                for option in options:
                    self.comboBox_2.addItem(option)

    def submitQuestion2(self):

        if self.submitButtonHit and self.question1Hit and not self.question2Hit:

            self.question2Hit = True
            choice2 = self.comboBox_2.currentText()

            if self.use == 2 and choice2 != "30 fps":
                self.use = 3

            if self.use == 3 and choice2 != "No clue":
                self.use = 4

            if self.performance >= self.use:
                self.textEdit_11.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Final Verdict: Your computer is capable of the tasks you require of it.</span></p></body></html>")

            else:

                self.textEdit_11.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Final Verdict: Your computer should be upgraded to more adequately fufill the tasks required of it.</span></p></body></html>")

            # this is where it would call the other parts of the program


app = QApplication(sys.argv)
widget = MainPage()
widget.show()
sys.exit(app.exec_())
