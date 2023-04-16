from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QRadioButton,\
    QPushButton, QGroupBox, QLabel, QButtonGroup
from random import shuffle
from random import randint
class Question():
    def __init__(self, question, right_ans, wrong1, wrong2, wrong3):
        self.question = question
        self.right_ans = right_ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    ans_btn.setText('Следующий вопрос')
def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    ans_btn.setText('Ответить')
    AnsGroupBtn.setExclusive(False)
    a_btn1.setChecked(False)
    a_btn2.setChecked(False)
    a_btn3.setChecked(False)
    a_btn4.setChecked(False)
    AnsGroupBtn.setExclusive(True)
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_ans)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    q_txt.setText(q.question)
    ans_txt.setText(q.right_ans)
    show_question()
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        my_win.score += 1
    else:
        show_correct('Неправильно')
def next_question():
    my_win.total += 1
    cur_question = randint(0, len(questions)-1) 
    ask(questions[cur_question])
def show_correct(txt):
    res_txt.setText(txt)
    show_result()
def clk_OK():
    if ans_btn.text() == 'Ответить':
        check_answer()
    else:
       next_question()
    print('Количество заданных вопросов:', my_win.total)
    print('Количество правильных ответов:', my_win.score)
    print('Процент правильных ответов:', round((my_win.score / my_win.total)*100,2), "%")
questions = []
questions.append(Question('Что покушал бобёр на завтрак?', 'Негммммммра Диму', 'Белого Диму', 'Америку', 'Виджета'))
questions.append(Question('Почему накакал Дима?', 'Нимммммкита', 'Нет', 'Фариз', 'Так надо'))
questions.append(Question('Что будет если не написать self в класс?', 'БАмммммН', 'Ничего', 'К тебе придёт учитель и насрет под дверь', 'Раздавит танк'))
questions.append(Question('ты аМОГУС??????????????', 'ОУНОУ', 'уц0ша0-уцйауцйа0уцйш0щ', 'да', 'пон'))
questions.append(Question('Никита?', 'никИта', 'НикиТа', 'аНикита', 'Ггиникита'))
questions.append(Question('Как зовут утителя?', 'Тюнин Павел', 'Тюнинг Павел', 'Абрамов Артем', 'Артем'))
questions.append(Question('Косинус ABC если AB это гиперболла', 'незнаю', 'знаю', 'пон3', 'нипокакая к хую гиперболлан4'))
questions.append(Question('Увеличтье окно для просмотра контента?', '1', '2', '39', '4'))
questions.append(Question('Как расшифровывается СОР?', 'Суммативное оценивание раздела', 'Сумарное обучение за раздел', 'Контрольная работа раздела', 'Составная часть обучения за четверть'))
questions.append(Question('Если фариз пукнул в прошлом классе когда дима егором артем ушел но при этом да и арканоид', 'ПайГей', 'ПАМАГИТЕ', 'Егор', 'Пихтон'))
questions.append(Question('Пайтон в фаризе', 'Питхон', 'Пайтон', 'Питон', 'Пуйтохин'))
questions.append(Question('Что пакакал но создал егор создатель?', 'Пай гей', 'Черный пайтон', 'Не араб майна', 'Ансар'))
questions.append(Question('НЕЗНАЮ??????', 'НТЬЫЧТО ОФИГЕЛДиму', 'Бцйуауцйауцйайуцауц Диму', 'амацйуауц', 'Виджета'))
app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle('мзоуцщшауцйоаауцйаауцйоаацйауцауцйауцйазуцйоайуцаоуцйазщоуцйзщшоауц')
my_win.resize(400, 250)
my_win.show()
q_txt = QLabel('Вопрос')
RadioGroupBox = QGroupBox('Ответы:')
AnsGroupBtn = QButtonGroup()
a_btn1 = QRadioButton('Ответ 1')
a_btn2 = QRadioButton('Ответ 2')
a_btn3 = QRadioButton('Ответ 3')
a_btn4 = QRadioButton('Ответ 4')
answers = [a_btn1, a_btn2, a_btn3, a_btn4]
AnsGroupBtn.addButton(a_btn1)
AnsGroupBtn.addButton(a_btn2)
AnsGroupBtn.addButton(a_btn3)
AnsGroupBtn.addButton(a_btn4)
vr_line1 = QVBoxLayout()
vr_line2 = QVBoxLayout()
hr_line = QHBoxLayout()
vr_line1.addWidget(a_btn1, alignment=Qt.AlignCenter)
vr_line1.addWidget(a_btn3, alignment=Qt.AlignCenter)
vr_line2.addWidget(a_btn2, alignment=Qt.AlignCenter)
vr_line2.addWidget(a_btn4, alignment=Qt.AlignCenter)
hr_line.addLayout(vr_line1)
hr_line.addLayout(vr_line2)
RadioGroupBox.setLayout(hr_line)
AnsGroupBox = QGroupBox('Результат теста')
res_txt = QLabel('Правильный/Неправильный')
ans_txt = QLabel('Сам ответ')
va_line = QVBoxLayout()
va_line.addWidget(res_txt, alignment=Qt.AlignLeft)
va_line.addWidget(ans_txt, alignment=Qt.AlignCenter)
AnsGroupBox.setLayout(va_line)
AnsGroupBox.hide()
ans_btn = QPushButton('Ответить')
v_line = QVBoxLayout()
v_line.addWidget(q_txt, alignment=Qt.AlignCenter)
v_line.addWidget(RadioGroupBox, alignment=Qt.AlignCenter)
v_line.addWidget(AnsGroupBox, alignment=Qt.AlignCenter)
v_line.addWidget(ans_btn, alignment=Qt.AlignCenter)
my_win.setLayout(v_line)
ans_btn.clicked.connect(clk_OK)
my_win.total = 0
my_win.score = 0
next_question()
app.exec_()