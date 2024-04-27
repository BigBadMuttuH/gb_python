# Множества
my_set = {1, 2, 3, 4, 2, 5, 6, 7}
my_f_set = frozenset((1, 2, 3, 4, 5, 6, 6, 2))
my_set.add((10, 9))
# my_f_set.add((10, 9)) так не выйдет
print(my_set, my_f_set, sep='\n')

my_other_set = my_set & my_f_set  # пересечение
print(my_other_set)
my_other_set = my_set | my_f_set  # Объединение
print(my_other_set)
my_other_set = my_set - my_f_set  # Разность
print(my_other_set)
