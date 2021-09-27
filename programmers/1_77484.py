# https://programmers.co.kr/learn/courses/30/lessons/77484
# 로또의 최고 순위와 최저 순위

def count_to_rank(count):
    return min(6, 7 - count)


def solution(lottos, win_nums):
    base = 0
    num_joker = 0
    for num in lottos:
        if num == 0:
            num_joker += 1
        elif num in win_nums:
            base += 1
    
    return count_to_rank(base + num_joker), count_to_rank(base)

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
