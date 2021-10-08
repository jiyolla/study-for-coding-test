# https://programmers.co.kr/learn/courses/30/lessons/86971
# 전력망을 둘로 나누기

def solution(n, wires):
    min_diff = n
    for discarded in range(len(wires)):
        adjacent = [[] for _ in range(n + 1)]
        for v1, v2 in wires[:discarded]:
            adjacent[v1].append(v2)
            adjacent[v2].append(v1)
        for v1, v2 in wires[discarded + 1:]:
            adjacent[v1].append(v2)
            adjacent[v2].append(v1)

        visited = [False] * (n + 1)
        def dfs(node):
            visited[node] = True
            ret = 1
            for child in adjacent[node]:
                if not visited[child]:
                    ret += dfs(child)
            return ret
        diff = abs(n - 2*dfs(1))
        if min_diff > diff:
            min_diff = diff
            
    return min_diff


print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
