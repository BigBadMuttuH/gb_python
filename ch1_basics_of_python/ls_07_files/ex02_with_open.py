with open('ex01.txt', 'r', encoding='utf-8') as file:
    print(list(file))

with (
    open('ex01.txt', 'r', encoding='utf-8') as f1,
    open('ex02.txt', 'r', encoding='utf-8', errors='backslashreplace') as f2
):
    print(list(f1))
    print(list(f2))

with open('ex01.txt', 'r', encoding='utf-8') as f:
    res = f.read()
    print(f'читаем первый раз\n{res}')
    res = f.read()
    print(f'читаем второй раз\n{res}')
