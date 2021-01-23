def solve():
    n, m = map(int, input().split())
    mem = list(map(int, input().split()))
    cost = list(map(int, input().split()))

    # 냅색 문제처럼 풀고, 다만 가치합이 m보다 큰 경우에 대해서는 cost를 조사해, 최소의 cost를 기록하여 문제를 풀 수 있겠다.
    # 그러나 문제점이 하나 있다. m의 범위가 무려 10,000,000이라는 건데... 괜찮나?
    # 그리고 최선의 해결책은 아닌듯 하다. 10**7 * 10**2 = 10**9라...
    # 다른 방법을 생각해보자.
    # 냅색 문제는 제한된 무게 안에서 최대 가치를 찾는 거라면, 이 문제는 제한된 가치 안에서 최소 무게를 찾는 것.
    # 어떻게 잘 전환해볼까?
    # 모두 다 가져간 상태에서 시작해서 하나씩 빼볼 수 있는지 테스트하는 걸로 할까?
    # 즉, dp[i][j]는 i번째 원소까지 빼기를 허락했을 때, 
    # 아, 아니다. 깔끔한 해결책 떠올림.
    # 현재 총 메모리는 sum(m_i)이다. 여기서 최소로 확보해야 되는 공간 m을 빼면, 우리가 최대로 사용할 수 있는 메모리 공간이 나온다.
    # 이 공간 안에서 cost의 합이 최대가 되도록하면 된다. 그래야, 남은 프로그램들의 cost의 합이 최소가 되고, 이 프로그램들이 비활성화될 것들이기 때문이다.
    # 즉, 완전 냅색 문제 그대로 풀면 된다.
    # 다만, m의 범위가 기가막히기 때문에, 바텀업 보단느 탑다운으로 가겠다.
    """
    cache = {}

    def dp(cap, i):
        if i == 0:
            cache[(cap, i)] = 0
            return 0
        if (cap, i) in cache:
            return cache[(cap, i)]
        cache[(cap, i)] = dp(cap, i - 1) if cap - mem[i - 1] < 0 else max(dp(cap - mem[i - 1], i - 1) + cost[i - 1], dp(cap, i - 1)) 
        return cache[(cap, i)]
    print(sum(cost) - dp(sum(mem) - m, n))
    print(len(cache))
    """
    # 메모리 초과 뜬다
    # 바텀업으로 해서 왼도우 슬라이싱으로 올라와야 되나...?
    """
    cap = sum(mem) - m
    dp_pre = [0 for _ in range(cap + 1)]
    for i in range(n):
        dp_cur = [0 for _ in range(cap + 1)]
        dp_cur[:mem[i]] = dp_pre[:mem[i]]
        for j in range(mem[i], cap + 1):
            dp_cur[j] = max(dp_pre[j - mem[i]] + cost[i], dp_pre[j])
        dp_pre = dp_cur
    print(sum(cost) - dp_pre[-1])
    """
    # 이렇게 해도 메모리 초과
    # 그럴만도 한 게 sum(mem) - m은 최대 10**9이 될 수 있다...최소 1기가바이트다
    # 방법 자체는 문제가 없는데, 제한 조건을 초과한다라...흠
    # cost를 기준으로 다시 냅색으로 풀어보자
    cap = sum(cost)
    ans = cap
    dp_pre = [0 for _ in range(ans + 1)]
    for i in range(n):
        dp_cur = [0 for _ in range(ans + 1)]
        dp_cur[:cost[i]] = dp_pre[:cost[i]]
        for j in range(cost[i], ans + 1):
            dp_cur[j] = max(dp_pre[j - cost[i]] + mem[i], dp_pre[j])
            if dp_cur[j] >= m:
                ans = j
                break
        dp_pre = dp_cur
    print(ans)


solve()
