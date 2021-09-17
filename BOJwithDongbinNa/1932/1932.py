import sys


@profile
def solve():
    read = sys.stdin.readline
    n = int(read())
    table = [0] * (n * (n + 1) // 2)
    table[0] = int(read())
    for i in range(1, n):
        line = list(map(int, read().split()))
        table[i * (i + 1) // 2] = table[i * (i - 1) // 2] + line[0]
        for j in range(1, i):
            table[i * (i + 1) // 2 + j] = max(table[i * (i - 1) // 2 + j - 1], table[i * (i - 1) // 2 + j]) + line[j]
        table[(i + 1) * (i + 2) // 2 - 1] = table[i * (i + 1) // 2 - 1] + line[-1]
    print(max(table[-n:]))


solve()
