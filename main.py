from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QMessageBox, QHBoxLayout, QGroupBox
from random import shuffle

class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


lict = list()






def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        main_win.score += 1
    else:
        show_correct('Неправильно')


def show_questions():
    RadioGroupbox.show()
    RadioGroupbox2.hide()
    button.setText('Ответить')
def show_result():
    RadioGroupbox.hide()
    RadioGroupbox2.show()
    button.setText('Следующий вопрос')
def start_test():
    if button.text() == 'Ответить':
        check_answer()
        show_result()

    else:
        next_question()
        show_questions()



app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('*Текст в подвале*')

text = QLabel('ДеревнЯ')
text2 = QLabel('Прав ли ты:')
text3 = QLabel('Ответ скоро будет!')

RadioGroupbox = QGroupBox('Варианты ответа')
RadioGroupbox2 = QGroupBox('Результаты текста')
button1 = QRadioButton('Энцы')
button2 = QRadioButton('Мама я в ютубе №2')
button3 = QRadioButton('Шайлушаи')
button4 = QRadioButton('Алеуты')
button = QPushButton('Ответить')
RadioGroupbox2.hide()
button.clicked.connect(start_test)
answers = [button1, button2, button3, button4]
shuffle(answers)
main_win.score = 0
main_win.total = 0
main_win.count = 0



def ask(q: Question):
    text.setText(q.question)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)

main_win.counter = -1
def next_question():
    main_win.total += 1
    main_win.counter += 1
    main_win.count += 1

    if main_win.counter == len(lict):
        main_win.counter = -1

    q=lict[main_win.counter]
    ask(q)

def show_correct(res):
    text3.setText(answers[0].text())
    text2.setText(res)


layout_quest = QHBoxLayout()
layout_quest.addWidget(button1)
layout_quest.addWidget(button2)
layout_quest.addWidget(button3)
layout_quest.addWidget(button4)

line = QVBoxLayout()
line1 = QVBoxLayout()
line2 = QVBoxLayout()
line3 = QHBoxLayout()
line4 = QVBoxLayout()
line5 = QHBoxLayout()

line.addWidget(text, alignment = Qt.AlignHCenter)
line1.addWidget(text2, alignment = (Qt.AlignLeft | Qt.AlignTop))
line1.addWidget(text3, alignment = (Qt.AlignVCenter | Qt.AlignHCenter))

line2.addWidget(button1, alignment = Qt.AlignCenter)

line2.addWidget(button2, alignment = Qt.AlignCenter)
line4.addWidget(button3, alignment = Qt.AlignCenter)
line4.addWidget(button4, alignment = Qt.AlignCenter)
line5.addLayout(line2)
RadioGroupbox.setLayout(line5)
RadioGroupbox2.setLayout(line1)
line.addWidget(RadioGroupbox)
line.addWidget(RadioGroupbox2)
line5.addLayout(line4)

line.addWidget(button, alignment = Qt.AlignCenter)



q1 = Question('2023', '2023', '2024', '2022', '1953')
q2 = Question('Что было в 1953', '1953', 'Динозавры', '3032', '6712')
q3 = Question('Почему 1953', 'Да', 'эээ а как рулить', 'хз', 'нет')
lict.append(q1)
lict.append(q2)
lict.append(q3)




main_win.setLayout(line)
main_win.show()

app.exec_()
print('Счет: ', main_win.score)
print('Кол-во вопросов:', main_win.count + 1)
print('Рейтинг:', main_win.counter / main_win.score * 100)