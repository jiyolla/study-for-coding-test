def solve():
    s1 = input()
    s2 = input()
    ans = 0
    """
    for c1 in s1:
        for i, c2 in enumerate(s2):
            if c1 == c2:
                # print(f'c1: {c1}, i + 1: {i + 1}')
                if i + 1 > table[ans]:
                    ans += 1
                    table[ans] = i + 1
                    break
                else:
                    for j in range(1, ans + 1):
                        if table[j] >= i + 1:
                            table[j] = i + 1
                            break
    print(ans)
    """
    # 이제 좀 끝내자 후...거진 2주간 미뤘다.
    # 문제를 내 말로 풀어본다.
    # 두 개의 수열이 주어진다. 동시에 이 두 수열의 부분수열이 될 수 있는 수열 중 가장 킨 수열을 찾는다.
    # 이 수열을 어떻게 확인할까?
    # 일단 이 수열은 두 수열의 부분수열이므로, 당연히 두 수열에 모두 포함된다.
    # 더 짤은 수열을 골라서, 다른 수열에 매칭해볼까? 어떤식으로?
    # 여기서 좀 갑작스러운 느낌이 없지 않아 있지만 dp개념 넣어보자.
    # LIS할 때처럼, dp[i]를 길이가 i인 부분 수열 중 다른 수열에서의 마지막 매칭 index가 가장 작은 걸로 할까?
    # 그리고 짧은 수열을 순회하면서 전체에 대한. 그니까 정확히 말하자면
    # dp[i][j]는 짧은 수열의 i번쨰 원소까지 순회했을 때, 길이가 j인 부분 수열 중 긴 수열 마지막 매칭 원소의 최솟값이다.
    # 그러면, dp[i][j]는 dp[i-1]을 순회하면서, 모든 길이의 마지막 원소에 위치에서 시작해서 짧은 수열 i번째 원소를 찾고 입력하면 된다.
    # 시발. 해결된 거 같다. 진짜 이렇게 글로 쓰는 것만으로 해도 생각이 정돈되고, 문제가 해결 된다...물론 짜봐야 알겠지만...
    # 구현!!!!! 근데 dp[i]는 dp[i-1]에만 의존하므로, 왼도우 적용하겠음.
    # s1이 더 짧은 수열이 됨
    s1, s2 = (s1, s2) if len(s1) < len(s2) else (s2, s1)
    dp_pre = []
    s = 0
    for i in range(len(s1)):
        s = i + 1
        if s1[i] in s2:
            dp_pre = [s2.index(s1[i])]
            break
    for c in s1[s:]:
        dp_cur = [min(dp_pre[0], s2.index(c) if c in s2 else 1000)]
        for i in range(1, len(dp_pre)):
            dp_cur.append(min(dp_pre[i], s2[dp_pre[i - 1] + 1:].index(c) + dp_pre[i - 1] + 1 if c in s2[dp_pre[i - 1] + 1:] else 1000))
        if c in s2[dp_pre[-1] + 1:]:
            dp_cur.append(s2[dp_pre[-1] + 1:].index(c) + dp_pre[-1] + 1)
        dp_pre = dp_cur
    print(len(dp_pre))


solve()
