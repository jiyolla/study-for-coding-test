import random
n = 100000

x = list(range(n))
y = list(range(n))
random.seed(a=1)
random.shuffle(x)
random.shuffle(y)
print(n)
for i in range(n):
    print(f'{x[i]} {y[i]}')
