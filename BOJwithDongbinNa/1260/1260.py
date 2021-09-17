from collections import deque
import sys
read = sys.stdin.readline

n, m, start = map(int, read().split())
v = [[] for _ in range(n + 1)]
for i in range(m):
    v1, v2 = map(int, read().split())
    v[v1].append(v2)
    v[v2].append(v1)
for i in range(n + 1):
    v[i].sort()

visited = [False] * (n+1)
res = []
stack = []
stack.append(start)
while stack:
    v1 = stack.pop()
    if not visited[v1]:
        visited[v1] = True
        res.append(str(v1))
        stack += reversed(v[v1])
print(" ".join(res))

visited = [False] * (n+1)
res = []
queue = deque()
queue.append(start)
while queue:
    for _ in range(len(queue)):
        v1 = queue.popleft()
        if not visited[v1]:
            visited[v1] = True
            res.append(str(v1))
            queue += v[v1]
print(" ".join(res))
