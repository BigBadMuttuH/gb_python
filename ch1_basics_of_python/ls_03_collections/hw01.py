import re
from collections import Counter


# При отправке кода на Выполнение раскомментируйте строку ниже,
# чтобы задать значения аргументов и вызвать функцию
# При отправке решения на Проверку закомментируйте эту строку обратно -
# система автоматически подставит разные значения аргументов и вызовет функцию для проверки
def pack_backpack(items, max_weight):
    current_weight = 0
    backpack = {}
    for item, weight in items.items():
        if current_weight + weight <= max_weight:
            backpack[item] = weight
            current_weight += weight
    return backpack


# Пример использования функции
items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0

# Результат сохранён в переменную backpack
backpack = pack_backpack(items, max_weight)


# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
#
# Слова разделяются пробелами. Такие слова как don t, it s, didn t итд
# (после того, как убрали знак препинания апостроф) считать двумя словами.
# Цифры за слова не считаем.
# Отсортируйте по убыванию значения количества повторяющихся слов. Слова выведите в обратном алфавитном порядке.
def top_10_frequent_words(text):
    # Удаляем знаки препинания, кроме апострофов
    cleaned_text = re.sub(r'[^\w\s\']', '', text)

    # Преобразуем текст к нижнему регистру и разбиваем на слова
    words = cleaned_text.lower().split()

    # Подсчитываем количество каждого слова, исключаем цифры
    word_counts = Counter(word for word in words if not word.isdigit())

    # Сортируем слова по количеству их встречаемости и алфавиту в обратном порядке
    sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]), reverse=True)

    # Возвращаем первые 10 элементов списка
    return sorted_words[:10]


# Пример использования функции
text = 'Hello world. Hello Python. Hello again.'
print(top_10_frequent_words(text))

# Удаляем знаки препинания и приводим текст к нижнему регистру
cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in text)

# Разбиваем текст на слова и считаем их количество
words = cleaned_text.split()
word_counts = {}

for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

# Получаем 10 самых часто встречающихся слов
top_words = sorted(word_counts.items(), key=lambda x: (x[1], x[0]), reverse=True)[:10]

print(top_words)


def find_duplicates(lst):
    seen = set()
    duplicates = []
    for item in lst:
        # Если элемент уже видели и он ещё не добавлен в список дубликатов
        if item in seen and item not in duplicates:
            duplicates.append(item)
        else:
            seen.add(item)  # Добавляем элемент в множество уникальных элементов
    return duplicates


# Пример использования
lst = [1, 1, 2, 2, 3, 3]
print(find_duplicates(lst))
