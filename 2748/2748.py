def solve():
    n = int(input())

    pib = [1, 1] + [0] * (n - 2)
    for i in range(2, n):
        pib[i] = pib[i - 2] + pib[i - 1]
    print(pib[-1])


solve()
