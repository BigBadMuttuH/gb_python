import copy

my_list = [4, 2, 3, 4, 5, 8, 9, 5, 1, 0]
sorted_list = sorted(my_list)
reversed_list = sorted(my_list, key=my_list.index)
reversed_list1 = sorted(my_list, reverse=True)

print(my_list, sorted_list, reversed_list, reversed_list1, sep='\n')

# оба листа ссылаются на один и тот же объект в памяти
new_list = my_list
my_list.insert(2, 555)
print(my_list, new_list, id(my_list), id(new_list), sep='\n')

new_list1 = my_list.copy()
my_list.insert(3, 999)
print(my_list, new_list1, id(my_list), id(new_list1), sep='\n')

# полное глубинное копирование
my_list2 = copy.deepcopy(my_list)

help(list.mro)