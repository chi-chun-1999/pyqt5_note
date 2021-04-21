import sys
from PyQt5.QtWidgets import QDialog,QApplication
from new_dialog import QnewDialog


if __name__=="__main__":
    app=QApplication(sys.argv)

    new_dialog=QnewDialog()
    new_dialog.show()

    if new_dialog.exec_()==QDialog.Accepted:
        print("Choose sure")
        new_dialog.GetOutCome()
    else:
        print("Choose exit")
