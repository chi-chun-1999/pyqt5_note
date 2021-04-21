import sys
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal


class Score(QObject):

    subject_changed=pyqtSignal(str)
    score_changed=pyqtSignal([int],[str])

    def __init__(self,subject='Math',score=90,parent=None):
        super().__init__(parent)
        self.setScore(score)
        self.setSubject(subject)

    def setScore(self,score):
        self.__score=score
        self.score_changed.emit(self.__score)

        if score<60:
            score_info='請重考'
        elif (60<= score <70):
            score_info='成績普通'
        elif (70<= score <90):
            score_info='成績不錯'
        elif (90<= score):
            score_info='成績超棒'
        self.score_changed[str].emit(score_info)

    def setSubject(self,subject):
        self.__subject=subject
        self.subject_changed.emit(self.__subject)


class Responsor(QObject):

    @pyqtSlot(int)
    def do_score_changed_int(self,age):
        print("你的成績是"+str(age))

    @pyqtSlot(str)
    def do_score_changed_str(self,score_info):
        print(score_info)

    @pyqtSlot(str)
    def do_subject_changed_int(self,subject):
        print("科目"+subject)


if __name__=="__main__":

    jack_score=Score("Math",85)
    resp=Responsor()

    jack_score.subject_changed.connect(resp.do_subject_changed_int)

    jack_score.score_changed.connect(resp.do_score_changed_int)
    jack_score.score_changed[str].connect(resp.do_score_changed_str)

    jack_score.setScore(50)
    jack_score.setSubject("Chinese")

    print("\n\n")
    jack_score.score_changed[str].disconnect(resp.do_score_changed_str)
    jack_score.setScore(79)
