from functools import reduce
numbers = [1, 2, 3, 4]
total = reduce(lambda a, b: a + b, numbers)
print(total)