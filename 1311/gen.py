import random

random.seed(0)
n = 17
print(n)
for i in range(n):
    print(*[random.randint(1, 10000) for j in range(n)])
