def solve():
    input()
    table = set(input().split())
    input()
    print(' '.join(['1' if i in table else '0' for i in input().split()]))


solve()
