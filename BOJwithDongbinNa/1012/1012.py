import sys
read = sys.stdin.readline
n_test = int(read())

for _ in range(n_test):
    m, n, k = map(int, read().split())
    field = [([0] * (m+2)) for _ in range(n + 2)]
    for _ in range(k):
        x, y = map(int, read().split())
        field[y + 1][x + 1] = 1

    stack = []
    n_worm = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if field[i][j] == 1:
                n_worm += 1
                stack.append((j, i))
                while stack:
                    x, y = stack.pop()
                    if field[y][x + 1] == 1:
                        field[y][x + 1] = 0
                        stack.append((x + 1, y))
                    if field[y][x - 1] == 1:
                        field[y][x - 1] = 0
                        stack.append((x - 1, y))
                    if field[y + 1][x] == 1:
                        field[y + 1][x] = 0
                        stack.append((x, y + 1))
                    if field[y - 1][x] == 1:
                        field[y - 1][x] = 0
                        stack.append((x, y - 1))
    print(n_worm)
