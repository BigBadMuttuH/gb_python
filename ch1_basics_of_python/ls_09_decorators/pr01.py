import json


def save_to_file(diction: dict, filename='result.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump({f'{k}': v for k, v in diction.items()}, f, ensure_ascii=False, indent=2)


def decorator(func):
    result = {}

    def wrapper(a, b, *args, **kwargs):
        if (a, b) not in result:
            result[(a, b)] = func(a, b)
        save_to_file(result, filename=func.__name__ + '.json')
        return result

    return wrapper


@decorator
def pr01(a: int, b: int):
    return a + b


if __name__ == '__main__':
    while True:
        a = int(input('Enter a number: '))
        b = int(input('Enter b number: '))
        print(pr01(a, b))
