# https://programmers.co.kr/learn/courses/30/lessons/43238
# 입국심사

# 최소공배수 기준으로 사이클이 생긴다.
# 하지만 최소공배수 자체가 매우 커서 큰 의미는 없을 수 있다.
# 최소공배수를 기준으로 DP테이블을 만드는 것도 가능할 거 같은데
# 최소공배수가 매우클 수 있기 때문에 단순하게 하는 것은 어려울 거 같다.
# 10명이 있고, [x, y, z]걸린다고 해보자.
# 각각 a, b, c명을 처리하는 게 베스트라고 하면
# minimize max(ax, by, cz), where a+b+c=10가 된다.
# 약간 updown방식으로 범위를 좁힐 수 있을 것 같다
# 일단 확실한 upper bound중 하나는 가장 빠른 사람이 혼자 다 하는 것.
# lower bound중 하나는 모든 사람이 평균 일률로 일한다고 가정했을 때, 아니면 더 단순하게 모든 사람이 가장 빠른 사람처럼 일한다고 가정.
# 이랬을 중간 시간이 취득가능한지 확인한다.
# 중간 시간을 각 사람의 처리시간으로 나누고, 몫을 다 더해서 손님 수와 비교한다.
# 손님 수가 더 크면, 불가능하다는 것이고, 이게 새 lowerbound, 정확히는 lowerbound - 1.
# 가능하다면, 이게 새 upperbound
# upper==lower까지 반복.

def solution(n, times):
    upper = n*min(times)
    lower = n*min(times)//len(times)

    while lower < upper:
        mid = (upper + lower)//2
        count = 0
        for time in times:
            count += mid//time
        if count < n:
            lower = mid + 1
        else:
            upper = mid
        
    return lower

print(solution(6, [7, 10]))
