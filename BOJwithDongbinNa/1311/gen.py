import random

random.seed(0)
n = int(input())
print(n)
for i in range(n):
    print(*[random.randint(1, 10000) for j in range(n)])
