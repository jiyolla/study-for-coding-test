import sys
import math


def solve():
    read = sys.stdin.readline
    n = int(read())
    adj = [[] for _ in range(n + 1)]
    # dist[(a, b)] = (min, max).
    # min and max of the dist between node a and b.
    dist = {}
    for _ in range(n - 1):
        a, b, c = map(int, read().split())
        adj[a].append(b)
        adj[b].append(a)
        dist[(a, b)] = dist[(b, a)] = (c, c)

    parent = [None] * (n + 1)
    depth = [None] * (n + 1)
    stack = [(1, 0)]
    depth[1] = 0
    parent[1] = 1
    max_depth = 0
    while stack:
        cur_node, cur_depth = stack.pop()
        if max_depth < cur_depth:
            max_depth = cur_depth
        for child in adj[cur_node]:
            if child != parent[cur_node]:
                parent[child] = cur_node
                depth[child] = cur_depth + 1
                stack.append((child, cur_depth + 1))

    max_power = math.floor(math.log2(max_depth))
    parent_2tothe = [[None] * (n + 1) for _ in range(max_power + 1)]
    for node in range(2, n + 1):
        parent_2tothe[0][node] = parent[node]
    for power in range(1, max_power + 1):
        for node in range(2, n + 1):
            if depth[node] >= (1 << power):
                p_half = parent_2tothe[power - 1][node]
                p_full = parent_2tothe[power][node] = parent_2tothe[power - 1][parent_2tothe[power - 1][node]]
                new_min = min(dist[(node, p_half)][0], dist[(p_half, p_full)][0])
                new_max = max(dist[(node, p_half)][1], dist[(p_half, p_full)][1])
                dist[(node, p_full)] = dist[(p_full, node)] = (new_min, new_max)

    def parent_n(n, x):
        if n == 0:
            return x
        biggest_power_under = math.floor(math.log2(n))
        next_n = n - (1 << biggest_power_under)
        next_x = parent_2tothe[biggest_power_under][x]
        p = parent_n(next_n, next_x)
        if next_n != 0:
            new_min = min(dist[(x, next_x)][0], dist[(next_x, p)][0])
            new_max = max(dist[(x, next_x)][1], dist[(next_x, p)][1])
        else:
            new_min, new_max = dist[(x, next_x)]
        dist[(x, p)] = dist[(p, x)] = (new_min, new_max)
        return p

    def find_LCA(a, b):
        if parent[a] == parent[b]:
            return parent[a]
        for power in range(1, max_power + 1):
            if parent_2tothe[power][a] == parent_2tothe[power][b]:
                p_a = parent_2tothe[power - 1][a]
                p_b = parent_2tothe[power - 1][b]
                break
        else:
            p_a = parent_2tothe[max_power][a]
            p_b = parent_2tothe[max_power][b]
        lca = find_LCA(p_a, p_b)
        new_min = min(dist[(a, p_a)][0], dist[(p_a, lca)][0], dist[(b, p_b)][0], dist[(p_b, lca)][0])
        new_max = max(dist[(a, p_a)][1], dist[(p_a, lca)][1], dist[(b, p_b)][1], dist[(p_b, lca)][1])
        dist[(a, b)] = dist[(b, a)] = (new_min, new_max)
        dist[(a, lca)] = dist[(lca, a)] = (min(dist[(a, p_a)][0], dist[(p_a, lca)][0]), max(dist[(a, p_a)][1], dist[(p_a, lca)][1]))
        dist[(b, lca)] = dist[(lca, b)] = (min(dist[(b, p_b)][0], dist[(p_b, lca)][0]), max(dist[(b, p_b)][1], dist[(p_b, lca)][1]))
        return lca

    print_buf = []
    for _ in range(int(read())):
        d, e = map(int, read().split())
        d, e = (d, e) if depth[d] > depth[e] else (e, d)
        elevated_d = parent_n(depth[d] - depth[e], d)
        new_min = math.inf
        new_max = 0
        if elevated_d != d:
            new_min = dist[(d, elevated_d)][0]
            new_max = dist[(d, elevated_d)][1]
        if elevated_d != e:
            p = find_LCA(elevated_d, e)
            new_min = min(new_min, dist[(elevated_d, p)][0], dist[(e, p)][0])
            new_max = max(new_max, dist[(elevated_d, p)][1], dist[(e, p)][1])
        print_buf.append(f'{new_min} {new_max}')
    print('\n'.join(print_buf))


solve()
