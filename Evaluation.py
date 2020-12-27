# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Evaluation.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Score import Ui_Dialog as Score  
import sqlite3
match= sqlite3.connect("fandatabase.db")
matchcur=match.cursor()




class Ui_evaluate_team(object):
     def __init__(self): 
        self.scoreDialog = QtWidgets.QMainWindow()
        self.score_screen = Score()
        self.score_screen.setupUi(self.scoreDialog)

     def setupUi(self, evaluate_team):
        evaluate_team.setObjectName("evaluate_team")
        evaluate_team.resize(575, 539)
        self.label = QtWidgets.QLabel(evaluate_team)
        self.label.setGeometry(QtCore.QRect(80, 30, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(evaluate_team)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 90, 511, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.selectteam_cb = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.selectteam_cb.setObjectName("selectteam_cb")
        self.horizontalLayout.addWidget(self.selectteam_cb)
        self.selectmatch_cb = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.selectmatch_cb.setObjectName("selectmatch_cb")
        self.selectmatch_cb.addItem("")
        self.selectmatch_cb.addItem("")
        self.horizontalLayout.addWidget(self.selectmatch_cb)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(evaluate_team)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 170, 511, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(evaluate_team)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 209, 511, 241))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.players_lw = QtWidgets.QListWidget(self.horizontalLayoutWidget_3)
        self.players_lw.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.players_lw.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.players_lw.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.players_lw.setObjectName("players_lw")
        self.horizontalLayout_3.addWidget(self.players_lw)
        self.scores_lw = QtWidgets.QListWidget(self.horizontalLayoutWidget_3)
        self.scores_lw.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scores_lw.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.scores_lw.setObjectName("scores_lw")
        self.horizontalLayout_3.addWidget(self.scores_lw)
        self.calcscore_btn = QtWidgets.QPushButton(evaluate_team)
        self.calcscore_btn.setGeometry(QtCore.QRect(220, 480, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setBold(True)
        font.setWeight(75)
        self.calcscore_btn.setFont(font)
        self.calcscore_btn.setObjectName("calcscore_btn")

        self.retranslateUi(evaluate_team)
        QtCore.QMetaObject.connectSlotsByName(evaluate_team)

        self.calcscore_btn.clicked.connect(self.final_score)
        selected_team = self.selectteam_cb.currentText()

        self.changedname(selected_team)

        self.selectteam_cb.currentTextChanged.connect(self.changedname)

     def retranslateUi(self, evaluate_team):
        _translate = QtCore.QCoreApplication.translate
        evaluate_team.setWindowTitle(_translate("evaluate_team", "Dialog"))
        self.label.setText(_translate("evaluate_team", "Evaluate the performance of your team"))
        self.selectmatch_cb.setCurrentText(_translate("evaluate_team", "Select Match"))
        self.selectmatch_cb.setItemText(0, _translate("evaluate_team", "Select Match"))
        self.selectmatch_cb.setItemText(1, _translate("evaluate_team", "Match 1"))
        self.label_3.setText(_translate("evaluate_team", " Players :"))
        self.label_2.setText(_translate("evaluate_team", "Points :"))
        self.calcscore_btn.setText(_translate("evaluate_team", "Calculate Score"))
        
        x = matchcur.execute("SELECT  DISTINCT name from teams;")
        team = x.fetchall()
        for i in team:
            self.selectteam_cb.addItem(i[0])
    
     def changedname(self, t):
        self.players_lw.clear()
        self.scores_lw.clear()
        y = matchcur.execute("SELECT players from teams WHERE name='" + t + "';")
        player = y.fetchall()
        for j in player:
            self.players_lw.addItem(j[0])
        z = matchcur.execute("SELECT value from teams WHERE name='" + t + "';")
        value = z.fetchall()
        for k in value:
            self.scores_lw.addItem(str(k[0]))

     def final_score(self):
        total_score=0
        t=self.selectteam_cb.currentText()   
        z = matchcur.execute("SELECT value from teams WHERE name='" + t + "';")
        value = z.fetchall()
        for k in value:
            total_score+=k[0]
        self.score_screen.finalscore.setText(str(total_score))   
        self.scoreDialog.show()
    
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    evaluate_team = QtWidgets.QDialog()
    ui = Ui_evaluate_team()
    ui.setupUi(evaluate_team)
    evaluate_team.show()
    sys.exit(app.exec_())
