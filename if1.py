"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи  и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def main():
    
    age = input('Введите ваш возраст: ')
    
    try:
        age = int(float(age))
    except TypeError:
        print('Нужно ввести числовое значение')

    if age >= 100 or age < 0:
        return('Правда?')

    if age <= 6:
        return f'Вам всего {age}! Думаю вы ходите в детский сад?'
    elif age <= 18:
        return f'Вам всего {age}! Вы учитесь у школе?'
    elif age <= 23:
        return f'Вам всего {age}! Вы студент?'
    elif age <= 60:
        return f'Вам уже {age}! Вы работаете?'
    else:
        return f'Вам уже {age}! Вам пора на пенсию.'

if __name__ == "__main__":
    print (main())