# https://programmers.co.kr/learn/courses/30/lessons/64065
# 튜플

from collections import Counter

def solution(s):
    c = Counter()
    s = s.replace('{', '')
    s = s.replace('}', '')
    for num in map(int, s.split(',')):
        c[num] += 1

    return [k for k, v in c.most_common()]


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
