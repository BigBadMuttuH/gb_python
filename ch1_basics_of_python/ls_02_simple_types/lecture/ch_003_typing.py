txt = 'Hello world'
# txt[5] = '_' # строка - не изменяемый тип данных,
# но можно так
print(txt, id(txt))
txt = txt.replace(' ', '_')
print(txt, id(txt))
print()

a = c = 2
b = 3
print(a, id(a), c, id(c), b, id(b))
a = b + c
print(a, id(a), c, id(c), b, id(b))

# в начале у 'a' и 'с' один и тот же адрес
# 2 140714880616920 2 140714880616920 3 140714880616952
# 5 140714880617016 2 140714880616920 3 140714880616952

# у НЕ_изменяемых можно вычислить hash
# у изменяемых объектов нельзя вычислить hash
# так можно отличить изменяемый объект, от неизменяемого

x = 42
y = 'txt'
z = 3.14
my_list = [x, y, z]
print(hash(x), hash(y), hash(z))
# print(hash(my_list)) # будет ошибка, т.к. list __изменяемый

o = input('Enter o: ')
print(o, type(o), id(o), hash(o), sep=', ')
