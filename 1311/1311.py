def solve():
    n = int(input())
    cost = [list(map(int, input().split())) for _ in range(n)]
    """
    mem = {((), ()): 0}
    def dp(worker, work):
        if (worker, work) in mem:
            return mem[(worker, work)]
        ans = 10**4 * 20
        for i in worker:
            for j in work:
                n_worker = list(worker)
                n_worker.remove(i)
                n_worker = tuple(n_worker)
                n_work = list(work)
                n_work.remove(j)
                n_work = tuple(n_work)
                ans = min(ans, cost[i - 1][j - 1] + dp(n_worker, n_work))
        mem[(worker, work)] = ans
        return ans
    print(dp(tuple([i for i in range(n)]), tuple([i for i in range(n)])))
    """
    # 딱 봐도 존나 느려. 완전 탐색임.
    # 완벽한 해결책 떠오름. dp[i+1]는 dp[i]했을 때에 택했던 원소를 택하고, 그 자리에서 새 사람을 배치시키거나, dp[i]를 가져오고, 새 일에 새 사람을 배치시키는 경우로 나누어서 생각하면 편함.
    """
    allocs_pre = []
    dp_pre = 20 * 10**4
    for k in range(n):
        if cost[k][0] < dp_pre:
            dp_pre = cost[k][0]
            allocs_pre = [[k]]
        elif cost[k][0] == dp_pre:
            allocs_pre.append([k])
    for i in range(1, n):
        allocs_cur = []
        dp_cur = 20 * 10**4
        for alloc in allocs_pre:
            for k in range(n):
                if k not in alloc:
                    if cost[k][i] < dp_cur:
                        dp_cur = cost[k][i]
                        allocs_cur = [alloc + [k]]
                    elif cost[k][i] == dp_cur:
                        allocs_cur.append(alloc + [k])
            for j in range(i):
                for k in range(n):
                    if k not in alloc:
                        # i: cur job, j: the job that we wish to change, alloc[j]: the person was in charge of j, k: new person for j
                        n_cost = cost[alloc[j]][i] - cost[alloc[j]][j] + cost[k][j]
                        if n_cost < dp_cur:
                            dp_cur = n_cost
                            allocs_cur = [alloc[:j] + [k] + alloc[j + 1:] + [alloc[j]]]
                        elif n_cost == dp_cur:
                            allocs_cur.append(alloc[:j] + [k] + alloc[j + 1:] + [alloc[j]])
        allocs_pre = allocs_cur
        dp_pre += dp_cur
    print(allocs_pre)
    print(dp_pre)
    """
    # """
    # 문제가 있어. 이 방법은. 기존 방법의 탐색 순서를 조금 수정해보겠다.
    mem = {(0, ): 0}

    # dp(n, work)로 해야겠다. worker를 굳이 매번 순회할 필요없는 거 같음.
    cache_hit = 0

    def dp(n, work):
        nonlocal cache_hit
        # print(f'n: {n}, work: {work}')
        # print(f'mem: {mem}')
        if (n, *work) in mem:
            cache_hit += 1
            return mem[(n, *work)]
        ans = 10**4 * 20
        for i, tbd in enumerate(work):
            ans = min(ans, cost[n - 1][tbd] + dp(n - 1, work[:i] + work[i + 1:]))
        mem[(n, *work)] = ans
        return ans
    print(dp(n, [i for i in range(n)]))
    print(len(mem))
    print(cache_hit)
    # """


solve()
