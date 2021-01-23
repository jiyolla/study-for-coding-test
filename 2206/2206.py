from collections import deque

n, m = map(int, input().split())
# 0: unvisited
# 1: wall
# 2: visited with smash on
# 3: visited without smash
maze = [list(input()) for _ in range(n)]

escaped = False
queue = deque()
queue.append((0, 0, False))
time = 0
while queue and not escaped:
    time += 1
    for _ in range(len(queue)):
        x, y, smashed = queue.popleft()
        if x == m - 1 and y == n - 1:
            escaped = True
            break
        if x + 1 < m:
            if maze[y][x + 1] == '0':
                maze[y][x + 1] = '2' if smashed else '3'
                queue.append((x + 1, y, smashed))
            elif not smashed:
                if maze[y][x + 1] == '1':
                    queue.append((x + 1, y, True))
                elif maze[y][x + 1] == '2':
                    maze[y][x + 1] = '3'
                    queue.append((x + 1, y, smashed))
        if y + 1 < n:
            if maze[y + 1][x] == '0':
                maze[y + 1][x] = '2' if smashed else '3'
                queue.append((x, y + 1, smashed))
            elif not smashed:
                if maze[y + 1][x] == '1':
                    queue.append((x, y + 1, True))
                elif maze[y + 1][x] == '2':
                    maze[y + 1][x] = '3'
                    queue.append((x, y + 1, smashed))
        if x > 0:
            if maze[y][x - 1] == '0':
                maze[y][x - 1] = '2' if smashed else '3'
                queue.append((x - 1, y, smashed))
            elif not smashed:
                if maze[y][x - 1] == '1':
                    queue.append((x - 1, y, True))
                elif maze[y][x - 1] == '2':
                    maze[y][x - 1] = '3'
                    queue.append((x - 1, y, smashed))
        if y > 0:
            if maze[y - 1][x] == '0':
                maze[y - 1][x] = '2' if smashed else '3'
                queue.append((x, y - 1, smashed))
            elif not smashed:
                if maze[y - 1][x] == '1':
                    queue.append((x, y - 1, True))
                elif maze[y - 1][x] == '2':
                    maze[y - 1][x] = '3'
                    queue.append((x, y - 1, smashed))

if escaped:
    print(time)
else:
    print(-1)
