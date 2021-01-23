#@profile
def solve():
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    # 생각해보자
    # 1, 2, 5, 7, 10, ... 이런식으로 동자의 가치가 있다고 치자
    # 이때 123원을 만든다고 하자
    # 이때 가능한 조합의 수를 구한다라?
    # 1로 돌면서 dp[1]~dp[123]까지 한번 돌고
    # 아니
    # dp[i] = dp[i - 1](1 더해서), dp[i - k]k 더해서...
    # 순서만 바뀐 것은 어떻게 중복 제거?
    # 애초에 dp[i]를 중복 제거한 걸로? 아니면 dp[k]구하고 중복 제거 따로?
    # dp[i]를 길이의 n의 배열로?
    # 각 원소i갸 i-th 가치의 동전의 개수 저장?아니 그러면 한 가지 경우에 대해서만 표시지하게 됨
    # dp[i]를 뭘로 정의해야 될까가 관건
    # dp[i] i를 동전의 종류수로 할지, 만드고자 하는 금액으로 할지?
    # 아니면 냅색 때채럼 이차?
    # 즉 dp[i][j]는 i종의 동전으로 j원을 만들 떄 경우의 수?
    # 그렇다면 쉽게 상관관계를 찾을 수 있는가?
    # dp[i][j]는? 새로 1종의 동전을 추가할 때, 즉 dp[i + 1][j]는 적어도 dp[i][j]보다 크고, dp[i][j]를 전부 포함하고, 
    # 추가적으로 사용했던 일부의 동전들을 새로운 동전으로 치환하여 경우의 수를 늘릴 수 있다
    # 즉 우리는 치환 가능한 조합을 찾으면 된다?
    # 어떻게 찾는가? dp[i][j - 새 동전의 가치]이면 하나만 치환할 때 경우의 수 아닌가?
    # 이런식으로 dp[i][j - j // 새 동전의 가치 * 새 동전의 가치]까지?
    # ok구현가자
    # 2차로 안 한다?
    # dp[i]는 i원을 만드는 경우의 수?
    # dp의 상관관계는 어떻게 되는가?
    # dp[i] += dp[i - c[j]]는 중복 카운트하지 않는가?
    # 아닌가?
    dp = [0] * (k + 1)
    dp[0] = 1
    for i in range(n):
        for j in range(1, k + 1):
            dp[j] += dp[j - coins[i]] if j >= coins[i] else 0
    print(dp[-1])

    dp = [[1] * (k + 1) for _ in range(n)]
    for i in range(k + 1):
        dp[0][i] = 1 if i % coins[0] == 0 else 0
    for i in range(1, n):
        for j in range(1, k + 1):
            dp[i][j] = sum([dp[i - 1][j - coins[i] * m] for m in range(j // coins[i] + 1)])
    print(dp[-1][-1])

    dp_last = [1] * (k + 1)
    dp_new = [1] * (k + 1)
    for i in range(k + 1):
        dp_last[i] = 1 if i % coins[0] == 0 else 0
    for i in range(1, n):
        for j in range(1, k + 1):
            # dp[i][j]를 구해야 한다
            dp_new[j] = sum([dp_last[j - coins[i] * m] for m in range(j // coins[i] + 1)])
        dp_last = dp_new[:]
    print(dp_new[-1])

    """
    mem = {}
    for i in range(k + 1):
        mem[(1, i)] = 1 if i % coins[0] == 0 else 0
    def recur(i, v):
        if v == 0:
            return 1
        if (i, v) in mem:
            return mem[(i, v)]
        res = 0
        for j in range(v // coins[i - 1] + 1):
            res += recur(i - 1, v - coins[i - 1] * j)
        mem[(i, v)] = res
        return res
    print(recur(n, k))
    """


solve()
