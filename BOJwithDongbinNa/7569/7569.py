from sys import stdin
from collections import deque

@profile
def solve():
    read = stdin.readline

    m, n, h = list(map(int, read().split()))

    new = deque()
    mature = [[[0] * m for j in range(n)] for k in range(h)]

    for k in range(h):
        for j in range(n):
            mature[k][j] = list(map(int, read().split()))
            for i in range(m):
                if mature[k][j][i] == 1:
                    new.append((i, j, k))

    d = -1

    while new:
        for _ in range(len(new)):
            t = new.popleft()
            x, y, z = t
            if x + 1 < m and mature[z][y][x + 1] == 0:
                mature[z][y][x + 1] = 1
                new.append((x + 1, y, z))
            if x > 0 and mature[z][y][x - 1] == 0:
                mature[z][y][x - 1] = 1
                new.append((x - 1, y, z))
            if y + 1 < n and mature[z][y + 1][x] == 0:
                mature[z][y + 1][x] = 1
                new.append((x, y + 1, z))
            if y > 0 and mature[z][y - 1][x] == 0:
                mature[z][y - 1][x] = 1
                new.append((x, y - 1, z))
            if z + 1 < h and mature[z + 1][y][x] == 0:
                mature[z + 1][y][x] = 1
                new.append((x, y, z + 1))
            if z > 0 and mature[z - 1][y][x] == 0:
                mature[z - 1][y][x] = 1
                new.append((x, y, z - 1))
        d += 1

    for z in range(h):
        for y in range(n):
            if 0 in mature[z][y]:
                d = -1
                break
    print(d)


if __name__ == '__main__':
    solve()

