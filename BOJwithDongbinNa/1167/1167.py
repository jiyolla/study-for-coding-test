import sys


def solve():
    read = sys.stdin.readline
    n = int(read())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n):
        v0, *edges = map(int, read().split())
        for i in range(0, len(edges) - 1, 2):
            adj[v0].append((edges[i], edges[i + 1]))

    # select leaf nodes, i.e. any node has only one edge
    # this is quite irrelavant of the choice of root node
    # the longest route is always between two leaf nodes.
    """
    leaves = []
    for node in range(1, n + 1):
        if len(adj[node]) == 1:
            leaves.append(node)
    """
    # Actually, maybe a single tree traversal would solve the problem
    # The traversal procedure is as follows.
    # Visit of a node
    # 1. Visit its every non leaf children
    # 2. If its children is all leaf node
    #     1. Select the two biggest edges and update tree diamter if needed
    #     2. Update current node's incoming edge by adding the biggest edge from children node
    #     3. End visit of current node.
    # 3. After visit of every non leaf children, they become leaf node with updated edges.
    # 4. procedure ends when root node's visit is complete
    # Root node does not have incoming edges, so pay a little attention to that.
    # Not sure if this work if when root node is a single edge node.
    # Just use other non single edge node.
    root = 1
    for node in range(1, n + 1):
        if len(adj[node]) != 1:
            root = node
            break

    visited = [False] * (n + 1)
    max_diameter = 0

    def dfs(node):
        nonlocal max_diameter
        visited[node] = True
        candidates = []
        for child, cost in adj[node]:
            if not visited[child]:
                if len(adj[child]) != 1:
                    cost += dfs(child)
                candidates.append(cost)
        candidates.sort()
        local_max = sum(candidates[-2:])
        if max_diameter < local_max:
            max_diameter = local_max
        return candidates[-1]

    visited[root] = True
    candidates = []
    for child, cost in adj[root]:
        if len(adj[child]) != 1:
            cost += dfs(child)
        candidates.append(cost)
    candidates.sort()
    print(max(max_diameter, sum(candidates[-2:])))


solve()
