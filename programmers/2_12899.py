# https://programmers.co.kr/learn/courses/30/lessons/12899
# 124 나라의 숫자

def solution(n):
    def recursive(n, i):
        if i == 0:
            return str(n - 1)
        a = (n - 1) // 3**i
        return str(a) + recursive(n - a*3**i, i - 1)

    for i in range(100):
        if 3**(i + 1) > n:
            break
        else:
            n -= 3**(i + 1)
    if n == 0:
        return '4'*i

    ret = []
    for r in recursive(n, i):
        if r == '0':
            ret.append('1')
        elif r == '1':
            ret.append('2')
        elif r == '2':
            ret.append('4')
    return ''.join(ret)

print(solution(38))
