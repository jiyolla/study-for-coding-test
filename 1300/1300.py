# @profile
def solve():
    n = int(input())
    k = int(input())
    lower = 1
    upper = n ** 2
    lower_index = 1
    upper_index = n ** 2
    j = 0
    while upper > lower:
        j += 1
        print(f'[{j}] u: {upper:<15}l: {lower:<15}', end='')
        # ans = (upper + lower) // 2
        #"""
        if (upper - lower)/upper > 0.01:
            if (upper_index - k)/upper_index < 0.00001:
                print('upper close', end='')
                ans = max(upper*99999//100000, lower)
            elif (k - lower_index)/k < 0.0001:
                print('lower close', end='')
                ans = min(lower*100001//100000, upper)
            else:
                print('fast', end='')
                ans = ((upper_index-k)*lower + (k-lower_index)*upper) // (upper_index-lower_index)
        else:
            ans = (upper + lower) // 2
        #"""
        count = ans // n * n
        for i in range(ans // n + 1, n + 1):
            count += ans//i
        if count >= k:
            upper = ans
            upper_index = count
        elif count < k:
            lower = ans + 1
            lower_index = count
        print(f'ans: {ans:<15}count: {count}')

    print(upper)


solve()
