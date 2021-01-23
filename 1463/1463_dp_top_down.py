def solve():
    n = int(input())
    mem = {0: n, 1: 0}

    def find(n):
        if n in mem:
            return mem[n]
        mem[n] = min(find(n // 2) + n % 2, find(n // 3) + n % 3) + 1
        return mem[n]
    print(find(n))


solve()
