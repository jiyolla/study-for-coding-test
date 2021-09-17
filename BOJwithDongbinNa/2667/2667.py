import sys


def solve():
    read = sys.stdin.readline

    n = int(read())

    building = [[] for _ in range(n)]
    marked = [[False] * n for _ in range(n)]

    for i in range(n):
        building[i] = [int(read(1)) for _ in range(n)]
        read()

    def dfs(x, y):
        marked[y][x] = True
        sub_sum = 1
        if x + 1 < n and building[y][x + 1] and not marked[y][x + 1] == 1:
            sub_sum += dfs(x + 1, y)
        if x > 0 and building[y][x - 1] and not marked[y][x - 1] == 1:
            sub_sum += dfs(x - 1, y)
        if y + 1 < n and building[y + 1][x] and not marked[y + 1][x] == 1:
            sub_sum += dfs(x, y + 1)
        if y > 0 and building[y - 1][x] and not marked[y - 1][x] == 1:
            sub_sum += dfs(x, y - 1)
        return sub_sum

    group = []
    for i in range(n):
        for j in range(n):
            if building[i][j] == 1 and not marked[i][j]:
                group.append(dfs(j, i))
    print(len(group))
    group.sort()
    for i in group:
        print(i)


if __name__ == '__main__':
    solve()
