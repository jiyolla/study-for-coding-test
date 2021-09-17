from collections import deque

n, k = map(int, input().split())
visited = [False] * 100001

t = 0
found = False
if n == k:
    found = True
queue = deque()
queue.append(n)
while queue and not found:
    for _ in range(len(queue)):
        cur = queue.popleft()
        if cur < 100000 and not visited[cur + 1]:
            if cur + 1 == k:
                found = True
                break
            visited[cur + 1] = True
            queue.append(cur + 1)
        if cur > 0 and not visited[cur - 1]:
            if cur - 1 == k:
                found = True
                break
            visited[cur - 1] = True
            queue.append(cur - 1)
        if cur * 2 <= 100000 and not visited[cur * 2]:
            if cur * 2 == k:
                found = True
                break
            visited[cur * 2] = True
            queue.append(cur * 2)
    t += 1
print(t)
