def solve():
    n = int(input())
    seq = list(map(int, input().split()))

    stack = [seq[-1]]
    res = [-1]
    for i in seq[-2::-1]:
        for _ in range(len(stack)):
            t = stack.pop(-1)
            if i < t:
                stack.append(t)
                res.append(t)
                stack.append(i)
                break
        if stack == []:
            res.append(-1)
            stack = [i]
        """
        temp = stack[::-1]
        found = False
        for j, t in enumerate(temp):
            if i < t:
                res.append(t)
                stack = stack[:len(stack) - j]
                stack.append(i)
                found = True
                break
        if not found:
            res.append(-1)
            stack = [i]
        """
    print(' '.join([str(i) for i in res[::-1]]))


solve()
