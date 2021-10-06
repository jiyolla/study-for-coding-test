# https://programmers.co.kr/learn/courses/30/lessons/86491
# 최소직사각형

def solution(sizes):
    max_width = 0
    max_height = 0
    for size in sizes:
        width, height = min(size), max(size)
        if max_width < width:
            max_width = width
        if max_height < height:
            max_height = height
    
    return max_width * max_height

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
