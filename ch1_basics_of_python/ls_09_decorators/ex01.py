def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Что-то происходит перед вызовом функции.")
        result = func(*args, **kwargs)
        print("Что-то происходит после вызова функции.")
        return result

    return wrapper


@my_decorator
def add(x, y):
    return x + y


@my_decorator
def say_hello():
    print("Hello!")


@my_decorator
def main(x, y):
    say_hello()
    result = add(x, y)
    print(result)


main(10, 20)
