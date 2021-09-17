from collections import deque


def solve():
    n, m = list(map(int, input().split()))

    maze = [list(input()) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    queue = deque()
    queue.append((0, 0))
    found = False
    for d in range(n * m):
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if x == m - 1 and y == n - 1:
                found = True
                break
            if x + 1 < m and maze[y][x + 1] == '1' and not visited[y][x + 1]:
                visited[y][x + 1] = True
                queue.append((x + 1, y))
            if x > 0 and maze[y][x - 1] == '1' and not visited[y][x - 1]:
                visited[y][x - 1] = True
                queue.append((x - 1, y))
            if y + 1 < n and maze[y + 1][x] == '1' and not visited[y + 1][x]:
                visited[y + 1][x] = True
                queue.append((x, y + 1))
            if y > 0 and maze[y - 1][x] == '1' and not visited[y - 1][x]:
                visited[y - 1][x] = True
                queue.append((x, y - 1))
        if found:
            print(d + 1)
            break


if __name__ == '__main__':
    solve()
