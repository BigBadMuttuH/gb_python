name = 'Alex'
age = 20
# старое форматирование
text1 = 'My name is %s and I am %d years old!' % (name, age)
print(text1)

# новые форматы
text2 = 'My name is {0}, I am {1} years old!'.format(name, age)
print(text2)

text3 = f'My name is {name}, I am {age} years old!'
print(text3)

print(f'{{Фигурные скобки}} and {{name}}, and {{{name}}}')

pi = 3.141592653589793
print(f'{pi:.2f}')

data = [2323, 2342424, 23424244, 24242424]
for item in data:
    print(f'{item:>10}')
for item in data:
    print(f'{item:<10}')
for item in data:
    print(f'{item:^10}')

num = 2 * pi * data[1]
print(f'{num=:_}')  # num=14_717_884.059984835
