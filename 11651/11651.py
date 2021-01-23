import sys
read = sys.stdin.readline

n = int(read())
v = []
for i in range(n):
    v.append(list(map(int, read().split())))

v.sort(key=lambda x: (x[1], x[0]))
for i in range(n):
    print(f'{v[i][0]} {v[i][1]}')
