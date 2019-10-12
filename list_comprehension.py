squares = [i**2 for i in range(1, 101) if i%2 == 0]
print(squares)

A = [1, 3, 5, 7]
B = [2, 4, 6, 8]
cartesian_product = [(a, b) for a in A for b in B]
print(cartesian_product)
