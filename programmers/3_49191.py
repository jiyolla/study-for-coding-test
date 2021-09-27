# https://programmers.co.kr/learn/courses/30/lessons/49191
# 순위

# 순위가 확실하다는 것은
# 모든 사람이 나와의 관계가 확실하다는 것이고
# 관계가 확실하다는 것은 이 문제에서 directed graph로 그렸을 때
# 나에게 오는 길이 있다는 것

# 모든 점에 대해서
# 모든 점에 connectivity를 갖는지 테스트하면 된다
# O(N^3)이지만, N이 100이기 때문에 괜찮다
# O(N^2) 솔루션도 있을 거 같은 느낌이다

def solution(n, results):
    adjacent_asc = [[] for _ in range(n + 1)]   # Weaker than me
    adjacent_desc = [[] for _ in range(n + 1)]  # Stronger than me
    for winner, loser in results:
        adjacent_asc[winner].append(loser)
        adjacent_desc[loser].append(winner)

    def dfs_asc(node):
        visited[node] = True
        for stronger in adjacent_asc[node]:
            if not visited[stronger]:
                dfs_asc(stronger)

    def dfs_desc(node):
        visited[node] = True
        for weaker in adjacent_desc[node]:
            if not visited[weaker]:
                dfs_desc(weaker)
    
    count = 0
    for i in range(1, n + 1):
        visited = [True] + [False]*n
        visited[i] = True
        for stronger in adjacent_asc[i]:
            dfs_asc(stronger)
        for weaker in adjacent_desc[i]:
            dfs_desc(weaker)
        if False not in visited:
            count += 1

    return count

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
