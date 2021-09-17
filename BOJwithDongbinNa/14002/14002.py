import sys
import bisect


def solve():
    read = sys.stdin.readline
    n = int(read())
    seq = list(map(int, read().split()))

    # mem[i][j]는 seq[:i + 1]의 부분 수열 중, 길이가 j + 1인 LIS 중 마지막 원소가 가장 작은 LIS의 마지막 원소값이다.
    mem = [[] for _ in range(n)]
    mem_idx = [[] for _ in range(n)]
    mem[0] = [seq[0]]
    mem_idx[0] = [0]
    for i in range(1, n):
        mem[i] = mem[i - 1][:]
        mem_idx[i] = mem_idx[i - 1][:]
        if seq[i] > mem[i][-1]:
            mem[i].append(seq[i])
            mem_idx[i].append(i)
        else:
            update_idx = bisect.bisect_left(mem[i], seq[i])
            mem[i][update_idx] = seq[i]
            mem_idx[i][update_idx] = i
    print(len(mem[-1]))
    ans = []
    idx = n
    for i in range(len(mem[-1]) - 1, -1, -1):
        num, idx = mem[idx - 1][i], mem_idx[idx - 1][i]
        ans.append(str(num))
    print(' '.join(ans[::-1]))


solve()
