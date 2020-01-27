import functools

numbers = list(range(1, 11))
print(numbers)

product = functools.reduce(lambda x, y: x*y, numbers)
print(product)
