def solve():
    n = int(input())
    f = [1, 2] + [0] * (n - 2)
    for i in range(2, n):
        f[i] = (f[i - 2] + f[i - 1]) % 15746
    print(f[n - 1])

solve()
