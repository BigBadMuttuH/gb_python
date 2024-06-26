# num = int(input("Введите число для анализа: "))
def analyze_number(num):
    """
    Напишите код, который анализирует число num и сообщает, является ли оно простым или составным.
    Используйте правило для проверки: “Число является простым, если это число натуральное и
    делится нацело только на единицу и на себя”.
    Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
    Если подается отрицательное число или число более ста тысяч,
    выведите на экран сообщение: "Число должно быть больше 1 и меньше 100000".
    Внимание! Число 1 — не является ни простым, ни составным числом, так как у него только один делитель — 1.
    """
    if num <= 1 or num > 100000:
        return "Число должно быть больше 1 и меньше 100000"

    if num == 1:
        return "Число 1 не является ни простым, ни составным"

    # Проверка простоты числа
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return "Не является простым"

    return "простое"


num = 12
result = analyze_number(num)
print(result)
