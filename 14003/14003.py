import sys
import bisect


def solve():
    read = sys.stdin.readline
    n = int(read())
    seq = list(map(int, read().split()))

    # mem[i]는 기방문한 부분 수열 중, 길이가 i + 1인 LIS 중 마지막 원소가 가장 작은 LIS의 마지막 원소값이다.
    mem = [seq[0]]
    # mem_idx[i]는 seq[i]가 mem에 기록될 때의 mem에서의 index값이다.
    mem_idx = [0] * n
    for i in range(1, n):
        if seq[i] > mem[-1]:
            mem_idx[i] = len(mem)
            mem.append(seq[i])
        else:
            update_idx = bisect.bisect_left(mem, seq[i])
            mem[update_idx] = seq[i]
            mem_idx[i] = update_idx
    order = len(mem)
    print(order)
    ans = []
    for i in range(n - 1, -1, -1):
        if mem_idx[i] == order - 1:
            order -= 1
            ans.append(str(seq[i]))
    print(' '.join(ans[::-1]))


solve()
