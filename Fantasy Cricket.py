# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fc1.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

from points_calculator import player_points
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Open import Ui_Dialog as Open   
from new_team import Ui_Form as New     
from Evaluation import Ui_evaluate_team as Evaluation

import sqlite3
fant=sqlite3.connect('fandatabase.db')  
fantcurs=fant.cursor()



class Ui_MainWindow(object):
    def __init__(self):
        self.newDialog = QtWidgets.QMainWindow()
        self.new_screen = New()
        self.new_screen.setupUi(self.newDialog)

        self.EvaluateWindow = QtWidgets.QMainWindow()
        self.eval_screen = Evaluation()
        self.eval_screen.setupUi(self.EvaluateWindow)

        self.openDialog = QtWidgets.QMainWindow()
        self.open_screen = Open()
        self.open_screen.setupUi(self.openDialog)
        
    def file_open(self):
        self.open_screen.setupUi(self.openDialog)
        self.openDialog.show()
        self.open_screen.openbtn.clicked.connect(self.openteam)

    def file_evaluate(self):
        self.eval_screen.setupUi(self.EvaluateWindow)
        self.EvaluateWindow.show()

        
    def setupUi(self, MainWindow):
        self.avail_points = 1000
        self.used_points = 0
        self.totalcount = 0
        self.batsmencount = 0
        self.bowlerscount = 0
        self.alrdscount = 0
        self.wicketerscount = 0
        
        self.a = []  
        self.b = []  
        self.c = []  
        self.d = []  
        self.list1 = []
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(787, 802)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(21)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.team_name = QtWidgets.QLabel(self.centralwidget)
        
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(14)
        font.setItalic(True)
        self.team_name.setFont(font)
        self.team_name.setObjectName("team_name")
        self.verticalLayout.addWidget(self.team_name)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Batsman = QtWidgets.QLabel(self.centralwidget)
        
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Batsman.setFont(font)
        self.Batsman.setObjectName("Batsman")
        self.horizontalLayout_4.addWidget(self.Batsman)
        self.batcount = QtWidgets.QLabel(self.centralwidget)
        
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(10)
        self.batcount.setFont(font)
        self.batcount.setObjectName("batcount")
        self.horizontalLayout_4.addWidget(self.batcount)
        self.Wicketkeeepr = QtWidgets.QLabel(self.centralwidget)
        
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Wicketkeeepr.setFont(font)
        self.Wicketkeeepr.setObjectName("Wicketkeeepr")
        self.horizontalLayout_4.addWidget(self.Wicketkeeepr)
        self.wicketcount = QtWidgets.QLabel(self.centralwidget)
        
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(10)
        self.wicketcount.setFont(font)
        self.wicketcount.setObjectName("wicketcount")
        self.horizontalLayout_4.addWidget(self.wicketcount)
        self.Allrounder = QtWidgets.QLabel(self.centralwidget)
        
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Allrounder.setFont(font)
        self.Allrounder.setObjectName("Allrounder")
        self.horizontalLayout_4.addWidget(self.Allrounder)
        self.alrcount = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(10)
        self.alrcount.setFont(font)
        self.alrcount.setObjectName("alrcount")
        self.horizontalLayout_4.addWidget(self.alrcount)
        self.Bowlers = QtWidgets.QLabel(self.centralwidget)
        
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Bowlers.setFont(font)
        self.Bowlers.setObjectName("Bowlers")
        self.horizontalLayout_4.addWidget(self.Bowlers)
        self.bowlcount = QtWidgets.QLabel(self.centralwidget)
        
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(10)
        self.bowlcount.setFont(font)
        self.bowlcount.setObjectName("bowlcount")
        self.horizontalLayout_4.addWidget(self.bowlcount)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bow_rb = QtWidgets.QRadioButton(self.centralwidget)
        
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(9)
        self.bow_rb.setFont(font)
        self.bow_rb.setObjectName("bow_rb")
        self.horizontalLayout_2.addWidget(self.bow_rb)
        self.bat_rb = QtWidgets.QRadioButton(self.centralwidget)
        
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(9)
        self.bat_rb.setFont(font)
        self.bat_rb.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.bat_rb.setObjectName("bat_rb")
        self.horizontalLayout_2.addWidget(self.bat_rb)
        self.ar_rb = QtWidgets.QRadioButton(self.centralwidget)
        
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(9)
        self.ar_rb.setFont(font)
        self.ar_rb.setObjectName("ar_rb")
        self.horizontalLayout_2.addWidget(self.ar_rb)
        self.wk_rb = QtWidgets.QRadioButton(self.centralwidget)
        
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(9)
        self.wk_rb.setFont(font)
        self.wk_rb.setObjectName("wk_rb")
        self.horizontalLayout_2.addWidget(self.wk_rb)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Totalplayers = QtWidgets.QLabel(self.centralwidget)
        
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setBold(True)
        font.setWeight(75)
        self.Totalplayers.setFont(font)
        self.Totalplayers.setObjectName("Totalplayers")
        self.horizontalLayout_3.addWidget(self.Totalplayers)
        self.points_available = QtWidgets.QLabel(self.centralwidget)
        
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setBold(True)
        font.setWeight(75)
        self.points_available.setFont(font)
        self.points_available.setObjectName("points_available")
        self.horizontalLayout_3.addWidget(self.points_available)
        self.TeamName = QtWidgets.QLabel(self.centralwidget)
        
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setBold(True)
        font.setWeight(75)
        self.TeamName.setFont(font)
        self.TeamName.setObjectName("TeamName")
        self.horizontalLayout_3.addWidget(self.TeamName)
        self.points_used = QtWidgets.QLabel(self.centralwidget)
        
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setBold(True)
        font.setWeight(75)
        self.points_used.setFont(font)
        self.points_used.setObjectName("points_used")
        self.horizontalLayout_3.addWidget(self.points_used)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.availplayers_lw = QtWidgets.QListWidget(self.centralwidget)
        self.availplayers_lw.setObjectName("availplayers_lw")
        self.horizontalLayout_6.addWidget(self.availplayers_lw)
        self.selectedplayers_lw = QtWidgets.QListWidget(self.centralwidget)
        self.selectedplayers_lw.setObjectName("selectedplayers_lw")
        self.horizontalLayout_6.addWidget(self.selectedplayers_lw)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 787, 25))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.new_team = QtWidgets.QAction(MainWindow)
        self.new_team.setShortcut("Ctrl+N")
        self.new_team.triggered.connect(self.file_new)
        self.new_team.setShortcutVisibleInContextMenu(True)
        self.new_team.setObjectName("new_team")
        
        self.open_team = QtWidgets.QAction(MainWindow)
        self.open_team.setShortcut("Ctrl+O")
        self.open_team.triggered.connect(self.file_open)
        self.open_team.setShortcutVisibleInContextMenu(True)
        self.open_team.setObjectName("open_team")
        
        self.evaluate_team = QtWidgets.QAction(MainWindow)
        self.evaluate_team.setShortcut("Ctrl+E")
        self.evaluate_team.triggered.connect(self.file_evaluate)
        self.evaluate_team.setShortcutVisibleInContextMenu(True)
        self.evaluate_team.setObjectName("evaluate_team")
        
        self.save_team = QtWidgets.QAction(MainWindow)
        self.save_team.setShortcut("Ctrl+S")
        self.save_team.triggered.connect(self.file_save)
        self.save_team.setShortcutVisibleInContextMenu(True)
        self.save_team.setObjectName("save_team")
        
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuManage_Teams.addAction(self.new_team)
        self.menuManage_Teams.addAction(self.open_team)
        self.menuManage_Teams.addAction(self.evaluate_team)
        
        self.menuManage_Teams.addAction(self.save_team)
        self.menuManage_Teams.addAction(self.actionQuit)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.availplayers_lw.itemDoubleClicked.connect(self.removelist1)
        self.selectedplayers_lw.itemDoubleClicked.connect(self.removelist2)

       
        self.stats = {}

        self.new_screen.savename.clicked.connect(self.namechange)

        self.bat_rb.clicked.connect(self.load_names)
        self.wk_rb.clicked.connect(self.load_names)
        self.bow_rb.clicked.connect(self.load_names)
        self.ar_rb.clicked.connect(self.load_names)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Fantasy Cricket"))
        self.team_name.setText(_translate("MainWindow", "                                            Team Name"))
        self.Batsman.setText(_translate("MainWindow", "Batsman(BAT)"))
        self.batcount.setText(_translate("MainWindow", "##"))
        self.Wicketkeeepr.setText(_translate("MainWindow", "WicketKeeper(WK)"))
        self.wicketcount.setText(_translate("MainWindow", "##"))
        self.Allrounder.setText(_translate("MainWindow", "AllRounder(ALR)"))
        self.alrcount.setText(_translate("MainWindow", "##"))
        self.Bowlers.setText(_translate("MainWindow", "Bowler(BOWL)"))
        self.bowlcount.setText(_translate("MainWindow", "##"))
        self.bow_rb.setText(_translate("MainWindow", "Bowler"))
        self.bat_rb.setText(_translate("MainWindow", "Batsman"))
        self.ar_rb.setText(_translate("MainWindow", "All Rounder"))
        self.wk_rb.setText(_translate("MainWindow", "Wicket Keeper"))
        self.Totalplayers.setText(_translate("MainWindow", "Available Points "))
        self.points_available.setText(_translate("MainWindow", "00"))
        self.TeamName.setText(_translate("MainWindow", "Used Points"))
        self.points_used.setText(_translate("MainWindow", "00"))
        self.label_7.setText(_translate("MainWindow", "Available Players"))
        self.label_6.setText(_translate("MainWindow", "Selected Players"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.new_team.setText(_translate("MainWindow", "New Team"))
        self.new_team.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.open_team.setText(_translate("MainWindow", "Open Team"))
        self.open_team.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.evaluate_team.setText(_translate("MainWindow", "Evaluate Team"))
        self.evaluate_team.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.save_team.setText(_translate("MainWindow", "Save Team"))
        self.save_team.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

    def file_new(self):
        self.newDialog.show()

    def namechange(self):
        teamname = self.new_screen.team_name.text()
        fantcurs.execute("SELECT DISTINCT name FROM teams")
        l = fantcurs.fetchall()
        for i in l:
            if i[0] == teamname:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Team with same name already exists!!\nPlease choose another name")
                msg.setWindowTitle("Invalid Team Name")
                msg.exec_()
                return 0
        if len(teamname) == 0:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("You cannot leave the field blank!!!")
            msg.setWindowTitle("Invalid Team Name")
            msg.exec_()
            return 0
        elif teamname.isnumeric():
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Please enter a valid teamname\n(Name must contain atleast one character)!!")
            msg.setWindowTitle("Invalid Team Name")
            msg.exec_()
            return 0
        else:
            self.reset()
            self.tname = self.new_screen.team_name.text()
            self.team_name.setText('          '+self.tname)
            self.newDialog.close()
            
    def reset(self):
        self.enablebuttons()
        self.load_names()
        self.used_points = 0
        self.alrdscount = 0
        self.wicketerscount = 0
        self.batsmencount = 0
        self.bowlerscount = 0
        self.totalcount = 0
        self.avail_points = 1000
        self.points_available.setText(str(self.avail_points))
        self.points_used.setText(str(self.used_points))
        self.bowlcount.setText(str(self.bowlerscount))
        self.batcount.setText(str(self.batsmencount))
        self.alrcount.setText(str(self.alrdscount))
        self.wicketcount.setText(str(self.wicketerscount))
        self.list1.clear()
        self.load_names()

        self.selectedplayers_lw.clear()


    def file_save(self):
        if not self.error(): 
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText(' 😪Insufficient Players OR Points !!')
            msg.setWindowTitle("Fantasy Cricket")
            msg.exec_()
        elif self.error():  
            try:
                fantcurs.execute("SELECT DISTINCT name FROM teams;")
                x = fantcurs.fetchall()
                for i in x:
                    if self.team_name.text() == i[0]:   
                        print('Updating already there')
                        fantcurs.execute("DELETE  FROM teams WHERE name='" + self.team_name.text() + "';") 
            except:
                print('error')
            for i in range(self.selectedplayers_lw.count()):
               
                try:
                    fantcurs.execute("INSERT INTO teams (name,players,value) VALUES (?,?,?)",
                                     (self.team_name.text(), self.list1[i], player_points[self.list1[i]]))

                    
                except:
                    print('error in operation!')
            fant.commit()
        else:
            print('---error in operation')

    def quit(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setInformativeText(' Bye 😙')
        msg.setWindowTitle("Fantasy Cricket")
        msg.exec_()
        sys.exit()

    def load_names(self):
        Batsman = 'BAT'
        WicketKeeper = 'WK'
        Allrounder = 'AR'
        Bowler = 'BWL'
        sql1 = "SELECT player,value from stats WHERE ctg = '" + Batsman + "';"
        sql2 = "SELECT Player,value from stats WHERE ctg = '" + WicketKeeper + "';"
        sql3 = "SELECT Player,value from stats WHERE ctg ='" + Allrounder + "';"
        sql4 = "SELECT Player,value from stats WHERE ctg = '" + Bowler + "';"

        fantcurs.execute(sql1)
        x = fantcurs.fetchall()
        fantcurs.execute(sql4)
        y = fantcurs.fetchall()
        fantcurs.execute(sql3)
        z = fantcurs.fetchall()
        fantcurs.execute(sql2)
        w = fantcurs.fetchall()

        batsmen = []
        bowlers = []
        allrounders = []
        wcktkeepers = []

        for k in x:
            batsmen.append(k[0])
            self.b.append(k[0])
            self.stats[k[0]] = k[1]
        for k in y:
            bowlers.append(k[0])
            self.stats[k[0]] = k[1]
            self.a.append(k[0])
        for k in w:
            wcktkeepers.append(k[0])
            self.stats[k[0]] = k[1]
            self.d.append(k[0])
        for k in z:
            allrounders.append(k[0])
            self.stats[k[0]] = k[1]
            self.c.append(k[0])
        for i in self.list1:
            if i in allrounders:
                allrounders.remove(i)
            elif i in batsmen:
                batsmen.remove(i)
            elif i in bowlers:
                bowlers.remove(i)
            elif i in wcktkeepers:
                wcktkeepers.remove(i)

        if self.bat_rb.isChecked() == True:
            self.availplayers_lw.clear()
            for i in range(len(batsmen)):
                item = QtWidgets.QListWidgetItem(batsmen[i])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.availplayers_lw.addItem(item)
        elif self.bow_rb.isChecked() == True:
            self.availplayers_lw.clear()
            for i in range(len(bowlers)):
                item = QtWidgets.QListWidgetItem(bowlers[i])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.availplayers_lw.addItem(item)
        elif self.ar_rb.isChecked() == True:
            self.availplayers_lw.clear()
            for i in range(len(allrounders)):
                item = QtWidgets.QListWidgetItem(allrounders[i])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.availplayers_lw.addItem(item)

        elif self.wk_rb.isChecked() == True:
            self.availplayers_lw.clear()
            for i in range(len(wcktkeepers)):
                item = QtWidgets.QListWidgetItem(wcktkeepers[i])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.availplayers_lw.addItem(item)
                
    def removelist1(self, item):   
        self.conditions_1(item.text())
        self.availplayers_lw.takeItem(self.availplayers_lw.row(item))
        self.selectedplayers_lw.addItem(item.text())
        self.totalcount = self.selectedplayers_lw.count()
        self.list1.append(item.text())
        self.error()

    def conditions_1(self, cat):   
        self.avail_points -= self.stats[cat]
        self.used_points += self.stats[cat]
        if cat in self.a:
            self.bowlerscount += 1
        elif cat in self.d:
            self.wicketerscount += 1
        elif cat in self.c:
            self.alrdscount += 1
        elif cat in self.b:
            self.batsmencount += 1

        self.points_available.setText(str(self.avail_points))
        self.points_used.setText(str(self.used_points))
        self.bowlcount.setText(str(self.bowlerscount))
        self.batcount.setText(str(self.batsmencount))
        self.alrcount.setText(str(self.alrdscount))
        self.wicketcount.setText(str(self.wicketerscount))

    def conditions_2(self, cat):   
        self.avail_points += self.stats[cat]
        self.used_points -= self.stats[cat]
        if cat in self.a:
            self.bowlerscount -= 1
        elif cat in self.d:
            self.wicketerscount -= 1
        elif cat in self.c:
            self.alrdscount -= 1
        elif cat in self.b:
            self.batsmencount -= 1

        self.points_available.setText(str(self.avail_points))
        self.points_used.setText(str(self.used_points))
        self.bowlcount.setText(str(self.bowlerscount))
        self.batcount.setText(str(self.batsmencount))
        self.alrcount.setText(str(self.alrdscount))
        self.wicketcount.setText(str(self.wicketerscount))

    
    def removelist2(self, item):   
        self.selectedplayers_lw.takeItem(self.selectedplayers_lw.row(item))
        self.availplayers_lw.addItem(item.text())
        self.list1.remove(item.text())
        # self.error()
        self.totalcount = self.selectedplayers_lw.count()
        self.conditions_2(item.text())    

    def openteam(self):  
        self.reset()
        teamname = self.open_screen.open_cb.currentText()
        self.team_name.setText(teamname)
        self.enablebuttons()
        fantcurs.execute("SELECT players from teams WHERE name= '" + teamname + "';")
        x=fantcurs.fetchall()
        score=[]
        for i in x:
            fantcurs.execute("SELECT value from stats WHERE player='"+i[0]+"';")
            y=fantcurs.fetchone()
            score.append(y[0])
        
        sum=0
        for i in score:
            sum+=i
        self.selectedplayers_lw.clear()
        self.load_names()
        for i in x:
            self.selectedplayers_lw.addItem(i[0])
            self.list1.append(i[0])
            self.conditions_1(i[0])
        self.used_points = sum
        self.avail_points = 1000 - sum
        self.points_available.setText(str(self.avail_points))
        self.points_used.setText(str(self.used_points))
        self.openDialog.close()

    def enablebuttons(self):
        self.bat_rb.setEnabled(True)
        self.bow_rb.setEnabled(True)
        self.ar_rb.setEnabled(True)
        self.wk_rb.setEnabled(True)
        
    def error(self):
        msg = QMessageBox()
        if self.wicketerscount > 1:
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText('Only 1 wicketkeeper is allowed!')
            msg.setWindowTitle("Error")
            msg.exec_()
            return 0
        elif self.totalcount > 11:
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText('No more than 11 players allowed!')
            msg.setWindowTitle("Selection Error")
            msg.exec_()
            return 0
        elif self.totalcount < 11 :
            return 0
        elif self.wicketerscount < 1:
            return 0
        elif self.avail_points <= -1:
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText('Not enough points!')
            msg.setWindowTitle("Selection Cricket")
            msg.exec_()
            return 0

        return 1
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
