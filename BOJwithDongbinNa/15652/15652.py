from itertools import combinations_with_replacement


def solve():
    n, m = map(int, input().split())
    ans = combinations_with_replacement(range(1, n + 1), m)
    print('\n'.join([' '.join([f'{i}' for i in p]) for p in ans]))


solve()
