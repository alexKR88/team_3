"""Программа находит простые числа в диапазоне, пользователь вводит
начало и конец диапазона в котором следует искать, вывод
оформляется в виде списка"""

"""Функция определяет простое число или нет, возвращает
True если оно простое и False если это не так"""
while True:
    try:
        a = int(input("Введите начало диапазона: "))
        b = int(input("Введите конец диапазона: "))
        #Создаем список для хранения простых чисел
        prime_numbers = []
        # Проверка каждого числа в диапазоне
        for num in range(a, b + 1):
            if num > 1:  # Простые числа больше 1
                is_prime = True
                # Проверяем делители до корня числа
                for i in range(2, int(
                        num ** 0.5) + 1):
                    if num % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    prime_numbers.append(num)
        # Вывод результата
        print("Простые числа в диапазоне:", prime_numbers)
    except:
        print("Некоректные данные!")

