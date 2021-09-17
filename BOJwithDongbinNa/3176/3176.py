import sys
import math

@profile
def solve():
    read = sys.stdin.readline
    n = int(read())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b, c = map(int, read().split())
        adj[a].append((b, c))
        adj[b].append((a, c))

    # parent[node] = (parent_node, min_dist, max_dist).
    parent = [None] * (n + 1)
    depth = [None] * (n + 1)
    stack = [(1, 0)]
    depth[1] = 0
    parent[1] = (1, None, None)
    max_depth = 0
    while stack:
        cur_node, cur_depth = stack.pop()
        if max_depth < cur_depth:
            max_depth = cur_depth
        for child, dist in adj[cur_node]:
            if child != parent[cur_node][0]:
                parent[child] = (cur_node, dist, dist)
                depth[child] = cur_depth + 1
                stack.append((child, cur_depth + 1))

    max_power = math.floor(math.log2(max_depth))
    parent_2tothe = [[None] * (n + 1) for _ in range(max_power + 1)]
    for node in range(2, n + 1):
        parent_2tothe[0][node] = parent[node]
    for power in range(1, max_power + 1):
        for node in range(2, n + 1):
            if depth[node] >= (1 << power):
                p_half, min_dist_half, max_dist_half = parent_2tothe[power - 1][node]
                p_full, min_dist_full, max_dist_full = parent_2tothe[power - 1][p_half]
                parent_2tothe[power][node] = (p_full, min(min_dist_half, min_dist_full), max(max_dist_half, max_dist_full))

    def parent_n(n, x):
        if n == 0:
            return x, math.inf, 0
        biggest_power_under = math.floor(math.log2(n))
        next_n = n - (1 << biggest_power_under)
        next_x, min_dist, max_dist = parent_2tothe[biggest_power_under][x]
        p, min_dist_p, max_dist_p = parent_n(next_n, next_x)
        return p, min(min_dist, min_dist_p), max(max_dist, max_dist_p)

    def find_LCA(a, b):
        if parent[a][0] == parent[b][0]:
            return min(parent[a][1], parent[b][1]), max(parent[a][2], parent[b][2])
        for power in range(1, max_power + 1):
            if parent_2tothe[power][a] is None or \
                parent_2tothe[power][b] is None or \
                parent_2tothe[power][a][0] == parent_2tothe[power][b][0]:
                p_a = parent_2tothe[power - 1][a]
                p_b = parent_2tothe[power - 1][b]
                break
        else:
            p_a = parent_2tothe[max_power][a]
            p_b = parent_2tothe[max_power][b]
        min_dist, max_dist = find_LCA(p_a[0], p_b[0])
        return min(min_dist, p_a[1], p_b[1]), max(max_dist, p_a[2], p_b[2])

    print_buf = []
    for _ in range(int(read())):
        d, e = map(int, read().split())
        d, e = (d, e) if depth[d] > depth[e] else (e, d)
        d, min_dist, max_dist = parent_n(depth[d] - depth[e], d)
        if d != e:
            min_dist_lca, max_dist_lca = find_LCA(d, e)
            if min_dist > min_dist_lca:
                min_dist = min_dist_lca
            if max_dist < max_dist_lca:
                max_dist = max_dist_lca
        print_buf.append(f'{min_dist} {max_dist}')
    print('\n'.join(print_buf))


solve()
