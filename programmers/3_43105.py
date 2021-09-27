# https://programmers.co.kr/learn/courses/30/lessons/43105
# 정수 삼각형

def solution(triangle):
    mem = [[0]*(i + 1) for i in range(len(triangle))]
    mem[0][0] = triangle[0][0]
    for r in range(1, len(triangle)):
        mem[r][0] = mem[r - 1][0] + triangle[r][0]
        for c in range(1, r):
            mem[r][c] = max(mem[r - 1][c - 1], mem[r - 1][c]) + triangle[r][c]
        mem[r][r] = mem[r - 1][r - 1] + triangle[r][r]
    
    return max(mem[-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
