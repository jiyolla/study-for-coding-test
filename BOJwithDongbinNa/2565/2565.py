def solve():
    n = int(input())
    seq = [list(map(int, input().split())) for _ in range(n)]
    seq.sort()
    table = [0] * (n + 1)
    ans = 0
    for _, i in seq:
        if i > table[ans]:
            ans += 1
            table[ans] = i
        else:
            for j in range(1, ans + 1):
                if table[j] >= i:
                    table[j] = i
                    break
    print(n - ans)


solve()
