class Person:
    max_up = 3


p1 = Person()
p1.name = 'Anton'
print(p1.name)
print(p1.max_up)
p2 = Person()
p2.max_up = 10
print(p2.max_up, p1.max_up)
Person.max_up = 20
print(p2.max_up, p1.max_up)  # значение остается то, что прямо получил класс.
