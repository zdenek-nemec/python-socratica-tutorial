numbers = list(range(1, 11))
print(numbers)

even = filter(lambda x: x%2 == 0, numbers)
print(even)
print(list(even))
