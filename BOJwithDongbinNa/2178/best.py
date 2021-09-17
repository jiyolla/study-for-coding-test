from sys import stdin

@profile
def solve():
    n,m = map(int,input().split())

    maze = [[0]*(m+2)]
    for _ in range(n):
        maze.append([0]+list(map(int,list(stdin.readline().rstrip("\n"))))+[0])
    maze.append([0]*(m+2))

    que = [(1,1)]
    maze[1][1] == 0
    count = 1
    while True:
        temp = []
        for node in que:
            i,j = node
            if maze[i+1][j] != 0:
                temp.append((i+1,j))
                maze[i+1][j] = 0

            if maze[i-1][j] != 0:
                temp.append((i-1,j))
                maze[i-1][j] = 0

            if maze[i][j+1] != 0:
                temp.append((i,j+1))
                maze[i][j+1] = 0

            if maze[i][j-1] != 0:
                temp.append((i,j-1))
                maze[i][j-1] = 0


        que = temp
        count += 1
        if (n,m) in temp:
            break

    print(count)


solve()
