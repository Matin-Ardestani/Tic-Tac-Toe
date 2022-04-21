# import libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from  PyQt5.QtWidgets import QMessageBox

# main window class
class Ui_MainWindow(object):
    #==================================Designer's codes==================================
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(600, 622)
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
        # set game mode
        self.oneplayermode_status = False
        self.twoplayermode_status = True
        self.click_counter = 0
        self.twoPlayer_mode()
        self.actionOne_player.triggered.connect(lambda: [self.game_reset() , self.onePlayer_mode()])
        self.actionTwo_player.triggered.connect(lambda: [self.game_reset() , self.twoPlayer_mode()])

        self.btn_list = [self.btn_1, self.btn_2, self.btn_3, self.btn_4, self.btn_5, self.btn_6, self.btn_7, self.btn_8, self.btn_9]

        # change btn colors when the are disabled
        for btn in self.btn_list:
            btn.setStyleSheet('''
                QPushButton:disabled{
                    color: #000000;
                }
            ''')

        # click counter
        
        self.btn_1.clicked.connect(lambda: self.clickCounter(self.btn_1))
        self.btn_2.clicked.connect(lambda: self.clickCounter(self.btn_2))
        self.btn_3.clicked.connect(lambda: self.clickCounter(self.btn_3))
        self.btn_4.clicked.connect(lambda: self.clickCounter(self.btn_4))
        self.btn_5.clicked.connect(lambda: self.clickCounter(self.btn_5))
        self.btn_6.clicked.connect(lambda: self.clickCounter(self.btn_6))
        self.btn_7.clicked.connect(lambda: self.clickCounter(self.btn_7))
        self.btn_8.clicked.connect(lambda: self.clickCounter(self.btn_8))
        self.btn_9.clicked.connect(lambda: self.clickCounter(self.btn_9))

    #===============================Designer's functions================================
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuMode.setTitle(_translate("MainWindow", "Mode"))
        self.actionOne_player.setText(_translate("MainWindow", "One Player Mode"))
        self.actionTwo_player.setText(_translate("MainWindow", "Two Player Mode"))


    #===============================My functions=======================================
    # click counter
    def clickCounter(self, btn_number):
        self.click_counter += 1

        # show the signs
        if self.click_counter % 2 == 0:
            btn_number.setText('*')
        else:
            btn_number.setText('O')
        
        # disable the btn
        btn_number.setEnabled(False)

        # check the situation
        if self.oneplayermode_status == True:
            self.onePlayer_mode()
        elif self.twoplayermode_status == True:
            self.twoPlayer_mode()


    # reset the game
    def game_reset(self):
        for btn in self.btn_list:
            btn.setEnabled(True)
            btn.setText('')

    # show the winner
    def show_winner(self, winner):
        msg = QMessageBox()
        msg.setWindowTitle('YOU WON!')
        msg.setText('The player number %s won the game!     ' % winner.upper())
        x = msg.exec_()

        # reset the game
        self.game_reset()


    

    # one player mode
    def onePlayer_mode(self):
        # change the mode title & status
        self.menuMode.setTitle('One Player Mode')
        self.oneplayermode_status = True
        self.twoplayermode_status = False

        print('one')
        



    # two player mode
    def twoPlayer_mode(self):
        # change the mode title & status
        self.menuMode.setTitle('Two Player Mode')
        self.oneplayermode_status = False
        self.twoplayermode_status = True

        # check if we have a winnner
        if self.click_counter >= 5: # there have to be at least 5 clickes to have a winner

            # horizonal winning situ for player one
            if (self.btn_1.text() == 'O' and self.btn_2.text() == 'O' and self.btn_3.text() == 'O') or (self.btn_4.text() == 'O' and self.btn_5.text() == 'O' and self.btn_6.text() == 'O') or (self.btn_7.text() == 'O' and self.btn_8.text() == 'O' and self.btn_9.text() == 'O'):
                self.show_winner('one')

            # vertical winning situ for player one
            elif (self.btn_1.text() == 'O' and self.btn_4.text() == 'O' and self.btn_7.text() == 'O') or (self.btn_2.text() == 'O' and self.btn_5.text() == 'O' and self.btn_8.text() == 'O') or (self.btn_3.text() == 'O' and self.btn_6.text() == 'O' and self.btn_9.text() == 'O'):
                self.show_winner('one')

            # oblique winning situ for player one
            elif (self.btn_1.text() == 'O' and self.btn_5.text() == 'O' and self.btn_9.text() == 'O') or (self.btn_3.text() == 'O' and self.btn_5.text() == 'O' and self.btn_7.text() == 'O'):
                self.show_winner('one')

            
            # horizonal winning situ for player two
            if (self.btn_1.text() == '*' and self.btn_2.text() == '*' and self.btn_3.text() == '*') or (self.btn_4.text() == '*' and self.btn_5.text() == '*' and self.btn_6.text() == '*') or (self.btn_7.text() == '*' and self.btn_8.text() == '*' and self.btn_9.text() == '*'):
                self.show_winner('two')

            # vertical winning situ for player two
            elif (self.btn_1.text() == '*' and self.btn_4.text() == '*' and self.btn_7.text() == '*') or (self.btn_2.text() == '*' and self.btn_5.text() == '*' and self.btn_8.text() == '*') or (self.btn_3.text() == '*' and self.btn_6.text() == '*' and self.btn_9.text() == '*'):
                self.show_winner('two')

            # oblique winning situ for player two
            elif (self.btn_1.text() == '*' and self.btn_5.text() == '*' and self.btn_9.text() == '*') or (self.btn_3.text() == '*' and self.btn_5.text() == '*' and self.btn_7.text() == '*'):
                self.show_winner('two')

        


# Run the app
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
