import sys
import math
# from collections import deque
# import heapq


def solve():
    read = sys.stdin.readline
    n, m = map(int, read().split())
    graph = [{} for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, read().split())
        if b in graph[a]:
            graph[a][b] = min(graph[a][b], c)
        else:
            graph[a][b] = c

    """
    # 마이너스 사이클 발생할 때 각별한 주의가 필요하다.
    # 그 사이클에 있는 임의의 노드에서 출발하여 도달할 수 있는 모든 노드들은 다 -1 시간에 안에 도달 가능하다.
    # 무한한 마이너스를 축적하고 출발해서 도착해서 무한히 과거로 돌아가는 것이다.
    # 마이너스 사이클 감지를 어떻게 할 것인가? 1차적으로 visited를 만들어서, 이미 visit된 것이 다시 갱신된다면 그것은 마이너스 사이클이라는 뜻인데
    # 마이너스 사이클에 존재하는 모든 노드들을 어떻게 식별하는가?
    # 굳이 식별해야 되나? 어차피 그 하나의 노드만 있어도 그 노드에서 출발해서 도착할 수 있는 점들은 다 -1로 설정하면 되는 거 아닌가?
    # 그 노드에서 출발해서는 도착 못하지만 사이클에 있는 다른 노드에서 출발해서 도착할 수 있는 노드는... 없다! 있으면 같은 사이클에 있는 게 아니지.
    # 즉, 마이너스 사이클을 감지하면 그 노드에서 도달가능한 모든 곳을 dfs로 검색해서 다 -math.inf로 설정한다.
    # 아니, 문제를 다시 읽어보니까 그냥 한 개의 도시라도 마이너스 무한대로 도착할 수 있으면 -1만 출력하는 거 같네.
    def dijkstra(start, *end):
        is_time_machine = False
        h = []
        heapq.heappush(h, (0, start))
        dist = [math.inf for _ in range(n + 1)]
        dist[start] = 0
        visited = [False for _ in range(n + 1)]
        while h:
            d1, v1 = heapq.heappop(h)
            print(d1, v1)
            # dist[v1] < d1은 문제가 있다. 순간이동이나 시간여행으로 0의 시간으로 다시 제자리로 올 수 있는 가능성이 커서
            # 그러면 엄격히 말해서는 무한히 과거로 돌아가지 못하는데도 이미 visit한 것을 방문하기 때문에 tima machine이 아닌데 time machine판정을 받게 된다.
            # dist[v1] <= d1이기만 해도 continue하는 게 맞다. 근데 이렇게 하면 젤 처음에 dist[start]가 걸려 버린다...
            # 이새끼를 어떻게 깔끔하게 예외처리하지...?
            # dist[start]도 마찬가지로 나중에 0의 시간으로 다시 제자리로 돌아왈 수 있기 때문에 단순히 v1==start면 봐준다로는 안 된다...
            # 우리가 봐주고 싶은 상황은 정확히, 오케이.
            # visited[start]가 false이면 그냥 패스하면 되겄네! 해결!
            # 아니 문제가 있다. 그리고 애초에 push가 같으면 안 되니까 위에 걱정했던 문제 발생 ㄴㄴ.
            # 그것보다 사이클 판정에 지금 문제가 있음.
            # 단순히 이미 방문한 노드를 더 짧은 거리로 방문했다해서 사이클이 생기는 게 아님.
            # 그 노드에서 출발하는 에지가 하나도 없다면 무한과거 발생 안 함.
            # 그리고 그 노드에서 1차적으로 연장만 해나가도 무한과거 X.
            # 말 그대로 사이클이 생성되어야 함. 그 사이클에 그리고 자기로 들어온 노드가 있어야 됨.
            # 그냥 지 혼자서 사이클 하나 만들어도 의미 없음.
            # 방문 기록을 
            # 다 필요없고 벨만포드 방법을 쓰면 되군...
            if dist[v1] < d1: # or math.isinf(-dist[v1]):
                continue
            if visited[v1]:
                is_time_machine = True
                breakf
                ""
                stack = [v1]
                dfs_visited = [False for _ in range(n + 1)]
                while stack:
                    dfs_v = stack.pop()
                    if dfs_visited[dfs_v]:
                        continue
                    dfs_visited[dfs_v] = True
                    dist[dfs_v] = -math.inf
                    stack += list(graph[dfs_v])
                ""
            visited[v1] = True
            for v2, d2 in graph[v1].items():
                if dist[v2] > d1 + d2:
                    dist[v2] = d1 + d2
                    heapq.heappush(h, (dist[v2], v2))
        return tuple([is_time_machine] + [dist[i] for i in end])
    is_time_machine, *res = dijkstra(1, *[i for i in range(2, n + 1)])
    if is_time_machine:
        print(-1)
    else:
        print('\n'.join(['-1' if math.isinf(i) else str(i) for i in res]))
    """
    # Bellman Ford 방법
    dist = [math.inf for _ in range(n + 1)]
    dist[1] = 0
    for i in range(n - 1):
        finished = True
        for v1 in range(1, n + 1):
            for v2, d in graph[v1].items():
                if dist[v2] > dist[v1] + d:
                    dist[v2] = dist[v1] + d
                    finished = False
        if finished:
            break
    negative_cycle = False
    if i == n - 2:
        for v1 in range(1, n + 1):
            for v2, d in graph[v1].items():
                if dist[v2] > dist[v1] + d:
                    negative_cycle = True
                    break
    if negative_cycle:
        print(-1)
    else:
        print('\n'.join(['-1' if math.isinf(i) else str(i) for i in dist[2:]]))
    """
    # Bellman Ford 방법 w/ queue
    dist = [math.inf for _ in range(n + 1)]
    dist[1] = 0
    visits = [0 for _ in range(n + 1)]
    negative_cycle = False
    q = deque()
    q.append(1)
    while q:
        v1 = q.popleft()
        visits[v1] += 1
        if visits[v1] >= n:
            negative_cycle = True
            break
        for v2, d in graph[v1].items():
            if dist[v2] > dist[v1] + d:
                dist[v2] = dist[v1] + d
                if v2 not in q:
                    q.append(v2)
    if negative_cycle:
        print(-1)
    else:
        print('\n'.join(['-1' if math.isinf(i) else str(i) for i in dist[2:]]))
    """


solve()
