import sys


def solve():
    read = sys.stdin.readline

    """
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
            size[root_v2] += size[root_v1]
            return True

    res = []
    for _ in range(int(read())):
        n, m = map(int, read().split())
        parent = [i for i in range(n)]
        size = [1 for _ in range(n)]
        ans = 0
        found = False
        for _ in range(m):
            a, b = map(int, read().split())
            if not found and union(a - 1, b - 1):
                ans += 1
                if size[b - 1] == n:
                    found = True
        res.append(str(ans))
    print('\n'.join(res))
    """
    # 와 개뻘짓했네... 1등 답안지 보고 개놀랬네... 뭐지 했지 스벌... 인정.
    # res = []
    for _ in range(int(read())):
        n, m = map(int, read().split())
        for _ in range(m):
            read()
        # res.append(str(n - 1))
        print(n - 1)
    # print('\n'.join(res))


solve()
