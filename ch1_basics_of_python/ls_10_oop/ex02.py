class Person:
    max_up = 3

    def __init__(self):
        self.level = 1
        self.health = 100
        print(f'{id(self)}: level={self.level}, health={self}')


p1 = Person()
p2 = Person()

print(f'{p1.max_up=}, {p1.level=}, {p1.health=}')
print(f'{p2.max_up=}, {p2.level=}, {p2.health=}')
print(f'{id(p1)=}, {id(p2)=}')
print(f'{p1.__dict__}')
