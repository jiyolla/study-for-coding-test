# https://programmers.co.kr/learn/courses/30/lessons/17677
# [1차] 뉴스 클러스터링

import re
from collections import Counter


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    set_1 = Counter()
    set_2 = Counter()
    for i in range(len(str1) - 1):
        if all(c.isalpha() for c in str1[i:i + 2]):
            set_1[str1[i:i + 2]] += 1
    for i in range(len(str2) - 1):
        if all(c.isalpha() for c in str2[i:i + 2]):
            set_2[str2[i:i + 2]] += 1
    
    intersection = 0
    union = 0
    if len(set_1) == 0 and len(set_2) == 0:
        return 65536
    for el in set_1:
        intersection += min(set_1[el], set_2[el])
        union += max(set_1[el], set_2[el])
    for el in set_2:
        if set_1[el] == 0:
            union += set_2[el]
    
    return int(intersection / union * 65536)

print(solution('FRANCE', 'french'))
