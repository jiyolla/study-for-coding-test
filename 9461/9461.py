def solve():
    t = int(input())
    n = [int(input()) for _ in range(t)]
    seq = [1, 1, 1, 2, 2] + [0] * 95
    for i in range(5, max(n)):
        seq[i] = seq[i - 1] + seq[i - 5]
    print('\n'.join([str(seq[i - 1]) for i in n]))


solve()
