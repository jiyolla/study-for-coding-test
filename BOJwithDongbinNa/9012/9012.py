import sys

sys.stdin.readline()

for exp in sys.stdin:
    stack = [' '] * len(exp)
    cursor = 0
    res = 'YES'
    for p in exp:
        if p == '(':
            stack[cursor] = p
            cursor += 1
        elif p == ')':
            if cursor == 0 or stack[cursor - 1] == ')':
                res = 'NO'
                break
            else:
                cursor -= 1
    if cursor != 0:
        res = 'NO'
    print(res)
