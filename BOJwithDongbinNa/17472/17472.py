def solve():
    n, m = map(int, input().split())
    parent = [i for i in range(n*m)]

    def num(i, j):
        return i*m + j

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
            parent[root_v2] = root_v1
            return True

    bitmap = []
    for i in range(n):
        line = input().split()
        bitmap.append(line)
        for j in range(m):
            if line[j] == '0':
                continue
            if i != 0 and bitmap[i - 1][j] == '1':
                union(num(i - 1, j), num(i, j))
            if j > 0 and line[j - 1] == '1':
                union(num(i, j - 1), num(i, j))

    """
    # island[i] = [left, right, top, bot]
    islands = {}
    island_list_access = []
    for i in range(n):
        for j in range(m):
            if bitmap[i][j] == '1':
                island_id = parent[num(i, j)]
                if island_id not in islands:
                    islands[island_id] = [j, j, i, i]
                    island_list_access += island_id
                else:
                    if islands[island_id][0] > j:
                        islands[island_id][0] = j
                    if islands[island_id][1] < j:
                        islands[island_id][1] = j
                    if islands[island_id][2] > i:
                        islands[island_id][2] = i
                    if islands[island_id][3] < i:
                        islands[island_id][3] = i
    # 자여기까지 islands들을 얻어냈고, 이제 island들끼리 연결 가능한 브리짓들을 모두 추가해야 한다.
    # 일단 다리가 세로나 가로 밖에 되지 않고, 섬과 연결할 때도 똑같이 세로나 가로를 유지하면서 연결되어야 되기 때문에
    # 두 섬이 연결 가능하려면, 세로나 가로로 겹치는 땅이 있어야 한다.
    # 겹치는 땅이 있으면 바로 그 방향에 대해서 가장 짧은 다리를 구한다.
    # 예를 들어서 i1의 가장 오른쪽이 i2의 가장 왼쪽보다 크다면, 겹치는 게 있다는 것인데
    # i2가 i1을 상하로 포위할 가능성도 있기 때문에,  i1의 가장 오른쪽 노드에서 위아래로 동시에 탐색한다. 반드시 땅과 만나게 되어 있다.
    # 근데 가는 도중에 다른 섬이 먼저 연결될 수도 있는데, 그럴 때는 해당 경로는 불가능한 걸로.
    bridges = []
    for i1 in range(len(islands)):
        for i2 in range(i1 + 1, len(islands)):
            i1_id = island_list_access[i1]
            i2_id = island_list_access[i2]
            if islands[i1_id][0] > islands[i2_id][1]:
    """
    # 아 너무 복잡해. 그냥 단순하게 모든 점에서 위아래 방향 탐색하는 것이 더 단순하고 최대 100개점 밖에 없으니 더 빠르기도 하겠다.
    # 현재 parent가 다 제대로 마킹된 상황. bitmap으로 자기가 땅인 것을 확인하면, 자기의 parent를 기억하고 위아래 방향으로 탐색해서
    # 기억해던 parent가 나오거나, 경계에 부딫히거나, bitmap이 '0'인 바다를 만나건, 땅인데 parent가 다른 애를 만나는 4가지 경우 밖에 없다.
    edges = []
    for i in range(n):
        for j in range(m):
            if bitmap[i][j] == '0':
                continue
            # search top
            for i2 in range(i - 1, -1, -1):
                if bitmap[i2][j] == '1':
                    if find(num(i2, j)) == find(num(i, j)):
                        break
                    else:
                        if i - i2 > 2:
                            edges.append((i - i2 - 1, num(i, j), num(i2, j)))
                        break
            # search bot
            for i2 in range(i + 1, n):
                if bitmap[i2][j] == '1':
                    if find(num(i2, j)) == find(num(i, j)):
                        break
                    else:
                        if i2 - i > 2:
                            edges.append((i2 - i - 1, num(i, j), num(i2, j)))
                        break
            # search left
            for j2 in range(j - 1, -1, -1):
                if bitmap[i][j2] == '1':
                    if find(num(i, j2)) == find(num(i, j)):
                        break
                    else:
                        if j - j2 > 2:
                            edges.append((j - j2 - 1, num(i, j), num(i, j2)))
                        break
            # search right
            for j2 in range(j + 1, m):
                if bitmap[i][j2] == '1':
                    if find(num(i, j2)) == find(num(i, j)):
                        break
                    else:
                        if j2 - j > 2:
                            edges.append((j2 - j - 1, num(i, j), num(i, j2)))
                        break
    # 이러면 이제 edges에 건설 가능한 모든 다리가 포함됨.
    # (다리 길이, 섬1의 root, 섬2의 root) 이렇게 말이야.
    # 여기서 드디어 크루스칼 돌리면 되는데
    # 모든 섬들이 연결된 것을 확인하기 위해서 총 몇 개의 섬이 있는지 확인하기는 해야 됨...
    # 아니면 굳이 조기 판정해서 끝내지 말고, 모든 다리 다 돌려도 나쁘지 않은 듯. 어차피 몇 개 없음.
    # 섬 개수 확인하는 게 더 올래 걸릳 수도.
    # 아니 근데 전부 연결되었는지 확인하려면... 스벌..그냥 총 섬 개수 확인하자.
    islands = {}
    for i in range(n):
        for j in range(m):
            if bitmap[i][j] == '1':
                island_id = parent[num(i, j)]
                if island_id not in islands:
                    islands[island_id] = ''
    edges.sort()
    ans = 0
    count = 1
    for d, i1, i2 in edges:
        if union(i1, i2):
            ans += d
            count += 1
            if count == len(islands):
                break
    print(ans if count == len(islands) else -1)


solve()
