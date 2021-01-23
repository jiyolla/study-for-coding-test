import sys
import math


def solve():
    read = sys.stdin.readline
    n = int(read())
    m = int(read())
    graph = [{} for _ in range(n + 1)]
    for _ in range(m):
        v1, v2, d = map(int, read().split())
        if v2 in v1:
            graph[v1][v2] = min(graph[v1]