import bisect
from itertools import combinations


def solve():
    n, c = map(int, input().split())
    w = list(map(int, input().split()))

    # len(left) <= len(right)
    left = w[:len(w)//2]
    right = w[len(w)//2:]

    left_sums = []
    right_sums = []
    for i in range(len(left) + 1):
        left_sums += list(map(sum, combinations(left, i)))
    for i in range(len(right) + 1):
        right_sums += list(map(sum, combinations(right, i)))

    left_sums.sort()
    ans = 0
    for r in right_sums:
        ans += bisect.bisect_right(left_sums, c - r)
    print(ans)


solve()
