# https://programmers.co.kr/learn/courses/30/lessons/77485
# 행렬 테두리 회전하기

def solution(rows, columns, queries):
    matrix = [[r*columns + c + 1 for c in range(columns)] for r in range(rows)]
    
    ret = []
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        old_0_0 = matrix[x1][y1]
        query_min = old_0_0
        for r in range(x1, x2):
            matrix[r][y1] = matrix[r + 1][y1]
            if query_min > matrix[r][y1]:
                query_min = matrix[r][y1]
        for c in range(y1, y2):
            matrix[x2][c] = matrix[x2][c + 1]
            if query_min > matrix[x2][c]:
                query_min = matrix[x2][c]
        for r in range(x2, x1, -1):
            matrix[r][y2] = matrix[r - 1][y2]
            if query_min > matrix[r][y2]:
                query_min = matrix[r][y2]
        for c in range(y2, y1, -1):
            matrix[x1][c] = matrix[x1][c - 1]
            if query_min > matrix[x1][c]:
                query_min = matrix[x1][c]
        matrix[x1][y1 + 1] = old_0_0
        ret.append(query_min)
    
    return ret

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
