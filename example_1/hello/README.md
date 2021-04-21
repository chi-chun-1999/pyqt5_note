# example_1 --- hello.py

1. 匯入PyQt5相關套件，QtCore, QtGui, QtWidget

2. ```python3
    QtWidgets.QApplication(sys.argv)
    ```
    ` QWidgets`的 `QApplication`模組是管理GUI應用程式的控制與主要流程的類別

3. ```python3
    widget=QtWidgets.QWidget()                  
    widget.resize(widget_width,widget_height)   
    widget.setWindowTitle("hello widget")       
    ```
    使用`QWidgets`的 `QWidget`類別。`resize()`函數用來設定設窗的大小，`setWindowTitle()`函數用來設定表單名稱

4. ```python3
    lab_hello=QtWidgets.QLabel(widget)
    lab_hello.setText("Hello World, PyQt5")
    ```
    使用`QWidgets` 的 `QLabel`類別。並將`widget`作為參數傳遞的建置函數，實際上是將widget作為lab_hello的父容器，這樣標籤才會顯示在widget上
5. ```python
    widget.show()                               
    sys.exit(app.exec_())                      
    ```
    顯示並執行
