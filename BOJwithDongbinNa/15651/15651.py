from itertools import product


def solve():
    n, m = map(int, input().split())
    ans = product(range(1, n + 1), repeat=m)
    print('\n'.join([' '.join([f'{i}' for i in p]) for p in ans]))


solve()
