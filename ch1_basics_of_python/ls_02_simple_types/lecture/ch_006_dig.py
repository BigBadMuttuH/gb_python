import sys

# Целые числа
# int(x, base=10) - возвращает целочисленный объект
# bin(x) - двоичная число 0b
# oct(x) - целое восьмеричное число 0o
# hex(x) - шестнадцатеричное число 0x
x = int("42")
y = int(3.141592653589793)
z = int("hello", base=30)
print(x, y, z, sep='\n')

# резиновый int
STEP = 2 ** 16
num = 1
for _ in range(30):
    print(sys.getsizeof(num), num)
    num *= STEP

num = 7_347_927_348
print(num)
