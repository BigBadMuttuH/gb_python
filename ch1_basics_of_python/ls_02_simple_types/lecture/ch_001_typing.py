# type(object)  # возвращает класс объекта, его тип.
# id(object)    # адрес объекта в оперативной памяти
# isinstance(object, classinfo) # принимает на вход объект и класс и
# возвращает истину или лож
# is сравнивает пару объектов на идентичность
a = 5
print(type(a), id(a))
print(isinstance(a, int))
a = "Hello world"
print(type(a), id(a))
print(isinstance(a, int))
a = 42 * 3.14 / 2.71
print(type(a), id(a))
print(isinstance(a, (int, str, complex)))
a = True
print(type(a), id(a))
print(isinstance(a, (int, float, complex)))
