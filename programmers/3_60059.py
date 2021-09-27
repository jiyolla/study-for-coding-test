# https://programmers.co.kr/learn/courses/30/lessons/60059
# 자물쇠와 열쇠

# Lock에서 매칭해야될 최소 패턴 찾고, 표현은 실제 2d list로
# 4개의 방향으로 확장을 하고
# 그 패턴을 Key에서 찾으면 된다. 
# N, M이 최대 20이라 시간 괜찮.

def solution(key, lock):
    r_0 = len(lock) - 1
    r_1 = 0
    c_0 = len(lock[0]) - 1
    c_1 = 0
    for r in range(len(lock)):
        for c in range(len(lock[r])):
            if lock[r][c] == 0:
                if r_0 > r:
                    r_0 = r
                if r_1 < r:
                    r_1 = r
                if c_0 > c:
                    c_0 = c
                if c_1 < c:
                    c_1 = c

    if r_1 < r_0 or c_1 < c_0:
        return True
    
    patterns = [[[lock[r][c] for c in range(c_0, c_1 + 1)] for r in range(r_0, r_1 + 1)]]
    for i in range(3):
        patterns.append(list(map(list, zip(*reversed(patterns[i])))))
    
    for i in range(len(key)):
        key[i] = [1 - i for i in key[i]]

    for pattern in patterns:
        for r in range(len(key) - len(pattern) + 1):
            for c in range(len(key[0]) - len(pattern[0]) + 1):
                for key_row, pattern_row in zip(key[r:], pattern):
                    if key_row[c:c + len(pattern_row)] != pattern_row:
                        break
                else:
                    return True

    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
