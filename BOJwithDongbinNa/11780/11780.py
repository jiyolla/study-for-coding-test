import sys
import math


def solve():
    read = sys.stdin.readline
    n = int(read())
    m = int(read())
    dist = [[math.inf] * (n + 1) for _ in range(n + 1)]
    # traceback[i][j] = dist[i][j]를 낳는 j전의 노드. 그 노드가 i이면 루트 길이가 1인 것.
    traceback = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, read().split())
        dist[a][b] = c if dist[a][b] > c else dist[a][b]
        traceback[a][b] = [a]
    for p in range(1, n + 1):
        for src in range(1, n + 1):
            if p == src:
                continue
            for dst in range(1, n + 1):
                if src == dst or dst == p:
                    continue
                if dist[src][dst] > dist[src][p] + dist[p][dst]:
                    dist[src][dst] = dist[src][p] + dist[p][dst]
                    traceback[src][dst] = traceback[src][p] + traceback[p][dst]
    print('\n'.join([' '.join(['0' if math.isinf(j) else str(j) for j in i[1:]]) for i in dist[1:]]))
    print_buf = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if math.isinf(dist[i][j]):
                print_buf.append('0')
                continue
            print_buf.append(f'{len(traceback[i][j]) + 1} {" ".join([str(k) for k in traceback[i][j]])} {j}')
    print('\n'.join(print_buf))


solve()
