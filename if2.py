"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main(str1, str2):
    if not(isinstance(str1, str) and isinstance(str2, str)):
        return 0
    if str1 == str2:
        return 1
    if len(str1) > len(str2):
        return 2
    if str1 != str2 and str2 == 'learn':
        return 3
        
    
if __name__ == "__main__":
    print(main(1, 'b'))
    print(main('learn', 'learn'))
    print(main('learn1', 'b'))
    print(main('1', 'learn'))
    print(main(1, [2]))
