import sys

stack = [0] * int(sys.stdin.readline())
p = 0
for cmd in sys.stdin:
    if cmd.startswith('push'):
        stack[p] = int(cmd.split()[1])
        p += 1
    elif cmd.startswith('pop'):
        print(stack[p - 1] if p > 0 else -1)
        p -= 1 if p > 0 else 0
    elif cmd.startswith('size'):
        print(p)
    elif cmd.startswith('empty'):
        print(1 if p == 0 else 0)
    elif cmd.startswith('top'):
        print(stack[p - 1] if p > 0 else -1)
