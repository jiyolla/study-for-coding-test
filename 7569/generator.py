import random
m = 50
n = 50
h = 50
random.seed(3)
print(f'{m} {n} {h}')
for i in range(h):
    for j in range(n):
        for k in range(m):
            print(random.choice([0, 1]), end=' ')
        print()