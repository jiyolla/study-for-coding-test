from sys import stdin
read = stdin.readline()
num_node = int(read())

connected = [[] for i in range(num_node + 1)]
visited = [False] * (num_node + 1)

num_edge = int(read())

for e in stdin:
    n1, n2 = list(map(int, e.split()))
    connected[n1].append(n2)
    connected[n2].append(n1)


def dfs(node):
    if not visited[node]:
        visited[node] = True
        for n in connected[node]:
            dfs(n)


dfs(1)
print(sum(visited[2:]))
