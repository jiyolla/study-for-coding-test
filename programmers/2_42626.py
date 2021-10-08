# https://programmers.co.kr/learn/courses/30/lessons/42626
# 더 맵게

import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    ret = 0
    while len(scoville) > 1:
        min_0 = heapq.heappop(scoville)
        min_1 = heapq.heappop(scoville)
        if min_0 < K:
            heapq.heappush(scoville, min_0 + 2*min_1)
            ret += 1
        else:
            return ret
    
    return -1 if scoville[0] < K else ret

print(solution([1, 2, 3, 9, 10, 12], 7))
