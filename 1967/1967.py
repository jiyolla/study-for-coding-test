import sys


def solve():
    sys.setrecursionlimit(10**6)
    read = sys.stdin.readline
    n = int(read())
    child = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        p, c, w = map(int, read().split())
        child[p].append((c, w))

    # 1167번이랑 거의 같다. 방금보다 조금 더 아름답게 짜볼 수 있을 것 같다.
    max_diameter = 0

    def dfs(node):
        nonlocal max_diameter
        candidates = []
        for c, w in child[node]:
            if child[c]:
                w += dfs(c)
            candidates.append(w)
        candidates.sort()
        local_max = sum(candidates[-2:])
        if max_diameter < local_max:
            max_diameter = local_max
        return candidates[-1]
    if child[1]:
        dfs(1)
    # 기가 막힌다. 모든 상황이 다 그냥 처리된다.
    print(max_diameter)


solve()
