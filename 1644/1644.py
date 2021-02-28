import math


def solve():
    n = int(input())

    if n == 1:
        print('0')
        return

    probably_prime = [True for i in range(n + 1)]
    sqrt = int(math.sqrt(n))
    for i in range(2, sqrt + 1):
        if probably_prime[i]:
            for j in range(i * 2, n + 1, i):
                probably_prime[j] = False
    prime_nums = [i for i in range(2, n + 1) if probably_prime[i]]

    r = 0
    acc = prime_nums[0]
    ans = 0
    for l in range(len(prime_nums)):
        if acc > n: pass
        elif acc == n:
            ans += 1
        else:
            for nr in range(r + 1, len(prime_nums)):
                acc += prime_nums[nr]
                if acc > n:
                    r = nr
                    break
                elif acc == n:
                    r = nr
                    ans += 1
                    break
            else:
                break
        acc -= prime_nums[l]
    print(ans)


solve()
