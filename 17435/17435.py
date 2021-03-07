import sys
import math


def solve():
    read = sys.stdin.readline
    m = int(read())
    f = tuple([None]) + tuple(map(int, read().split()))
    q = int(read())
    queries = [tuple(map(int, read().split())) for _ in range(q)]

    # f_2tothe[i][j] = f_{2^i}(j)
    max_power = math.ceil(math.log2(500000))
    f_2tothe = [[None] * (m + 1) for _ in range(max_power)]
    for x in range(1, m + 1):
        f_2tothe[0][x] = f[x]
    for power in range(1, max_power):
        for x in range(1, m + 1):
            f_2tothe[power][x] = f_2tothe[power - 1][f_2tothe[power - 1][x]]

    def f_(n, x):
        if n == 0:
            return x
        biggest_power_under = math.floor(math.log2(n))
        next_n = n - pow(2, biggest_power_under)
        return f_(next_n, f_2tothe[biggest_power_under][x])

    print_buf = []
    for n, x in queries:
        print_buf.append(f'{f_(n, x)}')
    print('\n'.join(print_buf))


solve()
