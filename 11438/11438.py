import sys
import math

@profile
def solve():
    read = sys.stdin.readline
    n = int(read())

    # 자, 트리가 주어지는데, 부모 관계는 불명
    # 단순하게 parent리스트만 만들고 싶은데, 그러려면 좀 손을 봐야됨
    # parent만들었다고 치자.
    # 10만개의 쿼리가 들어옴. 한 쿼리가 대충 log시간 안에 해결해야 돼
    # parent_2tothe[][]만들어
    # parent_2tothe[i][j]는 j의 2^i번째 parent, i = 0~필요한만큼
    # 그럼 쿼리가 들어올 때, 먼저 한놈 빠르게 끌어올려, 음 parent에 depth정보도 넣어야 됨
    # 끌어오릴는데 최대 log n시간, 그담에 같은 레벨의 두 노드에 대해서 parent달라지는 시작을 찾아냄
    # 이것도 log n 시간 안에 가능, 그러면 log n시간 안에 1개쿼리 처리 가능하네. 구현.

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, read().split())
        adj[a].append(b)
        adj[b].append(a)

    parent = [None] * (n + 1)
    depth = [None] * (n + 1)
    stack = [(1, 0)]
    parent[1] = 1
    depth[1] = 0
    max_depth = 0
    while stack:
        cur_node, cur_depth = stack.pop()
        if cur_depth > max_depth:
            max_depth = cur_depth
        for child in adj[cur_node]:
            if child != parent[cur_node]:
                parent[child] = cur_node
                depth[child] = cur_depth + 1
                stack.append((child, cur_depth + 1))
    max_power = math.floor(math.log2(max_depth))
    parent_2tothe = [[None] * (n + 1) for _ in range(max_power + 1)]
    for node in range(1, n + 1):
        parent_2tothe[0][node] = parent[node]
    for power in range(1, max_power + 1):
        min_depth_required = (1 << power)
        for node in range(2, n + 1):
            if depth[node] >= min_depth_required:
                parent_2tothe[power][node] = parent_2tothe[power - 1][parent_2tothe[power - 1][node]]

    def parent_n(n, x):
        if n == 0:
            return x
        biggest_power_under = math.floor(math.log2(n))
        next_n = n - (1 << biggest_power_under)
        return parent_2tothe[biggest_power_under][parent_n(next_n, x)]

    # a, b are expected to be on the same depth
    def find_LCA(a, b):
        if parent[a] == parent[b]:
            return parent[a]
        for power in range(1, max_power + 1):
            if parent_2tothe[power][a] == parent_2tothe[power][b]:
                return find_LCA(parent_2tothe[power - 1][a], parent_2tothe[power - 1][b])
        else:
            return find_LCA(parent_2tothe[max_power][a], parent_2tothe[max_power][b])

    print_buf = []
    for _ in range(int(read())):
        a, b = map(int, read().split())
        a, b = (a, b) if depth[a] > depth[b] else (b, a)
        a = parent_n(depth[a] - depth[b], a)
        if a == b:
            print_buf.append(f'{a}')
        else:
            print_buf.append(f'{find_LCA(a, b)}')
    print('\n'.join(print_buf))


solve()
