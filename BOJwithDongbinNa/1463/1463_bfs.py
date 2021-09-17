from collections import deque


def solve():
    n = int(input())
    queue = deque()
    visited = [False] * 1000001
    queue.append(n)
    visited[n] = True
    count = 0
    while not visited[1]:
        count += 1
        for i in range(len(queue)):
            opd = queue.popleft()
            if opd % 3 == 0 and not visited[opd // 3]:
                visited[opd // 3] = True
                queue.append(opd // 3)
            if opd % 2 == 0 and not visited[opd // 2]:
                visited[opd // 2] = True
                queue.append(opd // 2)
            if opd > 1 and not visited[opd - 1]:
                visited[opd - 1] = True
                queue.append(opd - 1)
    print(count)


solve()
