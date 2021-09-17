def solve():
    n = int(input())
    seq = list(map(int, input().split()))
    table = [0] * (n + 1)
    ans = 0
    for i in seq:
        if i > table[ans]:
            ans += 1
            table[ans] = i
        else:
            for j in range(1, ans + 1):
                print(f'i: {i} j: {j}')
                if table[j] >= i:
                    table[j] = i
                    break
    print(ans)


solve()
