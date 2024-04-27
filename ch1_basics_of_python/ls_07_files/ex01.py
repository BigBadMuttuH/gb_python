f = open('ex01.txt', 'w+', encoding='utf-8')
f.write('Hello world.\n')
f.write('This is the first line.\n')
f.write('This is the second line.\n')
f.close()

f = open('ex02.txt', 'wb')
f.write('\nThis is ch1251, а тут русские буквы.'.encode('cp1251'))
f.close()

f = open('ex02.txt', 'r', encoding='utf-8', errors='replace')
print(f.read())
f.close()
