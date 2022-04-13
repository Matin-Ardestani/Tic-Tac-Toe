# import libraries
from PyQt5 import QtCore, QtGui, QtWidgets

# main window class
class Ui_MainWindow(object):
    #==================================Designer's codes==================================
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(400, 200, 200, 200))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.btn_6.setFont(font)
        self.btn_6.setText("")
        self.btn_6.setObjectName("btn_6")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(200, 400, 200, 200))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.btn_8.setFont(font)
        self.btn_8.setText("")
        self.btn_8.setObjectName("btn_8")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(0, 0, 200, 200))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(50)
        self.btn_1.setFont(font)
        self.btn_1.setText("")
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(200, 0, 200, 200))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.btn_2.setFont(font)
        self.btn_2.setText("")
        self.btn_2.setObjectName("btn_2")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(200, 200, 200, 200))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.btn_5.setFont(font)
        self.btn_5.setText("")
        self.btn_5.setObjectName("btn_5")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(400, 400, 200, 200))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.btn_9.setFont(font)
        self.btn_9.setText("")
        self.btn_9.setObjectName("btn_9")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(400, 0, 200, 200))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.btn_3.setFont(font)
        self.btn_3.setText("")
        self.btn_3.setObjectName("btn_3")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(0, 200, 200, 200))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.btn_4.setFont(font)
        self.btn_4.setText("")
        self.btn_4.setObjectName("btn_4")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(0, 400, 200, 200))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.btn_7.setFont(font)
        self.btn_7.setText("")
        self.btn_7.setObjectName("btn_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        self.menuMode = QtWidgets.QMenu(self.menubar)
        self.menuMode.setObjectName("menuMode")
        MainWindow.setMenuBar(self.menubar)
        self.actionOne_player = QtWidgets.QAction(MainWindow)
        self.actionOne_player.setObjectName("actionOne_player")
        self.actionTwo_player = QtWidgets.QAction(MainWindow)
        self.actionTwo_player.setObjectName("actionTwo_player")
        self.menuMode.addAction(self.actionOne_player)
        self.menuMode.addAction(self.actionTwo_player)
        self.menubar.addAction(self.menuMode.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #===========================My Codes===========================================
        self.actionOne_player.triggered.connect(lambda: [self.menuMode.setTitle('One Player Mode') , self.onePlayer_mode()]) # change the btn name and call the functionsself.menuMode.setTitle('One Player Mode')
        self.actionTwo_player.triggered.connect(lambda: [self.menuMode.setTitle('Two Player Mode') , self.TwoPlayer_mode()]) # change the btn name and call the functionsself.menuMode.setTitle('One Player Mode')

    #===============================Designer's functions================================
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuMode.setTitle(_translate("MainWindow", "Mode"))
        self.actionOne_player.setText(_translate("MainWindow", "One Player Mode"))
        self.actionTwo_player.setText(_translate("MainWindow", "Two Player Mode"))


    #===============================My functions=======================================
    def onePlayer_mode(self):
        print('one')

    def TwoPlayer_mode(self):
        print('two')


# Run the app
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
