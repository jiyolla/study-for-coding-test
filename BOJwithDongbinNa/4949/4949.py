import sys

for line in sys.stdin:
    if line == '.\n':
        break
    stack = [' '] * len(line)
    p = 0
    res = 'yes'
    for c in line:
        if c == '(' or c == '[':
            stack[p] = c
            p += 1
        elif c == ')' or c == ']':
            if p == 0:
                res = 'no'
                break
            elif (c == ')' and stack[p - 1] == '(') or \
                (c == ']' and stack[p - 1] == '['):
                p -= 1
            else:
                res = 'no'
                break
    if p != 0:
        res = 'no'
    print(res)