from itertools import permutations


def solve():
    n, m = map(int, input().split())
    ans = permutations(range(1, n + 1), m)
    print('\n'.join([' '.join([f'{i}' for i in p]) for p in ans]))


solve()
