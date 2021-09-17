def solve():
    mem = {}
    def w(a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            return 1
        if a > 20 or b > 20 or c > 20:
            mem[(a, b, c)] = w(20, 20, 20)
            return mem[(a, b, c)]
        if (a, b, c) in mem:
            return mem[(a, b, c)]
        if a < b and b < c:
            mem[(a, b, c)] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
            return mem[(a, b, c)]
        mem[(a, b, c)] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        return mem[(a, b, c)]
    while True:
        a, b, c = map(int, input().split())
        if a == -1 and b == -1 and c == -1:
            break
        else:
            print(f'w({a}, {b}, {c}) = {w(a, b, c)}')


solve()
