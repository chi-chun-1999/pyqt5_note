import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from PyQt5.QtGui import QIcon

from ui_Widget import Ui_Widget

class QmyWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_Widget()
        self.ui.setupUi(self)
        
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    form=QmyWidget()
    form.show()
    sys.exit(app.exec_())