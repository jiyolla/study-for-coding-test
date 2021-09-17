def solve():
    n = int(input())
    table = [0] * (n + 1)
    table[1] = 0
    for i in range(2, n + 1):
        table[i] = min(table[i - 1], table[i // 3] if i % 3 == 0 else n, table[i // 2] if i % 2 == 0 else n) + 1
    print(table[n])


solve()
