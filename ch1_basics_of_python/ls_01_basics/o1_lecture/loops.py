num = float(input('Введите число: '))
count = 0
while count < num:
    print(count)
    count += 2

STEP = 2
limit = num - STEP
count = -STEP
while count < limit:
    count += STEP
    if count % 12 == 0:
        continue
    print(count)

min_limit = 0
max_limit = 10
while True:
    print('Введи число между', min_limit, 'и', max_limit, '? ')
    num = float(input())
    if num < min_limit or num > max_limit:
        print('Неверно')
    else:
        break
print('Было введено число ' + str(num))

animals = ['cat', 'dog', 'horse', 'sheep']
for i, animal in enumerate(animals, start=1):
    print(i, animal, sep=' | ')
