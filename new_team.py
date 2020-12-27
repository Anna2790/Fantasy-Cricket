# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_team.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(367, 219)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 20, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setObjectName("label")
        self.team_name = QtWidgets.QLineEdit(Form)
        self.team_name.setGeometry(QtCore.QRect(100, 70, 171, 31))
        self.team_name.setText("")
        self.team_name.setAlignment(QtCore.Qt.AlignCenter)
        self.team_name.setObjectName("team_name")
        self.savename = QtWidgets.QPushButton(Form)
        self.savename.setGeometry(QtCore.QRect(140, 130, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setBold(True)
        font.setWeight(75)
        self.savename.setFont(font)
        self.savename.setAutoDefault(True)
        self.savename.setObjectName("savename")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "New Team"))
        self.team_name.setPlaceholderText(_translate("Form", "Enter team name"))
        self.savename.setText(_translate("Form", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
