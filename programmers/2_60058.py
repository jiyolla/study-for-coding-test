# https://programmers.co.kr/learn/courses/30/lessons/60058
# 괄호 변환

def solution(p):
    def inverse(p):
        return ''.join([')' if item == '(' else '(' for item in p])

    def is_correct(p):
        stack = []
        try:
            for item in p:
                if item == '(': 
                    stack.append(0)
                else:
                    stack.pop()
        except IndexError:
            return False
        return True

    def transform(p):
        if not p:
            return p
        
        l_count = 0
        r_count = 0
        for i in range(len(p)):
            if p[i] == '(':
                l_count += 1
            elif p[i] == ')':
                r_count += 1
            if l_count != 0 and l_count == r_count:
                break
        
        u = p[:i + 1]
        v = p[i + 1:]
        if is_correct(u):
            return u + transform(v)

        ret = '(' + transform(v) + ')' + inverse(u[1:-1])

        return ret

    return transform(p)

print(solution("(()())()"))
