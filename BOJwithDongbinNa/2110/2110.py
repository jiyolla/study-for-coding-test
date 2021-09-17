import sys
import bisect

read = sys.stdin.readline
n, c = map(int, read().split())
lst = []
for _ in range(n):
    lst.append(int(read()))
lst.sort()

upper = (lst[-1] - lst[0]) // (c - 1)
lower = 1
while upper > lower:
    # test if ans can be tangible
    possible = True
    ans = (upper + lower) // 2 + 1
    last = lst[0]
    for i in range(c - 1):
        c_index = bisect.bisect_left(lst, last + ans)
        if c_index >= len(lst):
            possible = False
            break
        else:
            last = lst[c_index]
    if possible:
        lower = ans
    else:
        upper = ans - 1
print(upper)
