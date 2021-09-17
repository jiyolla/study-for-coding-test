import sys


@profile
def solve():
    read = sys.stdin.readline
    n = int(read())
    table = [[] for _ in range(n)]
    table[0].append(int(read()))
    for i in range(1, n):
        line = list(map(int, read().split()))
        table[i].append(table[i - 1][0] + line[0])
        for j in range(1, i):
            table[i].append(max(table[i - 1][j - 1], table[i - 1][j]) + line[j])
        table[i].append(table[i - 1][-1] + line[-1])
    print(max(table[-1]))


solve()
