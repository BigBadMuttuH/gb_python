import decimal
from decimal import Decimal
from math import pi


def ex1():
    data = [1, "hello", 2.5, 1.0]
    for i in data:
        print(i, id(i), i.__sizeof__(), hash(i), isinstance(i, (int, float, complex)), isinstance(i, str), sep=", ")


def translate(num: int, n: int) -> int:
    result = []
    while num:
        result.append(num % n)
        num //= n
    return sum(result[i] * 10 ** i for i in range(len(result)))
    # result = [str(i) for i in result[::-1]]
    # return "".join(result)


def ex2():
    default_number = "237"
    def_bin, def_oct = 2, 8
    number: int = int(input("Enter a number: ") or default_number)
    print(bin(number), oct(number))
    print(translate(number, def_bin), translate(number, def_oct))


def ex3():
    """
    Подсчитать площадь круга, через decimal
    """
    decimal.getcontext().prec = 42
    diameter = Decimal(input("Enter a diameter: "))
    PI = Decimal(pi)
    radius = diameter / 2
    print("The area of the circle is", diameter * PI)
    print("The surface of the circle is", PI * radius ** 2)


# def ex4():
#     """
#     Решаем квадратное уравнение, даже если дискриминант отрицательный
#     discriminant = b ** 2 - 4 * a * c
#     """
#     a, b, c = int(input("Enter a: ")), int(input("Enter b: ")), int(input("Enter c:"))
#     discriminant = b ** 2 - 4 * a * c


def main():
    # ex1()
    # ex2()
    ex3()


if __name__ == "__main__":
    main()
