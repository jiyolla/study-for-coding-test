import sys


def solve():
    read = sys.stdin.readline
    print_buf = []
    t = 0
    n, m = map(int, read().split())
    while n != 0 or m != 0:
        t += 1
        adj = [[] for _ in range(n + 1)]
        for _ in range(m):
            u, v = map(int, read().split())
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * (n + 1)
        ans = 0
        for root in range(1, n + 1):
            if visited[root]:
                continue
            stack = [(root, None)]
            has_cycle = False
            while stack and not has_cycle:
                cur, parent = stack.pop()
                visited[cur] = True
                for child in adj[cur]:
                    if child != parent:
                        if visited[child]:
                            has_cycle = True
                            break
                        stack.append((child, cur))
            if not has_cycle:
                ans += 1
        if ans == 0:
            print_buf.append(f'Case {t}: No trees.')
        elif ans == 1:
            print_buf.append(f'Case {t}: There is one tree.')
        else:
            print_buf.append(f'Case {t}: A forest of {ans} trees.')
        n, m = map(int, read().split())
    print('\n'.join(print_buf))


solve()
