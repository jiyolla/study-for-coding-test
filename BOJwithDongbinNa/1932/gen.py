import random
import sys


n = int(sys.argv[1]) if len(sys.argv) > 1 else 500
random.seed(1)
print(n)
for i in range(1, n + 1):
    print(*[random.randint(0, 9999) for _ in range(i)])
