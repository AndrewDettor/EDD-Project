# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\logan\Desktop\secondWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from scipy import stats
from pull_parts import PullParts

class Ui_MainWindow(object):
    upgradeComputer = 0
    choice2 = ''
    scoresList = []
    
    def setupUi(self, MainWindow,UC,c2,sL):
        global upgradeComputer
        global choice2
        global scoresList
        
        upgradeComputer = UC
        choice2 = c2
        scoresList = sL
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(470, 40, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(470, 20, 111, 16))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(470, 120, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(470, 100, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(470, 180, 111, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(470, 200, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(220, 200, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 100, 111, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(220, 40, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(220, 120, 113, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(220, 20, 111, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(220, 180, 111, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(280, 260, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(330, 310, 113, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(330, 350, 113, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(330, 390, 113, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(330, 430, 113, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(300, 310, 21, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(300, 350, 21, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(300, 390, 21, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(290, 430, 41, 20))
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Recommended CPU"))
        self.label_2.setText(_translate("MainWindow", "Recommended GPU"))
        self.label_3.setText(_translate("MainWindow", "Recommended RAM"))
        self.label_4.setText(_translate("MainWindow", "Current GPU"))
        self.label_5.setText(_translate("MainWindow", "Current CPU"))
        self.label_6.setText(_translate("MainWindow", "Current RAM"))
        self.label_7.setText(_translate("MainWindow", "Estimated Improvement"))
        self.label_8.setText(_translate("MainWindow", "CPU"))
        self.label_9.setText(_translate("MainWindow", "GPU"))
        self.label_10.setText(_translate("MainWindow", "RAM"))
        self.label_11.setText(_translate("MainWindow", "Overall"))

        global upgradeComputer
        global choice2
        global scoresList

        pp = PullParts()
            
        self.lineEdit_4.setText(str(pp.getCPUname()))
        self.lineEdit_5.setText(str(pp.getGPUname()))
        self.lineEdit_6.setText(str(pp.getRAMinfo()))

        if upgradeComputer == 2 and choice2 == '30 fps':
            Tfps = [('Intel Core i5-560M',2578),('GTX 1050',4701),('Corsair CMZ8GX3M2A1600C9 4GB',0)]
            self.doMath(Tfps)

        elif upgradeComputer == 2 and choice2 == '60 fps':
            Sfps = [('AMD PRO A10-9700',5677),('GTX 1060',8974),('Corsair CMZ8GX3M2A1600C16 8GB',0)]
            self.doMath(Sfps)

        elif upgradeComputer == 2 and choice2 == '144 fps':
            Ofps = [('AMD Ryzen 5 2600X',14381),('GTX 1080',12551),('Corsair CMZ8GX3M2A1600C16 8GB x 2',0)]
            self.doMath(Ofps)

        elif upgradeComputer == 3 and (choice2 == 'Rendering 1080p Footage' or choice2 == 'No clue'):
            Tp = [('Intel Core i9-9980XE',8312),('GTX 1080 Ti',14265),('TEAMGROUP-UD4-4133 8GB X 4',0)]
            self.doMath(Tp)

        elif upgradeComputer == 3 and choice2 == 'Rendering 4K Footage':
            Fk = [('Intel Core i9-9980XE',8312),('GTX 2080 Ti',16923),('TEAMGROUP-UD4-4133 8GB X 4',0)]
            self.doMath(Fk)

        elif upgradeComputer == 3 and choice2 == 'AutoDesk Applications':
            AutoDesk = [('Intel Core i9-9980XE',8312),('TITAN V CEO Edition in SLI',16923),('TEAMGROUP-UD4-4133 8GB X 8',0)]
            self.doMath(AutoDesk)
        else:
            VM = [('Intel Xeon Platinum 8168',8312),('TITAN V CEO Edition in SLI',33846),('TEAMGROUP-UD4-4133 8GB X 16',0)]
            self.doMath(VM)
        
    def doMath(self,val):
        self.lineEdit.setText(val[0][0])
        self.lineEdit_2.setText(val[1][0])
        self.lineEdit_3.setText(val[2][0])

        self.lineEdit_7.setText(str(int(abs(val[0][1] - scoresList[0]) / scoresList[0] * 100.0)) + '%')
        self.lineEdit_8.setText(str(int(abs(val[1][1] - scoresList[2]) / scoresList[2] * 100.0)) + '%')
        self.lineEdit_9.setText('n/a')

        whm = stats.hmean([val[0][1] * 0.396566187, scoresList[1] * 3.178718116, val[1][1] * 2.525195879, scoresList[3] * 1.757085479, scoresList[4] * 1.668158805])
                
        self.lineEdit_10.setText(str(int(abs(whm - scoresList[5]) / scoresList[5] * 100.0)) + '%')
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow,2,'144 fps',[13684,12251,2567,9023,7777,5799])
    MainWindow.show()
    sys.exit(app.exec_())

