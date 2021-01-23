from collections import deque
import sys
read = sys.stdin.readline

m, n = map(int, read().split())
queue = deque()
mature_topbot = ['-1'] * (m+2)
mature_body = []
for i in range(0, n):
    mature_body.append(['-1'] + read().split() + ['-1'])
    for j in range(1, m + 1):
        if mature_body[i][j] == '1':
            queue.append((j, i + 1))

mature = [mature_topbot] + mature_body + [mature_topbot]

d = -1
while queue:
    for _ in range(len(queue)):
        x, y = queue.popleft()
        if mature[y][x + 1] == '0':
            mature[y][x + 1] = '1'
            queue.append((x + 1, y))
        if mature[y][x - 1] == '0':
            mature[y][x - 1] = '1'
            queue.append((x - 1, y))
        if mature[y + 1][x] == '0':
            mature[y + 1][x] = '1'
            queue.append((x, y + 1))
        if mature[y - 1][x] == '0':
            mature[y - 1][x] = '1'
            queue.append((x, y - 1))
    d += 1

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if mature[i][j] == '0':
            d = -1
            break

print(d)
