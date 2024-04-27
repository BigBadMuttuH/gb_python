from fractions import Fraction

# Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.
HEX_BASE = 16
HEX_DIGITS = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
    5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
}


def int_to_hex(num):
    # Проверка на специальный случай
    if num == 0:
        return '0'

    hex_string = ''
    while num > 0:
        hex_digit = num % HEX_BASE
        hex_string = HEX_DIGITS[hex_digit] + hex_string
        num //= HEX_BASE
    return hex_string


# Получение числа от пользователя и его преобразование
# num = int(input("Введите целое число: "))
# hex_result = int_to_hex(num)
# print(f"Шестнадцатеричное представление числа {num}: {hex_result}")
#
# # Проверка результата с помощью встроенной функции hex
# print(f"Проверка с помощью функции hex: {hex(num)}")


def calculate_fractions(frac1, frac2):
    # На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
    # Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.
    # Для проверки своего кода используйте модуль fractions.
    #
    # Пример
    # На входе:
    # frac1 = "1/2"
    # frac2 = "1/3"
    #
    # На выходе:
    # Сумма дробей: 5/6
    # Произведение дробей: 1/6
    # Сумма дробей: 5/6
    # Произведение дробей: 1/6

    # Преобразование строковых представлений дробей в объекты Fraction
    f1 = Fraction(frac1)
    f2 = Fraction(frac2)

    # Вычисление суммы и произведения дробей
    sum_fractions = f1 + f2
    product_fractions = f1 * f2

    # Вывод результатов
    print(f"Сумма дробей: {sum_fractions}")
    print(f"Произведение дробей: {product_fractions}")

    return sum_fractions, product_fractions


# # Пример использования функции
# frac1 = "1/2"
# frac2 = "1/3"
#
# sum_result, product_result = calculate_fractions(frac1, frac2)


def add_fractions(frac1, frac2):
    numerator1, denominator1 = map(int, frac1.split('/'))
    numerator2, denominator2 = map(int, frac2.split('/'))

    # Находим общий знаменатель и вычисляем сумму числителей
    new_numerator = numerator1 * denominator2 + numerator2 * denominator1
    common_denominator = denominator1 * denominator2

    return f"{new_numerator}/{common_denominator}"


def multiply_fractions(frac1, frac2):
    numerator1, denominator1 = map(int, frac1.split('/'))
    numerator2, denominator2 = map(int, frac2.split('/'))

    # Вычисляем произведение числителей и знаменателей
    new_numerator = numerator1 * numerator2
    new_denominator = denominator1 * denominator2

    return f"{new_numerator}/{new_denominator}"


# Входные данные
frac1 = "1/2"
frac2 = "1/3"

# Результаты
sum_of_fractions = add_fractions(frac1, frac2)
product_of_fractions = multiply_fractions(frac1, frac2)

print(f"Сумма дробей: {sum_of_fractions}")
print(f"Произведение дробей: {product_of_fractions}")
