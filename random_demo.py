import random

for i in range(10):
    print(random.random())

for i in range(10):
    print(random.uniform(3, 7))

for i in range(10):
    print(random.normalvariate(0, 1))

for i in range(10):
    print(random.randint(1, 6))

for i in range(10):
    print(random.choice(["rock", "paper", "scisors"]))
