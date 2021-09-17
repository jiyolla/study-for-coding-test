import sys
read = sys.stdin.readline
n = [list(map(int, read().split())) for i in range(int(read()))]
n.sort(key=lambda x: (x[0], x[1]))
print('\n'.join(f'{i[0]} {i[1]}' for i in n))
