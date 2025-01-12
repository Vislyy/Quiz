from PyQt6.QtWidgets import *

app = QApplication([])
window = QWidget()

vmainline0 = QVBoxLayout()
hline0 = QHBoxLayout()
hline1 = QHBoxLayout()
ques = QLabel('Хто такий MC Петя')
ans1 = QRadioButton('Мотиватор')
ans2 = QRadioButton('Президент')
ans3 = QRadioButton('Ijcm cgsdf')
ans4 = QRadioButton('Я незнаю')

vmainline0.addWidget(ques)
hline0.addWidget(ans1)
hline0.addWidget(ans2)
hline1.addWidget(ans3)
hline1.addWidget(ans4)

vmainline0.addLayout(hline0)
vmainline0.addLayout(hline1)

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

window.setLayout(vmainline0)
window.show()
app.exec()

