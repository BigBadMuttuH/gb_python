num = 2 ** 16 - 1
b = bin(num)
o = oct(num)
h = hex(num)
print(b, o, h)

print(0.1 + 0.2)
pi = 3.141592653_589_793_24223233232
print(pi)

DEFAULT = 42
num = int(input('Enter a number: '))
level = num or DEFAULT
print(level)

name = input('Enter your name: ')
if name:
    print(f'Hello, {name}!')
else:
    print('Hello')

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while data:
    print(data.pop())
