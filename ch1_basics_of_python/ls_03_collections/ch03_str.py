text = "Hello World!"
print(text[6])
print(text[3:7])

new_txt = text.replace("l", "L")
print(text, new_txt, sep='\n')

print(text.count('l'))
print(text.index('l'))
print(text.find('l'))
print(text.find('z'))  # -1 нет такой буквы
