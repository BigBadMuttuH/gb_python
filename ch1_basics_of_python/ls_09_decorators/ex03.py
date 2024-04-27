def logger(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"[{level}] - Вызывается функция {func.__name__}")
            result = func(*args, **kwargs)
            print(f"[{level}] - Функция {func.__name__} завершила работу")
            return result

        return wrapper

    return decorator


@logger(level="INFO")
def add(x, y):
    return x + y


@logger(level="DEBUG")
def multiply(x, y):
    return x * y


print(add(2, 3))
print(multiply(2, 3))
