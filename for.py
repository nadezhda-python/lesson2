"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main(school_scores):

    number_of_students = 0
    total_score = 0

    for school_class in school_scores:
        number_of_students += len(school_class["scores"])
        total_score = total_score + sum(school_class["scores"])
        print (f'В классе {school_class["school_class"]} средний бал учеников равен \
        {round(sum(school_class["scores"])/len(school_class["scores"]), 2)}.')

    print(f'По всей школе средний бал учеников равен {round(total_score/number_of_students, 2)}')

    
if __name__ == "__main__":
    school_scores = [
    {'school_class': '4a', 'scores': [3, 3]},
    {'school_class': '6a', 'scores': [1, 2, 3, 2]},
    {'school_class': '4g', 'scores': [5, 5, 5, 5, 5]}
    ]
    main(school_scores)
