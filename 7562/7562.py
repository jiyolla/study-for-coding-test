from collections import deque


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        visited = [[False] * n for _ in range(n)]
        x0, y0 = map(int, input().split())
        x1, y1 = map(int, input().split())
        queue = deque()
        queue.append((x0, y0))
        visited[x0][y0] = True
        ans = 0
        while not visited[x1][y1]:
            ans += 1
            for i in range(len(queue)):
                x, y = queue.popleft()
                if x - 1 >= 0 and y - 2 >= 0 and not visited[x - 1][y - 2]:
                    visited[x - 1][y - 2] = True
                    queue.append((x - 1, y - 2))
                if x - 2 >= 0 and y - 1 >= 0 and not visited[x - 2][y - 1]:
                    visited[x - 2][y - 1] = True
                    queue.append((x - 2, y - 1))
                if x + 1 < n and y + 2 < n and not visited[x + 1][y + 2]:
                    visited[x + 1][y + 2] = True
                    queue.append((x + 1, y + 2))
                if x + 2 < n and y + 1 < n and not visited[x + 2][y + 1]:
                    visited[x + 2][y + 1] = True
                    queue.append((x + 2, y + 1))
                if x + 1 < n and y - 2 >= 0 and not visited[x + 1][y - 2]:
                    visited[x + 1][y - 2] = True
                    queue.append((x + 1, y - 2))
                if x + 2 < n and y - 1 >= 0 and not visited[x + 2][y - 1]:
                    visited[x + 2][y - 1] = True
                    queue.append((x + 2, y - 1))
                if x - 1 >= 0 and y + 2 < n and not visited[x - 1][y + 2]:
                    visited[x - 1][y + 2] = True
                    queue.append((x - 1, y + 2))
                if x - 2 >= 0 and y + 1 < n and not visited[x - 2][y + 1]:
                    visited[x - 2][y + 1] = True
                    queue.append((x - 2, y + 1))
        print(ans)


solve()
