import sys


def solve():
    read = sys.stdin.readline
    n = int(read())
    seq = list(map(int, read().split()))
    x = int(read())
    seq.sort()
    ans = 0
    e = n - 1
    for s in range(n - 1):
        for new_e in range(e, s, -1):
            if seq[s] + seq[new_e] < x:
                break
            if seq[s] + seq[new_e] == x:
                ans += 1
                break
        e = new_e
    print(ans)


solve()
