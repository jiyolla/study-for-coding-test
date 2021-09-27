# https://programmers.co.kr/learn/courses/30/lessons/43162
# 네트워크

def solution(n, computers):
    visited = [False] * n

    adjacent = [[] for _  in range(n)]
    for r in range(n):
        for c in range(r):
            if computers[r][c] == 1:
                adjacent[r].append(c)
                adjacent[c].append(r)
    
    def dfs(node):
        visited[node] = True
        for connected in adjacent[node]:
            if not visited[connected]:
                dfs(connected)
    
    count = 0
    for i in range(n):
        if not visited[i]:
            count += 1
            dfs(i)
    
    return count

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
