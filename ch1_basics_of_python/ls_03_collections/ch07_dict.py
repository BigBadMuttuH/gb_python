a = {'one': 42, 'two': 2.45, 'three': 3.45, 'four': 'hello world'}
b = dict(one=42, two=2.45, three=3.45, four='hello world')
c = dict([('one', 42), ('two', 2.45), ('three', 3.45), ('four', 'hello world')])
print(a == b == c)


x = 10
a['ten'] = x
print(a, a['one'])
print(a.get('two'))
print(a.get('five', 5))  # 5 - значение по умолчанию, не добавиться в словарь
print(a.get('ten', 5))
print(a)
print(a.setdefault('five', 5))  # 5, добавиться в словарь
print(a.setdefault('ten', 5))  # 5, не добавиться в словарь
print(a)

for key in a:
    print(key)
for value in a.values():
    print(value)
for key, value in a.items():
    print(f'{key}, {value}')

s = a | b | c | {'six': 6, 'eight': 8}
print(s)
my_dict = {'one': 1,
           'two': 2,
           'three': 3,  # хорошая практика ставить запятую после каждого значения
           }
