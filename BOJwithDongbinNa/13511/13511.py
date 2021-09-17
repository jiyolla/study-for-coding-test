import sys
import math


def solve():
    read = sys.stdin.readline
    n = int(read())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v, w = map(int, read().split())
        adj[u].append((v, w))
        adj[v].append((u, w))

    parent = [None] * (n + 1)
    depth = [None] * (n + 1)
    depth[1] = 0
    stack = [(1, 0)]
    max_depth = 0
    while stack:
        cur_node, cur_depth = stack.pop()
        if max_depth < cur_depth:
            max_depth = cur_depth
        for child, cost in adj[cur_node]:
            if depth[child] is None:
                parent[child] = (cur_node, cost)
                depth[child] = cur_depth + 1
                stack.append((child, cur_depth + 1))

    max_power = math.floor(math.log2(max_depth))
    parent_2tothe = [[None] * (n + 1) for _ in range(max_power + 1)]
    for node in range(2, n + 1):
        parent_2tothe[0][node] = parent[node]
    for power in range(1, max_power + 1):
        for node in range(2, n + 1):
            if depth[node] >= (1 << power):
                p_half, cost_half = parent_2tothe[power - 1][node]
                p_full, cost_full = parent_2tothe[power - 1][p_half]
                parent_2tothe[power][node] = (p_full, cost_half + cost_full)

    def parent_n(n, x):
        if n == 0:
            return x, 0
        biggest_power_under = math.floor(math.log2(n))
        next_n = n - (1 << biggest_power_under)
        next_x, cost = parent_2tothe[biggest_power_under][x]
        p, cost_p = parent_n(next_n, next_x)
        return p, cost + cost_p

    # input: two nodes on the same depth
    # output: cost between two nodes, number of nodes between them(inclusive)
    def lca(a, b):
        if parent[a][0] == parent[b][0]:
            return parent[a][1] + parent[b][1], 3
        jump_to_power = None
        for power in range(1, max_power + 1):
            if parent_2tothe[power][a] is None or \
                parent_2tothe[power][b] is None or \
                parent_2tothe[power][a][0] == parent_2tothe[power][b][0]:
                jump_to_power = power - 1
                break
        else:
            jump_to_power = max_power
        p_a = parent_2tothe[jump_to_power][a]
        p_b = parent_2tothe[jump_to_power][b]
        cost, num_nodes = lca(p_a[0], p_b[0])
        return cost + p_a[1] + p_b[1], num_nodes + (2 << jump_to_power)

    print_buf = []
    for _ in range(int(read())):
        cmd, *param = map(int, read().split())
        if cmd == 1:
            u, v = param
            u, v = (u, v) if depth[u] > depth[v] else (v, u)
            u, ans = parent_n(depth[u] - depth[v], u)
            if u != v:
                ans += lca(u, v)[0]
        else:
            u, v, k = param
            if depth[u] >= depth[v]:
                if k <= depth[u] - depth[v] + 1:
                    ans = parent_n(k - 1, u)[0]
                else:
                    k -= depth[u] - depth[v]
                    p_u = parent_n(depth[u] - depth[v], u)[0]
                    num_lca_nodes = lca(p_u, v)[1]
                    if k <= num_lca_nodes // 2:
                        ans = parent_n(k - 1, p_u)[0]
                    else:
                        ans = parent_n(num_lca_nodes - k, v)[0]
            else:
                p_v = parent_n(depth[v] - depth[u], v)[0]
                if p_v != u:
                    num_lca_nodes = lca(u, p_v)[1]
                    if k <= num_lca_nodes // 2:
                        ans = parent_n(k - 1, u)[0]
                    else:
                        ans = parent_n(num_lca_nodes + depth[v] - depth[u] - k, v)[0]
                else:
                    ans = parent_n(depth[v] - depth[u] - k + 1, v)[0]
        print_buf.append(f'{ans}')
    print('\n'.join(print_buf))


solve()
