import sys


def solve():
    read = sys.stdin.readline
    n = int(read())
    xs, ys, zs = [], [], []
    for i in range(n):
        x, y, z = map(int, read().split())
        xs.append((x, i))
        ys.append((y, i))
        zs.append((z, i))
    # 아니 점이 너무 많은데... ? 100,000개? 그럼 에지는 10,000,000,000...100억개..
    # 확실한 건 크루스칼로는 안 된다...
    # 프림즈 뭐시기가 답인가? 찾아보지.
    # 이 새끼도 최소 E의 linear time인데...흠...
    # 흠 실제로는 생각보다 빨리 끝날 수도 있다. 근데 적어도 E전체를 지금 저장 못하는 상황.
    # 프림즈는 E전체가 필요하나?
    # 필요없다. 일단 구현해본다.
    # 프림 알고리즘은 dist[i]를 유지하는 게 포인트인데
    # 가장 작은 노드를 추가하고, 나머지 노드들에서 이 새롭게 추가된 노드와의 거리를 다 한번 비교하면서 dist를 업데이트 해야 된다.
    """
    dist = []
    selected = [False for _ in range(n)]
    for _ in range(n - 1):
        d, v = heapq.heappop(dist)
        selected[v] = True
        for d in :
            new_d = min(abs(points[v][0] - points)
            if d < mi
        heapq.heapify(dist)
    """                    
    # 흠 이건 어떤가?
    # 모든 노드들의 x, y, z를 분리해서 오름차순 정렬하는 것이다.
    # 차이값이 중요한 거지 값 자체가 중요한 게 아니다..
    xs.sort()
    ys.sort()
    zs.sort()
    edges = [(xs[i + 1][0] - x, j, xs[i + 1][1]) for i, (x, j) in enumerate(xs[:-1])]
    edges += [(ys[i + 1][0] - y, j, ys[i + 1][1]) for i, (y, j) in enumerate(ys[:-1])]
    edges += [(zs[i + 1][0] - z, j, zs[i + 1][1]) for i, (z, j) in enumerate(zs[:-1])]
    edges.sort()

    def find(v):
        while v != parent[v]:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    def union(v1, v2):
        root_v1 = find(v1)
        root_v2 = find(v2)
        if root_v1 == root_v2:
            return False
        else:
            parent[root_v1] = root_v2
            return True

    parent = [i for i in range(n)]
    size = 1
    ans = 0
    for d, v1, v2 in edges:
        if union(v1, v2):
            size += 1
            ans += d
            if size == n:
                break
    print(ans)


solve()
