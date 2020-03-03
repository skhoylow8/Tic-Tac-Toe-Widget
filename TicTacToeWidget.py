#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 11:53:59 2020

@author: Setareh Khoylow
"""
#%%
# To run this code:
# 1. open up terminal (on Mac) or Anaconda Prompt (on Windows);
# 2. type 'cd [the directory where you have saved this file]';
# 3. then type 'python TicTacToeWidget.py 1'.

import sys

#%%
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QPushButton, QMessageBox)

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.turn = 0 #keeps track of who's turn it is
        self.initUI()

    def OX(self): #determines what symbol to place based on who's turn it is
        if self.turn % 2 == 0:
            return 'O'
        return 'X'

    def initUI(self):
        self.setWindowTitle('Os and Xs') #title of the window

        bw, bh = 100, 100     # this is the height and width of the window

        self.initGeo(bw, bh)  # geometry : pass in the button width and height
        self.initBtn(bw, bh)  # buttons
        self.initSta()        # statuses: X, O, None
        self.show() #shows the window

    def initGeo(self, bw, bh):
        self.setGeometry(100, 100, 3*bw, (7*bh) // 2) #// = floor division (round up)
        #the boad will be placed in 100 by 100 on the screen
        #the board will be 3 x width of button
        #the height of the window will be 7 x height / 2

    def initBtn(self, bw, bh):
        self.initOXs(bw, bh)  # X/O board
        self.initRes(bw, bh)  # restart

    def initSta(self):
        self.status = [None] * 9 #this creates a list that stores 9 Nones
        #once a button is clicked then the None will be changes either to a O or X

    def initOXs(self, bw, bh):
        self.OX_btns = [] #this stores the list of buttons
        #self.OX_btns[0]... self.OX_btns[8]

        for i in range(9):
            btn = QPushButton('', self) #they are originally not going to say anything hence '' and it is within self (the window)
            btn.move((i%3) * bw, (i//3) * bh)
            btn.resize(bw, bh)

            btn.setCheckable(True) #want this to be checkable to see if a value is already there
            btn.clicked.connect(self.OXs_func)

            self.OX_btns.append(btn) #this stores all the buttons in the list

    def initRes(self, bw, bh):
        btn = QPushButton('Restart', self)
        btn.move(0, 3*bh)
        btn.resize(3*bw, bh//2) #its size is 3 times the width and half the height

        btn.clicked.connect(self.restart_func)

    def OXs_func(self):
        btn = self.sender() #this returns the button that sent the signal

        if btn.isChecked():           
            btn.setCheckable(False)   #this will make check to be false forever so you can't click on them ever again
            btn.setText(self.OX()) # sets the buttons text either to a O or X

            i = self.OX_btns.index(btn) #this asks for the index of that button
            self.status[i] = self.OX() #this stores the status of the button (O or X) in the list called status above 

            self.checkStatus()

    def checkStatus(self):
        end = ((self.status[0] == self.status[1] == self.status[2] != None) or
               (self.status[3] == self.status[4] == self.status[5] != None) or
               (self.status[6] == self.status[7] == self.status[8] != None) or
               (self.status[0] == self.status[3] == self.status[6] != None) or
               (self.status[1] == self.status[4] == self.status[7] != None) or
               (self.status[2] == self.status[5] == self.status[8] != None) or
               (self.status[0] == self.status[4] == self.status[8] != None) or
               (self.status[2] == self.status[4] == self.status[6] != None))
        if end: #if someone got TicTacToe then display this message box
            msgBox = QMessageBox(self)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.setText(self.OX() + ' wins!!')
            msgBox.show()

            self.stop() #if the game comes to an end then we call a stop function
        self.turn += 1

    def stop(self):
        for btn in self.OX_btns:
            btn.setCheckable(False)

    def restart_func(self):
        self.initSta()

        for btn in self.OX_btns:
            btn.setText('')
            btn.setCheckable(True)

def main1():
    app = QApplication([])
    w = MyWidget() #w is self
    app.exec_()

if len(sys.argv) == 2 and sys.argv[1] == '1':
    main1()