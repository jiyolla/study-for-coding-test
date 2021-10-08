# https://programmers.co.kr/learn/courses/30/lessons/42586
# 기능개발

def solution(progresses, speeds):
    etds = []
    for progress, speed in zip(progresses, speeds):
        etd = (100 - progress + speed - 1)//speed
        etds.append(etd)
    ret = []
    last_day = 0
    for etd in etds:
        if etd <= last_day:
            ret[-1] += 1
        else:
            ret.append(1)
            last_day = etd

    return ret

print(solution([93, 30, 55], [1, 30, 5]))
