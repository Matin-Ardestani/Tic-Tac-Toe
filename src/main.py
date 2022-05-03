# import libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from  PyQt5.QtWidgets import QMessageBox
import random

# - - -
# 1|2|3
# - - -
# 4|5|6
# - - -
# 7|8|9
# - - -

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
        self.onePlayer_mode()
        self.actionOne_player.triggered.connect(lambda: [self.game_reset() , self.onePlayer_mode()])
        self.actionTwo_player.triggered.connect(lambda: [self.game_reset() , self.twoPlayer_mode()])

        self.btn_list = [self.btn_1, self.btn_2, self.btn_3, self.btn_4, self.btn_5, self.btn_6, self.btn_7, self.btn_8, self.btn_9]
        self.btnedge_list = [self.btn_1, self.btn_3, self.btn_7, self.btn_9]
        self.btnmiddle_list = [self.btn_2, self.btn_4, self.btn_6, self.btn_8]

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
        
        self.click_counter = 0

    # show the winner
    def show_winner(self, winner):
        msg = QMessageBox()
        msg.setWindowTitle('YOU WON!')
        if winner == 'tie':
            msg.setText('NO ONE won the game!')
        else:
            msg.setText('The player number %s won the game!     ' % winner.upper())
        x = msg.exec_()

        # reset the game
        self.game_reset()



    def check_winning(self):


        # show the winner
        def show_winner(winner):
            msg = QMessageBox()
            msg.setWindowTitle('YOU WON!')
            if winner == 'tie':
                msg.setText('NO ONE won the game!')
            else:
                msg.setText('The player number %s won the game!     ' % winner.upper())
            x = msg.exec_()

            # reset the game
            self.game_reset()


        # horizontal winning situ for player one
        if (self.btn_1.text() == 'O' and self.btn_2.text() == 'O' and self.btn_3.text() == 'O') or (self.btn_4.text() == 'O' and self.btn_5.text() == 'O' and self.btn_6.text() == 'O') or (self.btn_7.text() == 'O' and self.btn_8.text() == 'O' and self.btn_9.text() == 'O'):
            show_winner('one')

        # vertical winning situ for player one
        elif (self.btn_1.text() == 'O' and self.btn_4.text() == 'O' and self.btn_7.text() == 'O') or (self.btn_2.text() == 'O' and self.btn_5.text() == 'O' and self.btn_8.text() == 'O') or (self.btn_3.text() == 'O' and self.btn_6.text() == 'O' and self.btn_9.text() == 'O'):
            show_winner('one')

        # oblique winning situ for player one
        elif (self.btn_1.text() == 'O' and self.btn_5.text() == 'O' and self.btn_9.text() == 'O') or (self.btn_3.text() == 'O' and self.btn_5.text() == 'O' and self.btn_7.text() == 'O'):
            show_winner('one')

            
        # horizontal winning situ for player two
        if (self.btn_1.text() == '*' and self.btn_2.text() == '*' and self.btn_3.text() == '*') or (self.btn_4.text() == '*' and self.btn_5.text() == '*' and self.btn_6.text() == '*') or (self.btn_7.text() == '*' and self.btn_8.text() == '*' and self.btn_9.text() == '*'):
            show_winner('two')

        # vertical winning situ for player two
        elif (self.btn_1.text() == '*' and self.btn_4.text() == '*' and self.btn_7.text() == '*') or (self.btn_2.text() == '*' and self.btn_5.text() == '*' and self.btn_8.text() == '*') or (self.btn_3.text() == '*' and self.btn_6.text() == '*' and self.btn_9.text() == '*'):
             show_winner('two')

        # oblique winning situ for player two
        elif (self.btn_1.text() == '*' and self.btn_5.text() == '*' and self.btn_9.text() == '*') or (self.btn_3.text() == '*' and self.btn_5.text() == '*' and self.btn_7.text() == '*'):
            show_winner('two')

        # no winner situ
        else:
            is_tie = True
            for btn in self.btn_list:
                if btn.isEnabled() == True:
                    is_tie = False
                    break
            if is_tie == True:
                show_winner('tie')

    

    # one player mode
    def onePlayer_mode(self):
        # change the mode title & status
        self.menuMode.setTitle('One Player Mode')
        self.oneplayermode_status = True
        self.twoplayermode_status = False


        def winning_move():
            # check if you can win the game
            # first row (1,2,3)
            if (self.btn_1.text() == '*') and (self.btn_3.text() == '*') and (self.btn_2.isEnabled() == True):
                next_move = self.btn_2
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1
            elif (self.btn_1.text() == '*') and (self.btn_2.text() == '*') and (self.btn_3.isEnabled() == True):
                next_move = self.btn_3
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1
            elif (self.btn_2.text() == '*') and (self.btn_3.text() == '*') and (self.btn_1.isEnabled() == True):
                next_move = self.btn_1
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1
            # third row (7,8,9)
            elif (self.btn_7.text() == '*') and (self.btn_9.text() == '*') and (self.btn_8.isEnabled() == True):
                next_move = self.btn_8
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1
            elif (self.btn_7.text() == '*') and (self.btn_8.text() == '*') and (self.btn_9.isEnabled() == True):
                next_move = self.btn_9
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1
            elif (self.btn_8.text() == '*') and (self.btn_9.text() == '*') and (self.btn_7.isEnabled() == True):
                next_move = self.btn_7
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1
            
            # first column (1,4,7)
            elif (self.btn_1.text() == '*') and (self.btn_7.text() == '*') and (self.btn_4.isEnabled() == True):
                next_move = self.btn_4
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1
            elif (self.btn_1.text() == '*') and (self.btn_4.text() == '*') and (self.btn_7.isEnabled() == True):
                next_move = self.btn_7
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1
            elif (self.btn_4.text() == '*') and (self.btn_7.text() == '*') and (self.btn_1.isEnabled() == True):
                next_move = self.btn_1
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1
            # third column (3,6,9)
            elif (self.btn_3.text() == '*') and (self.btn_9.text() == '*') and (self.btn_6.isEnabled() == True):
                next_move = self.btn_6
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1
            elif (self.btn_3.text() == '*') and (self.btn_6.text() == '*') and (self.btn_9.isEnabled() == True):
                next_move = self.btn_9
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1
            elif (self.btn_6.text() == '*') and (self.btn_9.text() == '*') and (self.btn_3.isEnabled() == True):
                next_move = self.btn_3
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1

            # first oblique (1,5,9)
            elif (self.btn_1.text() == '*') and (self.btn_5.text() == '*') and (self.btn_9.isEnabled() == True): # (1,5, )
                next_move = self.btn_9
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1
            elif (self.btn_1.text() == '*') and (self.btn_9.text() == '*') and (self.btn_5.isEnabled() == True): # (1, ,9)
                next_move = self.btn_5
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1
            elif (self.btn_5.text() == '*') and (self.btn_9.text() == '*') and (self.btn_1.isEnabled() == True): # ( ,5,9)
                next_move = self.btn_1
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1
            # second oblique (3,5,7)
            elif (self.btn_3.text() == '*') and (self.btn_5.text() == '*') and (self.btn_7.isEnabled() == True):
                next_move = self.btn_7
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1
            elif (self.btn_3.text() == '*') and (self.btn_7.text() == '*') and (self.btn_5.isEnabled() == True):
                next_move = self.btn_5
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1
            elif (self.btn_5.text() == '*') and (self.btn_7.text() == '*') and (self.btn_3.isEnabled() == True):
                next_move = self.btn_3
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1
            else:
                return False # cannot win

        # prevent from losing situations
        def prevent_losing():
            # first row situ (1,2,3)
            if (self.btn_1.text() == 'O') and (self.btn_2.text() == 'O') and (self.btn_3.text() != 'O' and self.btn_3.isEnabled() == True): # (O,O, ) , (1,2,3)
                next_move = self.btn_3
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1
                
                
            elif (self.btn_1.text() == 'O') and (self.btn_2.text() != 'O' and self.btn_2.isEnabled() == True) and (self.btn_3.text() == 'O'): # (O, ,O) , (1,2,3)
                next_move = self.btn_2
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1
                
            elif (self.btn_1.text() != 'O' and self.btn_1.isEnabled() == True) and (self.btn_2.text() == 'O') and (self.btn_3.text() == 'O'): # ( ,O,O) , (1,2,3)
                next_move = self.btn_1
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1
                

            # second row situ (4,5,6)
            elif (self.btn_4.text() == 'O') and (self.btn_5.text() == 'O') and (self.btn_6.text() != 'O' and self.btn_6.isEnabled() == True): # (O,O, ) , (4,5,6)
                next_move = self.btn_6
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1
                
            elif (self.btn_4.text() == 'O') and (self.btn_5.text() != 'O' and self.btn_5.isEnabled() == True) and (self.btn_6.text() == 'O'): # (O, ,O) , (4,5,6)
                next_move = self.btn_5
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1
                
            elif (self.btn_4.text() != 'O' and self.btn_4.isEnabled() == True) and (self.btn_5.text() == 'O') and (self.btn_6.text() == 'O'): # ( ,O,O) , (4,5,6)
                next_move = self.btn_4
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1
                

            # third row situ (7,8,9)
            elif (self.btn_7.text() == 'O') and (self.btn_8.text() == 'O') and (self.btn_9.text() != 'O' and self.btn_9.isEnabled() == True): # (O,O, ) , (7,8,9)
                next_move = self.btn_9
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1
                
            elif (self.btn_7.text() == 'O') and (self.btn_8.text() != 'O' and self.btn_8.isEnabled() == True) and (self.btn_9.text() == 'O'): # (O, ,O) , (7,8,9)
                next_move = self.btn_8
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1
                
            elif (self.btn_7.text() != 'O' and self.btn_7.isEnabled() == True) and (self.btn_8.text() == 'O') and (self.btn_9.text() == 'O'): # ( ,O,O) , (7,8,9)
                next_move = self.btn_7
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1

            
            # first column (1,3,7)
            elif (self.btn_1.text() == 'O') and (self.btn_4.text() == 'O') and (self.btn_7.text() != 'O' and self.btn_7.isEnabled() == True): # (O,O, ) , (1,4,7)
                next_move = self.btn_7
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1

            elif (self.btn_1.text() == 'O') and (self.btn_4.text() != 'O' and self.btn_4.isEnabled() == True) and (self.btn_7.text() == 'O'): # (O, ,O) , (1,4,7)
                next_move = self.btn_4
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1

            elif (self.btn_1.text() != 'O' and self.btn_1.isEnabled() == True) and (self.btn_4.text() == 'O') and (self.btn_7.text() == 'O'): # ( ,O,O) , (1,4,7)
                next_move = self.btn_1
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1


            # second column (2,5,8)
            elif (self.btn_2.text() == 'O') and (self.btn_5.text() == 'O') and (self.btn_8.text() != 'O' and self.btn_8.isEnabled() == True): # (O,O, ) , (2,5,8)
                next_move = self.btn_8
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1

            elif (self.btn_2.text() == 'O') and (self.btn_5.text() != 'O' and self.btn_5.isEnabled() == True) and (self.btn_8.text() == 'O'): # (O, ,O) , (2,5,8)
                next_move = self.btn_5
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1

            elif (self.btn_2.text() != 'O' and self.btn_2.isEnabled() == True) and (self.btn_5.text() == 'O') and (self.btn_8.text() == 'O'): # ( ,O,O) , (2,5,8)
                next_move = self.btn_2
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1


            # third column (3,6,9)
            elif (self.btn_3.text() == 'O') and (self.btn_6.text() == 'O') and (self.btn_9.text() != 'O' and self.btn_9.isEnabled() == True): # (O,O, ) , (3,6,9)
                next_move = self.btn_9
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1

            elif (self.btn_3.text() == 'O') and (self.btn_6.text() != 'O'  and self.btn_6.isEnabled() == True) and (self.btn_9.text() == 'O'): # (O, ,O) , (3,6,9)
                next_move = self.btn_6
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1

            elif (self.btn_3.text() != 'O' and self.btn_3.isEnabled() == True) and (self.btn_6.text() == 'O') and (self.btn_9.text() == 'O'): # ( ,O,O) , (3,6,9)
                next_move = self.btn_3
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1


            # oblique situ one (1,5,9)
            elif (self.btn_1.text() == 'O') and (self.btn_5.text() == 'O') and (self.btn_9.text() != 'O' and self.btn_9.isEnabled() == True): # (O,O, ) , (1,5,9)
                next_move = self.btn_9
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1

            elif (self.btn_1.text() == 'O') and (self.btn_5.text() != 'O' and self.btn_5.isEnabled() == True) and (self.btn_9.text() == 'O'): # (O, ,O) , (1,5,9)
                next_move = self.btn_5
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1

            elif (self.btn_1.text() != 'O' and self.btn_1.isEnabled() == True) and (self.btn_5.text() == 'O') and (self.btn_9.text() == 'O'): # ( ,O,O) , (1,5,9)
                next_move = self.btn_1
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1


            # oblique situ two (3,5,7)
            elif (self.btn_3.text() == 'O') and (self.btn_5.text() == 'O') and (self.btn_7.text() != 'O' and self.btn_7.isEnabled() == True): # (O,O, ) , (3,5,7)
                next_move = self.btn_7
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1

            elif (self.btn_3.text() == 'O') and (self.btn_5.text() != 'O' and self.btn_5.isEnabled() == True) and (self.btn_7.text() == 'O'): # (O, ,O) , (3,5,7)
                next_move = self.btn_5
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1

            elif (self.btn_3.text() != 'O' and self.btn_3.isEnabled() == True) and (self.btn_5.text() == 'O') and (self.btn_7.text() == 'O'): # ( ,O,O) , (3,5,7)
                next_move = self.btn_3
                next_move.setText('*')
                next_move.setEnabled(False)
                self.click_counter += 1

            else:
                return True # there is no danger

        # do my move
        if self.click_counter % 2 != 0: # check if it's my turn

            # ----------------------first move ( corners )
            if self.click_counter == 1:
                # if the player's move was in corner
                for pre_move in self.btnedge_list:
                    if pre_move.isEnabled() == False:
                        next_move = pre_move
                        while next_move == pre_move:
                            next_move = random.choice(self.btnedge_list)
                        next_move.setText('*')
                        next_move.setEnabled(False)
                        self.click_counter += 1
                        break
                
                # if the player's move was in middle or center
                for pre_move in self.btnmiddle_list:
                    if (pre_move.isEnabled() == False) or (self.btn_5.isEnabled() == False):
                        next_move = random.choice(self.btnedge_list)
                        next_move.setText('*')
                        next_move.setEnabled(False)
                        self.click_counter += 1
                        break


            # ----------------------second move
            elif self.click_counter == 3:
                # prevent losing the game
                if prevent_losing() == True: # no danger ( you can move for winning not stop losing )
                    # first edge (1)
                    if self.btn_1.text() == '*':
                        if (self.btn_2.isEnabled() == True) and (self.btn_3.isEnabled() == True): # vertical
                            next_move = self.btn_3
                            next_move.setText('*')
                            next_move.setEnabled(False)
                            self.click_counter += 1
                        elif (self.btn_4.isEnabled() == True) and (self.btn_7.isEnabled() == True): # horizontal
                            next_move = self.btn_7
                            next_move.setText('*')
                            next_move.setEnabled(False)
                            self.click_counter += 1
                        elif (self.btn_5.isEnabled() == True) and (self.btn_9.isEnabled() == True): # blique
                            next_move = self.btn_5
                            next_move.setText('*')
                            next_move.setEnabled(False)
                            self.click_counter += 1

                    # second edge (3)
                    elif self.btn_3.text() == '*':
                        if (self.btn_2.isEnabled() == True) and (self.btn_1.isEnabled() == True): # vertical
                            next_move = self.btn_1
                            next_move.setText('*')
                            next_move.setEnabled(False)
                            self.click_counter += 1
                        elif (self.btn_6.isEnabled() == True) and (self.btn_9.isEnabled() == True): # horizontal
                            next_move = self.btn_9
                            next_move.setText('*')
                            next_move.setEnabled(False)
                            self.click_counter += 1
                        elif (self.btn_5.isEnabled() == True) and (self.btn_7.isEnabled() == True): # blique
                            next_move = self.btn_5
                            next_move.setText('*')
                            next_move.setEnabled(False)
                            self.click_counter += 1

                    # third edge (7)
                    elif self.btn_7.text() == '*':
                        if (self.btn_4.isEnabled() == True) and (self.btn_1.isEnabled() == True): # vertical
                            next_move = self.btn_1
                            next_move.setText('*')
                            next_move.setEnabled(False)
                            self.click_counter += 1
                        elif (self.btn_8.isEnabled() == True) and (self.btn_9.isEnabled() == True): # horizontal
                            next_move = self.btn_9
                            next_move.setText('*')
                            next_move.setEnabled(False)
                            self.click_counter += 1
                        elif (self.btn_5.isEnabled() == True) and (self.btn_3.isEnabled() == True): # blique
                            next_move = self.btn_5
                            next_move.setText('*')
                            next_move.setEnabled(False)
                            self.click_counter += 1

                    # forth edge (9)
                    elif self.btn_9.text() == '*':
                        if (self.btn_6.isEnabled() == True) and (self.btn_3.isEnabled() == True): # vertical
                            next_move = self.btn_3
                            next_move.setText('*')
                            next_move.setEnabled(False)
                            self.click_counter += 1
                        elif (self.btn_8.isEnabled() == True) and (self.btn_7.isEnabled() == True): # horizontal
                            next_move = self.btn_7
                            next_move.setText('*')
                            next_move.setEnabled(False)
                            self.click_counter += 1
                        elif (self.btn_5.isEnabled() == True) and (self.btn_1.isEnabled() == True): # blique
                            next_move = self.btn_5
                            next_move.setText('*')
                            next_move.setEnabled(False)
                            self.click_counter += 1
                            

            # ----------------------third move
            elif self.click_counter == 5:

                
                if winning_move() == False:
                
                
                    # no danger
                    if prevent_losing() == True: # prevent losing the game
                        # first edge (1)
                        if (self.btn_1.text() == '*') and (self.btn_2.isEnabled() == True) and (self.btn_3.isEnabled() == True): # vertical
                            next_move = self.btn_3
                            next_move.setText('*')
                            next_move.setEnabled(False)
                            self.click_counter += 1
                        elif (self.btn_1.text() == '*') and (self.btn_4.isEnabled() == True) and (self.btn_7.isEnabled() == True): # horizontal
                            next_move = self.btn_7
                            next_move.setText('*')
                            next_move.setEnabled(False)
                            self.click_counter += 1
                        elif (self.btn_1.text() == '*') and (self.btn_5.isEnabled() == True) and (self.btn_9.isEnabled() == True): # blique
                            next_move = self.btn_5
                            next_move.setText('*')
                            next_move.setEnabled(False)
                            self.click_counter += 1

                        # second edge (3)
                        elif (self.btn_3.text() == '*') and (self.btn_2.isEnabled() == True) and (self.btn_1.isEnabled() == True): # vertical
                            next_move = self.btn_1
                            next_move.setText('*')
                            next_move.setEnabled(False)
                            self.click_counter += 1
                        elif (self.btn_3.text() == '*') and (self.btn_6.isEnabled() == True) and (self.btn_9.isEnabled() == True): # horizontal
                            next_move = self.btn_9
                            next_move.setText('*')
                            next_move.setEnabled(False)
                            self.click_counter += 1
                        elif (self.btn_3.text() == '*') and (self.btn_5.isEnabled() == True) and (self.btn_7.isEnabled() == True): # blique
                            next_move = self.btn_5
                            next_move.setText('*')
                            next_move.setEnabled(False)
                            self.click_counter += 1

                        # third edge (7)
                        elif (self.btn_7.text() == '*') and (self.btn_4.isEnabled() == True) and (self.btn_1.isEnabled() == True): # vertical
                            next_move = self.btn_1
                            next_move.setText('*')
                            next_move.setEnabled(False)
                            self.click_counter += 1
                        elif (self.btn_7.text() == '*') and (self.btn_8.isEnabled() == True) and (self.btn_9.isEnabled() == True): # horizontal
                            next_move = self.btn_9
                            next_move.setText('*')
                            next_move.setEnabled(False)
                            self.click_counter += 1
                        elif (self.btn_7.text() == '*') and (self.btn_5.isEnabled() == True) and (self.btn_3.isEnabled() == True): # blique
                            next_move = self.btn_5
                            next_move.setText('*')
                            next_move.setEnabled(False)
                            self.click_counter += 1

                        # forth edge (9)
                        elif (self.btn_9.text() == '*') and (self.btn_6.isEnabled() == True) and (self.btn_3.isEnabled() == True): # vertical
                            next_move = self.btn_3
                            next_move.setText('*')
                            next_move.setEnabled(False)
                            self.click_counter += 1
                        elif (self.btn_9.text() == '*') and (self.btn_8.isEnabled() == True) and (self.btn_7.isEnabled() == True): # horizontal
                            next_move = self.btn_7
                            next_move.setText('*')
                            next_move.setEnabled(False)
                            self.click_counter += 1
                        elif (self.btn_9.text() == '*') and (self.btn_5.isEnabled() == True) and (self.btn_1.isEnabled() == True): # blique
                            next_move = self.btn_5
                            next_move.setText('*')
                            next_move.setEnabled(False)
                            self.click_counter += 1

                        # center (5)
                        elif (self.btn_5.text() == '*') and (self.btn_2.isEnabled() == True) and (self.btn_8.isEnabled() == True): # vertical
                            # good situation for (2)
                            if (self.btn_1.text() == '*') or (self.btn_3.text() == '*'):
                                next_move = self.btn_2
                                next_move.setText('*')
                                next_move.setEnabled(False)
                                self.click_counter += 1
                            elif (self.btn_7.text() == '*') or (self.btn_9.text() == '*'):
                                # good situation for (8)
                                next_move = self.btn_8
                                next_move.setText('*')
                                next_move.setEnabled(False)
                                self.click_counter += 1
                        elif (self.btn_5.text() == '*') and (self.btn_4.isEnabled() == True) and (self.btn_6.isEnabled() == True):
                            if (self.btn_1.text() == '*') or (self.btn_7.text() == '*'):
                                # good situation for (4)
                                next_move = self.btn_4
                                next_move.setText('*')
                                next_move.setEnabled(False)
                                self.click_counter += 1
                            elif (self.btn_3.text() == '*') or (self.btn_9.text() == '*'):
                                # good situation for (6)
                                next_move = self.btn_6
                                next_move.setText('*')
                                next_move.setEnabled(False)
                                self.click_counter += 1
                        elif (self.btn_5.text() == '*') and (self.btn_1.isEnabled() == True) and (self.btn_9.isEnabled() == True):
                            if (self.btn_4.text() == '*') or (self.btn_7.text() == '*') or (self.btn_2.text() == '*') or (self.btn_3.text() == '*'):
                                # good situation for (1)
                                next_move = self.btn_1
                                next_move.setText('*')
                                next_move.setEnabled(False)
                                self.click_counter += 1
                            elif (self.btn_3.text() == '*') or (self.btn_6.text() == '*') or (self.btn_8.text() == '*') or (self.btn_7.text() == '*'):
                                # good situation for (9)
                                next_move = self.btn_9
                                next_move.setText('*')
                                next_move.setEnabled(False)
                                self.click_counter += 1
                        elif (self.btn_5.text() == '*') and (self.btn_3.isEnabled() == True) and (self.btn_7.isEnabled() == True):
                            if (self.btn_6.text() == '*') or (self.btn_9.text() == '*') or (self.btn_2.text() == '*') or (self.btn_1.text() == '*'):
                                # good situation for (3)
                                next_move = self.btn_3
                                next_move.setText('*')
                                next_move.setEnabled(False)
                                self.click_counter += 1
                            elif (self.btn_8.text() == '*') or (self.btn_9.text() == '*') or (self.btn_1.text() == '*') or (self.btn_4.text() == '*'):
                                # good situation for (7)
                                next_move = self.btn_7
                                next_move.setText('*')
                                next_move.setEnabled(False)
                                self.click_counter += 1

                        # middle (2)
                        elif (self.btn_2.text() == '*') and (self.btn_1.isEnabled() == True) and (self.btn_3.isEnabled() == True): # horizontal (1, ,3)
                            next_move = random.choice([self.btn_1, self.btn_3])
                            next_move.setText('*')
                            next_move.setEnabled(False)
                            self.click_counter += 1

                        # middle (4)
                        elif (self.btn_4.text() == '*') and (self.btn_1.isEnabled() == True) and (self.btn_7.isEnabled() == True): # vertical (1, ,7)
                            next_move = random.choice([self.btn_1, self.btn_7])
                            next_move.setText('*')
                            next_move.setEnabled(False)
                            self.click_counter += 1

                        # middle (6)
                        elif (self.btn_6.text() == '*') and (self.btn_3.isEnabled() == True) and (self.btn_9.isEnabled() == True): # vertical (3, ,9)
                            next_move = random.choice([self.btn_3, self.btn_9])
                            next_move.setText('*')
                            next_move.setEnabled(False)
                            self.click_counter += 1

                        # middle (8)
                        elif (self.btn_8.text() == '*') and (self.btn_7.isEnabled() == True) and (self.btn_9.isEnabled() == True): # horizontal (7, ,9)
                            next_move = random.choice([self.btn_7, self.btn_9])
                            next_move.setText('*')
                            next_move.setEnabled(False)
                            self.click_counter += 1

                        else:
                            next_move = self.btn_1
                            while next_move.isEnabled() == False:
                                next_move = random.choice(self.btn_list)

                            next_move.setText('*')
                            next_move.setEnabled(False)
                            self.click_counter += 1

                        




                self.check_winning() # check if the game is over



            # ----------------------forth move
            elif self.click_counter == 7:
                self.check_winning()
                
                if self.click_counter == 7:
                    if winning_move() == False: # check if you can win
                        # no danger
                        if prevent_losing() == True: # prevent losing the game
                            next_move = self.btn_1
                            while next_move.isEnabled() == False:
                                next_move = random.choice(self.btn_list)

                            next_move.setText('*')
                            next_move.setEnabled(False)
                            self.click_counter += 1
                        

                self.check_winning()


            # ----------------------fifth move ( for the competiter )
            elif self.click_counter == 9:
                self.check_winning()


            # show the move
            # next_move.setText('*')
            # next_move.setEnabled(False)
            # self.click_counter += 1
        



    # two player mode
    def twoPlayer_mode(self):
        # change the mode title & status
        self.menuMode.setTitle('Two Player Mode')
        self.oneplayermode_status = False
        self.twoplayermode_status = True

        # check if we have a winnner
        if self.click_counter >= 5: # there have to be at least 5 clickes to have a winner
            self.check_winning()
            

        


# Run the app
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
