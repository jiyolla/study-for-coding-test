import sys
import heapq


def solve():
    read = sys.stdin.readline
    n, m = map(int, read().split())
    prereq = [[] for _ in range(n + 1)]
    prereq_count = [0] * (n + 1)
    """
    for _ in range(m):
        a, b = map(int, read().split())
        heapq.heappush(prereq[b], a)
        prereq_count[b] += 1
    ans = []
    solved = [False] * (n + 1)
    """
    """
    while len(ans) < n:
        for i in range(1, n + 1):
            if prereq_count[i] == 0 and not selected[i]:
                q.append(i)
                ans.append(str(i))
                selected[i] = True
                break
        while q:
            cur = q.popleft()
            for i in range(1, n + 1):
                if cur in prereq[i]:
                    prereq_count[i] -= 1
                    if prereq_count == 0:
                        q.append(i)
                        ans.append(str(i))
                        selected[i] = True
    print(' '.join(ans))
    """
    # 시간 초과 뜨는데
    # 좋은 방법이 생각남
    # 거꾸로 하는 거임
    # prereq가 먼저 풀면 좋은 문제를 가리키는 리스트가 아니라 이 문제를 먼저 푸는 문제로 요구하는 문제들을 가라키는 리스트로 하는 것이다
    # """
    for _ in range(m):
        a, b = map(int, read().split())
        # 문제a를 문제b보다 먼저 푸는 게 좋다
        prereq[a].append(b)
        prereq_count[b] += 1
    h = []
    ans = []
    for i in range(1, n + 1):
        if prereq_count[i] == 0:
            heapq.heappush(h, i)
    while h:
        cur = heapq.heappop(h)
        ans.append(str(cur))
        for i in prereq[cur]:
            prereq_count[i] -= 1
            if prereq_count[i] == 0:
                heapq.heappush(h, i)
    print(' '.join(ans))
    # """
    # 문제를 잘못 이해했네
    # 무조건 1부터 푸는 거네. 다만 1번 푸는데 필요한 문제가 있으면 그거 다 풀고 1번 푸고, 그 다음에 2번 이런식이군.
    # 그러면 원래대로 하는 게 낫다.
    """
    def solve_problem(i):
        for p in prereq[i]:
            print(i, p)
            if not solved[p]:
                solve_problem(p)
        ans.append(str(i))
        solved[i] = True
        return
    for i in range(1, n + 1):
        if not solved[i]:
            solve_problem(i)
    print(' '.join(ans))
    """


solve()
