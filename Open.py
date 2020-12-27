# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Open.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
match=sqlite3.connect('fandatabase.db')
matchcur=match.cursor()

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(375, 253)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(134, 39, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.open_cb = QtWidgets.QComboBox(Dialog)
        self.open_cb.setGeometry(QtCore.QRect(90, 90, 201, 31))
        self.open_cb.setObjectName("open_cb")
        self.openbtn = QtWidgets.QPushButton(Dialog)
        self.openbtn.setGeometry(QtCore.QRect(140, 150, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setBold(True)
        font.setWeight(75)
        self.openbtn.setFont(font)
        self.openbtn.setObjectName("openbtn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        teams= matchcur.execute("SELECT DISTINCT name FROM teams;")  
        y= teams.fetchall()
        for i in y:
            self.open_cb.addItem(i[0])

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Select Team"))
        self.openbtn.setText(_translate("Dialog", "Open"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
