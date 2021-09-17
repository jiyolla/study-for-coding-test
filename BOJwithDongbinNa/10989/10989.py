import sys
read = sys.stdin.readline
count = [0] * 10001
for _ in range(int(read())):
    count[int(read())] += 1
for i, c in enumerate(count[1:], start=1):
    if c:
        print(''.join([str(i)+'\n']*c), end='')
