# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(321, 277)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 60, 291, 41))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_underline = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_underline.setObjectName("checkBox_underline")
        self.horizontalLayout_2.addWidget(self.checkBox_underline)
        self.checkBox_italic = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_italic.setObjectName("checkBox_italic")
        self.horizontalLayout_2.addWidget(self.checkBox_italic)
        self.checkBox_bold = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_bold.setObjectName("checkBox_bold")
        self.horizontalLayout_2.addWidget(self.checkBox_bold)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(20, 110, 291, 87))
        self.textEdit.setObjectName("textEdit")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 291, 41))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_black = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_black.setObjectName("radioButton_black")
        self.horizontalLayout.addWidget(self.radioButton_black)
        self.radioButton_red = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_red.setObjectName("radioButton_red")
        self.horizontalLayout.addWidget(self.radioButton_red)
        self.radioButton_blue = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_blue.setObjectName("radioButton_blue")
        self.horizontalLayout.addWidget(self.radioButton_blue)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 200, 291, 54))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(6, 6, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pushButton_clear = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.horizontalLayout_3.addWidget(self.pushButton_clear)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.pushButton_sure = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_sure.setObjectName("pushButton_sure")
        self.horizontalLayout_3.addWidget(self.pushButton_sure)
        self.pushButton_exit = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.horizontalLayout_3.addWidget(self.pushButton_exit)

        self.retranslateUi(Dialog)
        self.pushButton_sure.clicked.connect(Dialog.accept)
        self.pushButton_exit.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.checkBox_underline.setText(_translate("Dialog", "underline"))
        self.checkBox_italic.setText(_translate("Dialog", "italic"))
        self.checkBox_bold.setText(_translate("Dialog", "bold"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">hello world </span></p></body></html>"))
        self.radioButton_black.setText(_translate("Dialog", "black"))
        self.radioButton_red.setText(_translate("Dialog", "red"))
        self.radioButton_blue.setText(_translate("Dialog", "blue"))
        self.pushButton_clear.setText(_translate("Dialog", "clear"))
        self.pushButton_sure.setText(_translate("Dialog", "sure"))
        self.pushButton_exit.setText(_translate("Dialog", "exit"))
