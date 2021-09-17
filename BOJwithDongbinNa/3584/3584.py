import sys


def solve():
    read = sys.stdin.readline
    print_buf = []
    for _ in range(int(read())):
        n = int(read())
        parent = [None] * (n + 1)
        for _ in range(n - 1):
            a, b = map(int, read().split())
            parent[b] = a
        c1, c2 = map(int, read().split())
        visited = [False] * (n + 1)
        visited[c1] = True
        while parent[c1] is not None:
            c1 = parent[c1]
            visited[c1] = True
        while not visited[c2]:
            c2 = parent[c2]
        print_buf.append(f'{c2}')
    print('\n'.join(print_buf))


solve()
