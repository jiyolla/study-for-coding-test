import sys
n = int(sys.stdin.readline())

meetings = []
for _ in range(n):
    meetings.append(list(map(int, sys.stdin.readline().rstrip('\n').split())))
meetings.sort(key=lambda x: (x[1], x[0]))

available = 0
count = 0
for i in meetings:
    if i[0] >= available:
        available = i[1]
        count += 1
print(count)
