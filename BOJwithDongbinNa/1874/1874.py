import sys

stack = [0] * int(sys.stdin.readline())
p = 0
next_int = 1
res = ""
for n in sys.stdin:
    if p == 0:
        res += '+\n'
        stack[p] = next_int
        next_int += 1
        p += 1
    if stack[p - 1] > int(n):
        res = 'NO'
        break
    while stack[p - 1] < int(n):
        res += '+\n'
        stack[p] = next_int
        next_int += 1
        p += 1
    res += '-\n'
    p -= 1
print(res)
