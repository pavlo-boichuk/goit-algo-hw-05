from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:
    '''
    Функція, яка генерує та повертає іншу функцію для обчислення n-те число Фібоначчі
    :return: Callable[[int], int] - повертає іншу функцію для обчислення n-те число Фібоначчі
    '''

    cache_dict = {} # Створення порожнього словника для кешування

    def fibonacci(n: int) -> int:
        '''
        Функція обчислює n-те число Фібоначчі. Якщо число вже знаходиться у кеші, функція має повертати значення з кешу
        :param n: int — n-ий член ряду Фібоначчі
        :return: int - повертає n-те число Фібоначчі
        '''
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache_dict:
            # Якщо число вже знаходиться у кеші, функція має повертати значення з кешу
            return cache_dict[n]
        else:
            # Якщо число не знаходиться у кеші, функція має обчислити його, зберегти у кеш та повернути результат
            cache_dict[n] = fibonacci(n - 1) + fibonacci(n - 2) # Використання рекурсії для обчислення чисел
            return cache_dict[n]

    return fibonacci

# Створення замикання
my_fibonacci = caching_fibonacci()
print(my_fibonacci(10))
print(my_fibonacci(15))
