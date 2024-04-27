text = ['Hello World! I love Python! I love Python! I love Python! I love Python! I love Python!',
        'How and why are you? What is your name? What is your, Where is your favorite color? What is',
        'Please, tell me your favorite, Where is for for for while you are your favorite color?']

with open('ex04.txt', 'a', encoding='utf-8') as f:
    for line in text:
        res = f.write(line + '\n')
        print(f'{res=}\n{len(line)=}')


with open('ex04.txt', 'a', encoding='utf-8') as f:
    for line in text:
        print(line, file=f)


with open('ex04.txt', 'a', encoding='utf-8') as f:
    for line in text:
        print(line, end='***\n##', file=f)
        # print(line, end='</h1>\n<h1>', file=f)

