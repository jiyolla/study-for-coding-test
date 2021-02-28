import math


def solve():
    n = int(input())
    w = []
    for _ in range(n):
        w.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(n):
            if w[i][j] == 0 and i != j:
                w[i][j] = math.inf

    # dp[i] = (cost, last_city)
    # 여기서 i는 도시방문상태로 0은 모두 미방문, 2**n - 1는 모두 방문.
    # 이었으나, 0번 도시는 이미 방문했기에, n대신 n - 1을 사용함
    # 도시번호는 0부터 시작해서 n - 1까지.
    dp = [(math.inf, None)] * 2**(n - 1)
    dp[0] = (0, 0)
    for i in range(1, 2**(n - 1) - 1):
        # dp[i]를 구하다
        target_city = 1
        masker = 1
        tmp = i
        while tmp:
            if i & masker:
                cost, last_city = dp[i & ~masker]
                # print(f'dst: {bin(i):>8}, src: {bin(i & ~masker):>8}, cost: {cost:>5}, last_city: {last_city}')
                if last_city is not None:
                    new_cost = cost + w[last_city][target_city]
                    if new_cost < dp[i][0]:
                        dp[i] = (new_cost, target_city)
            masker <<= 1
            tmp //= 2
            target_city += 1
    ans = math.inf
    for i in range(n - 1):
        # 하나씩 모자란 친구들(0번 도시 모자란 친구는 제외하고)
        cost, last_city = dp[(2**(n - 1) - 1) & ~(1 << i)]
        if last_city is not None:
            new_cost = cost + w[last_city][i + 1] + w[i + 1][0]
            if new_cost < ans:
                ans = new_cost
    print(ans)


solve()
