# https://programmers.co.kr/learn/courses/30/lessons/67256
# [카카오 인턴] 키패드 누르기

def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def solution(numbers, hand):
    ret = []
    l_pos = [3, 0]
    r_pos = [3, 2]
    for number in numbers:
        if number in [1, 4, 7]:
            ret.append('L')
            l_pos = [number//3, 0]
        elif number in [3, 6, 9]:
            ret.append('R')
            r_pos = [number//3 - 1, 2]
        else:
            number = 11 if number == 0 else number
            pos = [number//3, 1]
            if dist(l_pos, pos) == dist(r_pos, pos):
                if hand == 'right':
                    ret.append('R')
                    r_pos = pos
                else:
                    ret.append('L')
                    l_pos = pos
            elif dist(l_pos, pos) > dist(r_pos, pos):
                ret.append('R')
                r_pos = pos
            else:
                ret.append('L')
                l_pos = pos
    
    return ''.join(ret)

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
