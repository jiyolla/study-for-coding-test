from collections import deque


n, m = list(map(int, input().split()))

maze_t = ['0'] * (m + 2)
maze_m = [(['0'] + list(input()) + ['0']) for _ in range(n)]
maze_b = ['0'] * (m + 2)
maze = [maze_t] + maze_m + [maze_b]

queue = deque()
queue.append((1, 1))
found = False
d = 0
while True:
    for _ in range(len(queue)):
        x, y = queue.popleft()
        if x == m and y == n:
            found = True
            break
        if maze[y][x + 1] == '1':
            maze[y][x + 1] = '0'
            queue.append((x + 1, y))
        if maze[y][x - 1] == '1':
            maze[y][x - 1] = '0'
            queue.append((x - 1, y))
        if maze[y + 1][x] == '1':
            maze[y + 1][x] = '0'
            queue.append((x, y + 1))
        if maze[y - 1][x] == '1':
            maze[y - 1][x] = '0'
            queue.append((x, y - 1))
    if found:
        print(d + 1)
        break
    d += 1
