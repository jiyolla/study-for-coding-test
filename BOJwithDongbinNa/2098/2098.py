import math


def solve():
    n = int(input())
    w = []
    for _ in range(n):
        w.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(n):
            if w[i][j] == 0 and i != j:
                w[i][j] = math.inf

    # mem[state][last_city] = best_cost
    # state = 0 ~ (n - 1) bits of 1. State exclude 0th city, as it's visited on boot.
    # city number = 0 ~ n - 1, including 0th city(the starting city).
    mem = [[math.inf] * n for _ in range(1 << (n - 1))]

    # mem[0] should only be visited on its first element,
    # as mem[0][i] would mean to start the travel from city i,
    # and we only reckon travels starting from 0th city.
    # But, simply setting others to inf would simplify the codes.
    mem[0] = [0] + [math.inf] * (n - 1)

    # Compute mem for states from 1 to those with (n - 1 - 1)bits of 1 and a 0.
    # States with (n - 1 - 1)bits of 1 and a 0 only have one decision to make,
    # but their decisioning policy need some special care,
    # which is the cost of going back to the starting city.
    # So, they are not processed here.
    for state in range(1, (1 << (n - 1)) - 1):
        target_city_bit = 1
        target_city = 1
        while target_city_bit <= state:
            if state & target_city_bit:
                for last_city, cost in enumerate(mem[state & (~target_city_bit)]):
                    new_cost = cost + w[last_city][target_city]
                    if mem[state][target_city] > new_cost:
                        mem[state][target_city] = new_cost
            target_city_bit <<= 1
            target_city += 1

    # For states with last decision to make
    ans = math.inf
    for i in range(1, n):
        for last_city, cost in enumerate(mem[((1 << (n - 1)) - 1) & (~(1 << (i - 1)))]):
            new_cost = cost + w[last_city][i] + w[i][0]
            if ans > new_cost:
                ans = new_cost

    print(ans)


solve()
