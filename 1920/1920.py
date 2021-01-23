from collections import Counter


def solve():
    input()
    table = Counter(input().split())
    input()
    print(' '.join(['1' if table[i] else '0' for i in input().split()]))


solve()
