# https://programmers.co.kr/learn/courses/30/lessons/43165
# 타겟 넘버

def solution(numbers, target):
    def dfs(numbers, idx, num):
        if idx == len(numbers):
            return 1 if num == 0 else 0
        ret = dfs(numbers, idx + 1, num - numbers[idx])
        ret += dfs(numbers, idx + 1, num + numbers[idx])
        return ret
    
    return dfs(numbers, 0, target)

print(solution([1, 1, 1, 1, 1], 3))
