from PyQt6.QtWidgets import *

app = QApplication([])
window = QWidget()

main_line = QVBoxLayout()
line0 = QHBoxLayout()
line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()

ques = QLabel('Хто такий MC Петя')
ques1 = QLabel('Скільки йому років?')

ans1 = QRadioButton('Мотиватор')
ans2 = QRadioButton('Президент')
ans3 = QRadioButton('Ijcm cgsdf')
ans4 = QRadioButton('Я незнаю')

ans5 = QRadioButton('20')
ans6 = QRadioButton('25')
ans7 = QRadioButton('34')
ans8 = QRadioButton('26')

main_line.addWidget(ques)
line0.addWidget(ans1)
line0.addWidget(ans2)
line1.addWidget(ans3)
line1.addWidget(ans4)
line2.addWidget(ans5)
line2.addWidget(ans6)
line3.addWidget(ans7)
line3.addWidget(ans8)

main_line.addLayout(line0)
main_line.addLayout(line1)
main_line.addWidget(ques1)
main_line.addLayout(line3)
main_line.addLayout(line2)

def win_func():
    msg = QMessageBox()
    msg.setText('Ви перемогли у вікторині')
    msg.setWindowTitle('Перемога!')
    msg.exec()
def lose_func():
    msg = QMessageBox()
    msg.setText('Ви програли у вікторині')
    msg.setWindowTitle('Поразка')
    msg.exec()

ans1.clicked.connect(win_func)
ans2.clicked.connect(lose_func)
ans3.clicked.connect(lose_func)
ans4.clicked.connect(lose_func)
ans5.clicked.connect(lose_func)
ans6.clicked.connect(win_func)
ans7.clicked.connect(lose_func)
ans8.clicked.connect(lose_func)

window.setLayout(main_line)
window.show()
app.exec()

