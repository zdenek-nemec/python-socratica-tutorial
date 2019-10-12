import math
import time

def is_prime_v1(n):
    """Return "True" if "n" is a prime number. False otherwise."""
    if n == 1:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

def is_prime_v2(n):
    """Return "True" if "n" is a prime number. False otherwise."""
    if n == 1:
        return False
    for d in range(2, math.floor(math.sqrt(n))):
        if n % d == 0:
            return False
    return True

def is_prime_v3(n):
    """Return "True" if "n" is a prime number. False otherwise."""
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n > 2 and n % 2 == 0:
        return False
    for d in range(3, math.floor(math.sqrt(n)), 2):
        if n % d == 0:
            return False
    return True

for n in range(1, 21):
    print(n, is_prime_v1(n))

t0 = time.time()
for n in range(1, 100000):
    is_prime_v3(n)
t1 = time.time()
print("Time required:", t1 - t0)
