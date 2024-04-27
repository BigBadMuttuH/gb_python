help(iter)
help(next)

# a = 42
# iter(a)

data = [2, 3, 6, 8]
list_iter = iter(data)
print(list_iter)
print(next(list_iter))
print(*list_iter)  # перебор только один раз
