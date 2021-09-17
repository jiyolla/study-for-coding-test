import bisect


def solve():
    input()
    table = list(map(int, input().split()))
    table.sort()
    input()
    print('\n'.join(['1' if bisect.bisect_right(table, int(i)) - bisect.bisect_left(table, int(i)) > 0 else '0' for i in input().split()]))


solve()
