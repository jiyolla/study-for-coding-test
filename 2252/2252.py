import sys


def solve():
    read = sys.stdin.readline
    n, m = map(int, read().split())
    graph = [[] for _ in range(n + 1)]
    indegree = [0 for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, read().split())
        graph[a].append(b)
        indegree[b] += 1
    stack = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            stack += [i]
    ans = []
    while stack:
        v1 = stack.pop()
        ans.append(str(v1))
        for v2 in graph[v1]:
            indegree[v2] -= 1
            if indegree[v2] == 0:
                stack += [v2]
    print(' '.join(ans))


solve()
