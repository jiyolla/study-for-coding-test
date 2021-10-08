# https://programmers.co.kr/learn/courses/30/lessons/86052
# 빛의 경로 사이클

import sys

sys.setrecursionlimit(10**6)

def solution(grid):
    #   0
    # 3   1
    #   2
    visited = [[[False]*4 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    
    def next_direction(r, c, d):
        if grid[r][c] == 'S':
            return d
        if grid[r][c] == 'L':
            return (d - 1)%4
        if grid[r][c] == 'R':
            return (d + 1)%4
    
    def dfs(r, c, d):
        visited[r][c][d] = True
        
        if d == 0:
            r -= 1
            if r < 0:
                r = len(grid) - 1
        elif d == 1:
            c += 1
            if c == len(grid[0]):
                c = 0
        elif d == 2:
            r += 1
            if r == len(grid):
                r = 0
        elif d == 3:
            c -= 1
            if c < 0:
                c = len(grid[0]) - 1
        
        d = next_direction(r, c, d)
        if not visited[r][c][d]:
            return dfs(r, c, d) + 1
        return 1
        
    
    ret = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            for d in range(4):
                if not visited[r][c][d]:
                    ret.append(dfs(r, c, d))
    
    return sorted(ret)

print(solution(["SL","LR"]))
