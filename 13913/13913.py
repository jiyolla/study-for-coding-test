import math
from collections import deque


def solve():
    n, k = map(int, input().split())

    q = deque()
    q.append((n, 0))
    mem = {n: (0, 0)}
    found = False
    ans = 0
    while q and not found:
        for _ in range(len(q)):
            cur, step = q.popleft()
            if cur == k:
                found = True
                ans = step
            if cur - 1 >= 0 and not cur - 1 in mem:
                mem[cur - 1] = (step + 1, 1)
                q.append((cur - 1, step + 1))
            if cur + 1 <= k and not cur + 1 in mem:
                mem[cur + 1] = (step + 1, 2)
                q.append((cur + 1, step + 1))
            if cur * 2 <= k + 1 and not cur * 2 in mem:
                mem[cur * 2] = (step + 1, 3)
                q.append((cur * 2, step + 1))

    print(ans)
    cur = k
    route = []
    for i in range(ans + 1):
        route.append(str(cur))
        if mem[cur][1] == 1:
            cur += 1
        elif mem[cur][1] == 2:
            cur -= 1
        elif mem[cur][1] == 3:
            cur //= 2
    print(' '.join(route[::-1]))


solve()
