SIZE = 100

with open('ex01.txt', 'r', encoding='utf-8') as f:
    while res := f.read(SIZE):
        print(res)


with open('ex01.txt', 'r', encoding='utf-8') as f:
    while res := f.readline():
        print(res)


with open('ex01.txt', 'r', encoding='utf-8') as f:
    while res := f.readline(SIZE):
        print(res)


with open('ex01.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')
