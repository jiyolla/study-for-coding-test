def solve():
    n, m = map(int, input().split())
    trees = list(map(int, input().split()))
    trees.sort(reverse=True)
    lower = 0
    upper = max(trees) - 1
    while upper > lower:
        ans = (upper + lower) // 2 + 1
        # print(f'u:{upper:<10}l:{lower:<10}ans:{ans:<10}')
        cut = 0
        for tree in trees:
            if tree - ans > 0 and cut <= m:
                cut += tree - ans
            else:
                break
        if cut < m:
            upper = ans - 1
        elif cut == m:
            upper = ans
            break
        elif cut > m:
            lower = ans
    print(upper)


solve()
