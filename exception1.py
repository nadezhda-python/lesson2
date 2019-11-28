"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():

    question_answers = {
        'Как дела': 'Хорошо!', 
        'Что делаешь?' : 'Программирую',
        'Хочешь есть?' : 'Да'
    }

    while True:
        try:
            question = input('Задай вопрос на который я могу ответить: \n')
            if question in question_answers:
                print(question_answers[question])
                break
            else:
                print ('Давай что-то полегче!')
        except KeyboardInterrupt:
            print('Пока-пока')
            break

if __name__ == "__main__":
    ask_user()
