"""

Домашнее задание №3

Перепишите функцию discounted(price, discount, max_discount=20) 
из урока про функции так, чтобы она перехватывала исключения, когда 
переданы некорректные аргументы (например, строки вместо чисел).
    
"""

def discounted(price, discount, max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(float(max_discount))
        if max_discount > 99:
            return 'Слишком большая максимальная скидка'
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    except ValueError:
        return 'Цена и размер скидки должны быть численными'
    
    
if __name__ == "__main__":
    print(discounted(100, 'f', 200))


