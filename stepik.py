from random import *


answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]
def welcome():
    print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
    print('Как тебя зовут?')
    input_name = input()
    print(f'Привет, {input_name}')

def input_question():
    print('Введи свой вопрос!')
    question = input()
    if question in ['Давай закончим', 'Хватит', 'Пока', 'Нет', 'Давай спать']:
        return False, print('Возвращайся если возникнут вопросы!')
    print(choice(answers))
    return question

def game():
    welcome()
    input_question()
    while True:
        print('Хочешь ещё задать вопрос?')
        one_more_game = input().lower()
        if one_more_game in ['да', 'д', 'l', 'lf']:
            input_question()
        else:
            return print('Возвращайся если возникнут вопросы!')

game()
