my_list = [1, 3, 4, 10, 12, 88, 2, 5, 18]
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11]]
print(len(my_list))
# len выводит длину поверхностного списка
print(len(matrix))

print(my_list[2:5:2])
print(my_list.pop())
print(my_list.extend([314, 42]))    # None
print(my_list.sort(reverse=True))   # None
print(my_list)
