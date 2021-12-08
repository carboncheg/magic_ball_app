print('О, приветствую тебя, мой друг! \nЯ - магический шар, и я знаю ответ на любой вопрос.')
name = input('Как тебя зовут, мой друг? \n')
if name == '':
    print('Что тебя волнует?')
else:
    print(f'Что тебя волнует, {name}?')

def launch_app():

    from random import randint
    from answers import answers

    num_answer = randint(0, 19)

    def is_valid(q):
        return q.endswith('?') and not q[:-1].isdigit() and len(q) > 3

    def choice(answer):
        return answers[num_answer]

    while True:
        question = input('Введи свой вопрос: \n').strip()
        if not is_valid(question):
            print('Нужно ввести вопрос')
            continue
        else:
            print(choice(answers))
            break

launch_app()

positive_answers = ['д', 'да', 'конечно', 'ага', 'угу']
negative_answers = ['н', 'не', 'нет', 'неа']

while True:
    again = input('Хочешь ли ты спросить еще? \n').lower()
    if again in positive_answers:
        launch_app()
    elif again in negative_answers:
        print('Возвращайся, если возникнут вопросы')
        break
    else:
        print('Твой ответ мне непонятен')
