# Генераторы
a = range(0, 10, 2)
print(f'{a=}, {type(a)=}, {a.__sizeof__()=}, {len(a)}')

# генераторные выражения
my_gen = (chr(i) for i in range(97, 123))
print(my_gen)
for char in my_gen:
    print(char, end='')

# Генератор списка
my_comprehensions = [chr(i) for i in range(97, 123)]
print('\n', my_comprehensions)
for char in my_comprehensions:
    print(char, end=',')
