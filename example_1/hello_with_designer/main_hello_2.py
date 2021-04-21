import sys
from PyQt5 import QtWidgets
from ui_hello import Ui_Form

class QnewWidget(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.__ui=Ui_Form()
        self.__ui.setupUi(self)
        self.lab="繼承的QnewWidget"
        self.__ui.label.setText(self.lab)

    def setButtonText(self,text):
        self.__ui.pushButton.setText(text)

    def on_pushButton_clicked(self):
        print("hello hello hello")

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    new_widget=QnewWidget()
    new_widget.show()
    new_widget.setButtonText("間接設定")
    sys.exit(app.exec_())
