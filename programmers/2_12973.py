# https://programmers.co.kr/learn/courses/30/lessons/12973
# 짝지어 제거하기

def solution(s):
    stack = []
    for l in s:
        if stack and stack[-1] == l:
            stack.pop(-1)
        else:
            stack.append(l)
    return 0 if stack else 1

print(solution())
