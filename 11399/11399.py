n = int(input())
wait_time = list(map(int, input().split()))

wait_time.sort(reverse=True)
sum = 0
for i, t in enumerate(wait_time):
    sum += (i + 1) * t
print(sum)

