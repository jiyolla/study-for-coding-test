def solve():
    n = int(input())
    seq = list(map(int, input().split()))
    minus_count = 0
    cur = 0
    minus = 0
    max_sum = 0
    new_chunk = True
    for i in seq:
        if i < 0:
            minus += i
            new_chunk = True
            minus_count += 1
        elif new_chunk:
            cur = max(0, cur + minus) + i
            minus = 0
            print(f'i: {i}, cur: {cur}')
            new_chunk = False
        else:
            cur += i
        max_sum = max(cur, max_sum)
    print(max(seq) if minus_count == n else max_sum)


solve()
