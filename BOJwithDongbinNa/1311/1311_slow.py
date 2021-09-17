def solve():
    n = int(input())
    cost = [list(map(int, input().split())) for _ in range(n)]
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
        # print(worker)
        # print(work)
        return ans
    print(dp(tuple([i for i in range(n)]), tuple([i for i in range(n)])))


solve()
