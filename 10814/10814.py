import sys
read = sys.stdin.readline
enrolled = [(lambda x: [int(x[0]), x[1]])(read().split()) for _ in range(int(read()))]
print('\n'.join(f'{i[0]} {i[1]}' for i in sorted(enrolled, key=lambda x: x[0])))
