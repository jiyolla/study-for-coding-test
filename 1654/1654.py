import sys
import bisect


def solve():
    read = sys.stdin.readline
    k, n = map(int, read().split())
    lines = [int(read()) for _ in range(k)]
    lines.sort(reverse=True)

    upper = lines[0]
    lower = 1
    while upper > lower:
        ans = (upper + lower) // 2 + 1
        # print(f'u:{upper:<10} l:{lower:<10} ans:{ans:<10}')
        # check if possible
        # 2 solution for this
        count = 0
        # """
        if(k * 1000 < lines[0] // ans):
            for i in lines:
                count += i // ans
        else:
        # """
            last = 0
            for i in range(1, lines[0] // ans + 1):
                cur = bisect.bisect_left(lines[::-1], ans * i, lo=last)
                count += (cur - last) * (i - 1)
                # print(f'last:{last:<10} i:{i:<10} cur:{cur:<10} count:{count:<10}')
                last = cur
            count += (k - last) * (lines[0] // ans)
            # print(f'last:{last:<10} i:{i:<10} cur:{cur:<10} count:{count:<10}')

        # adjust upper and lower bound
        if count >= n:
            lower = ans
        else:
            upper = ans - 1
    print(upper)


solve()
