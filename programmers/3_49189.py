# https://programmers.co.kr/learn/courses/30/lessons/49189
# 가장 먼 노드

import heapq


def solution(n, edge):
    adjacent = [[] for _ in range(n + 1)]
    for src, dst in edge:
        adjacent[src].append(dst)
        adjacent[dst].append(src)

    visited = [False] * (n + 1)
    hq = [(0, 1)]
    visited[1] = True
    max_depth = 0
    cur_depth_count = 0
    while hq:
        depth, src = heapq.heappop(hq)
        if depth > max_depth:
            max_depth = depth
            cur_depth_count = 1
        else:
            cur_depth_count += 1
        for node in adjacent[src]:
            if not visited[node]:
                heapq.heappush(hq, (depth + 1, node))
                visited[node] = True

    return cur_depth_count

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
