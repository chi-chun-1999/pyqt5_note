import sys
from PyQt5 import QtCore, QtGui, QtWidgets

widget_width=300
widget_height=200

app=QtWidgets.QApplication(sys.argv)
widget=QtWidgets.QWidget()                  #建立視窗
widget.resize(widget_width,widget_height)   #設定設窗大小
widget.setWindowTitle("hello widget")       #設定視窗名稱

lab_hello=QtWidgets.QLabel(widget)          #建立標籤
lab_hello.setText("Hello World, PyQt5")     #設定標籤文字

font_size=15

font=QtGui.QFont()                          #建立字形物件
font.setPointSize(font_size)                #設定字體大小
font.setBold(True)                          #設定粗體

lab_hello.setFont(font)                     #設定標籤字體
size=lab_hello.sizeHint()                   #取得字體合適大小

lab_x=int((widget_width-size.width())/2)
lab_y=int((widget_height-size.height())/2)
lab_hello.setGeometry(lab_x,lab_y,size.width(),size.height())

widget.show()                               #顯示視窗
sys.exit(app.exec_())                       #執行程式
