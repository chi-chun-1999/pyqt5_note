import sys
from PyQt5 import QtWidgets
import ui_hello

app=QtWidgets.QApplication(sys.argv)

widget=QtWidgets.QWidget()                  #建立視窗
widget.setWindowTitle("hello widget")

ui = ui_hello.Ui_Form()
ui.setupUi(widget)

widget.show()
##ui.label.setText("hello, 程式被修改")
sys.exit(app.exec_())
