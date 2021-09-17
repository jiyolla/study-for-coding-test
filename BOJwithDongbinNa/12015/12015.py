import bisect


def solve():
    n = int(input())
    seq = list(map(int, input().split()))

    min_seq = [0] * (n + 1)
    size = 0
    for i in seq:
        if i > min_seq[size]:
            size += 1
            min_seq[size] = i
        else:
            b_left = bisect.bisect_left(min_seq, i, lo=0, hi=size)
            b_right = bisect.bisect_right(min_seq, i, lo=0, hi=size)
            if b_left == b_right:
                min_seq[b_right] = i
    print(size)


solve()
