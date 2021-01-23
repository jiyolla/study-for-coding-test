def solve():
    t = int(input())
    n = [int(input()) for _ in range(t)]
    fib = [[1, 0], [0, 1]] + [[0, 0] for _ in range(max(n) - 1)]
    for i in range(2, max(n) + 1):
        fib[i][0], fib[i][1] = fib[i - 2][0] + fib[i - 1][0], fib[i - 2][1] + fib[i - 1][1]
    print('\n'.join(f'{fib[i][0]} {fib[i][1]}' for i in n))


solve()
