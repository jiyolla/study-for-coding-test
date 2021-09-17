n, k = list(map(int, input().split()))

coins = []
for _ in range(n):
    coins.append(int(input()))
coins.reverse()
count = 0
for v in coins:
    count += k // v
    k %= v
    if k == 0:
        break

print(count)
