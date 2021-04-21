import sys
from PyQt5.QtWidgets import QDialog,QApplication
from ui_Dialog import Ui_Dialog
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt, pyqtSlot

class QnewDialog(QDialog):

    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.radioButton_black.clicked.connect(self.do_setTextColor)
        self.ui.radioButton_red.clicked.connect(self.do_setTextColor)
        self.ui.radioButton_blue.clicked.connect(self.do_setTextColor)

    def on_pushButton_clear_clicked(self):
        self.ui.textEdit.clear()

    def on_checkBox_bold_toggled(self,checked):
        font=self.ui.textEdit.font()
        font.setBold(checked)       #表示選取狀態
        self.ui.textEdit.setFont(font)

    def on_checkBox_underline_clicked(self):
        checked=self.ui.checkBox_underline.isChecked()
        font=self.ui.textEdit.font()
        font.setUnderline(checked)
        self.ui.textEdit.setFont(font)

    @pyqtSlot(bool)
    def on_checkBox_italic_clicked(self,checked):
    ##def on_checkBox_italic_clicked(self):
        ##checked=self.ui.checkBox_italic.isChecked()
        font=self.ui.textEdit.font()
        font.setItalic(checked)
        self.ui.textEdit.setFont(font)

    def do_setTextColor(self):
        plet=self.ui.textEdit.palette()

        if(self.ui.radioButton_black.isChecked()):
            plet.setColor(QPalette.Text,Qt.black)

        elif(self.ui.radioButton_red.isChecked()):
            plet.setColor(QPalette.Text,Qt.red)

        elif(self.ui.radioButton_blue.isChecked()):
            plet.setColor(QPalette.Text,Qt.blue)

        self.ui.textEdit.setPalette(plet)

    def GetOutCome(self):
        print(self.ui.textEdit.toPlainText())
