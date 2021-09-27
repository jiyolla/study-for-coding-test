# https://programmers.co.kr/learn/courses/30/lessons/62048
# 멀쩡한 사각형

import math


def solution(w, h):
    gcd = math.gcd(w, h)
    w, h = w//gcd, h//gcd

    count = h + w - 1
    # count += sum([h*(r + 1)//w for r in range(w)])
    # count -= sum([h*r//w for r in range(w)])
    # for r in range(w):
    #     # count += h*(r + 1)//w + (0 if h*(r + 1)%w == 0 else 1) - h*r//w
    #     count += h*(r + 1)//w - h*r//w
        
    return w*h*gcd**2 - count*gcd

print(solution(8, 12))
