# Константы
ADULT = 18


def hello_world(s):
    print(s)
    print(id(s))


hello_world('Hello world')
hello_world(str(34 - ADULT))
print(ADULT, str(34 - ADULT), 'text', sep=' (=^.^=) ', end="#\n")
# 34 - магическое число, не делайте так

res = int(input('Enter a number: '))
print(res, type(res))
