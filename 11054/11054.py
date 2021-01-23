import bisect


def solve():
    n = int(input())
    seq = list(map(int, input().split()))

    # up[i]는 길이가 i인 모든 부분증가수열의 마지막 원소의 최솟값이다.
    # down[i]는 길이가 i인 모든 부분감소수열의 마지막 원소의 최댓값이다.
    # bitonic[i]는 길이가 i인 모든 부분바이토닉수열의 마지막 원소의 최댓값이다. 여기서 바이토닉수열은 더욱 엄격한 바이토닉수열로 반드시 up+down으로 이루어짐.
    # bitonic이 좀 문제가 있다.
    # 단순히 엄격한 바이토닉 수열로 치부하기에는 새로운 원소의 첨가 작업할 때 문제가 발생한다.
    # 단조증가감사 수열과는 달리 bitonic은 i가 증감하에 따라 단조적인 증감을 보이지 않기 때문에 bisect을 이용하여 삽입할 수 없다.
    # 그렇다면 그냥 전수조사해서 업데이트 해버려? 오케이
    # 문제가 있다. 업데이트를 정확히 어떻게 하지? 뒤에서 시작해서 처음으로 자기보다 큰 수를 바꿔? 불가능.
    # 그리고 지금 down을 애초에 쓰지도 않음. 총체적인 난국이다.
    # 설계를 다시 해보자.
    # up은 지금 문제 없는 거 같다.
    # 여기서 무식하게 수열을 하나씩 읽으면서 거꾸로
    # 아, 이게 생각보다 굉장히 효율적일 수도?
    # 아니다. n^3시간이다.
    # 그래도 한번 해봐?
    # 아니다. 불가능.
    # dp[i][j]를 i번째 원소까지 길이가 j인 부분증가수열의 마지막 원소의 최솟값이라고 하자.
    # seq에 대해서 한번, seq[::-1]에 대해서 한번 dp를 구한다 해보자. dp를 구하는 데는 n logn걸린다.
    # 이 두 dp가 있으면 바이토닉을 구할 수 있는가?
    # O(n)시간에 구할 수 있는데 살짝 문제가 있다.
    # 1 2 4 5 4 2 1이 있다 쳐보자. 각각 양쪽에서 dp를 구하면 5는 버려질 것이다. 그러면 양쪽에서 둘 다 1 2 4가 뜬다.
    # 마지막 값이 같으므로 단순하게 dp로 해결 안 되는데 이때 탐색을 해야 한다. 어느쪽으로 탐색하는가? j를 낮추는 방향이 쉬울 거다.
    # 하지만 이 경우에 j를 낮추면 최댓값을 놓치는 것이다. 오히려 dp에 없는 5를 가져와야 해결된다.
    # 어떻게 5가 탐색되게 할 수 있을까?
    # seq에 대한 dp[i][j1]와 seq[::-1]에 대한 dp[n - 1 - i][j2]가 같을 때(이 때, j1과j2는 각각 dp[i] 및 dp[n - 1 -i]의 최댓값),
    # 음...다른 접근법.
    # 어차피 O(n)시간 들여서 dp테이블 다 돌거, 그냥 각 원소를 중앙 원소라고 가정하고 한번 돌면 안 되나?
    # 그렇되면 중간값 같을 때 발생하는 문제는 해결되나?
    # 1 2 4 3 3 4 2
    # 문제 없나? 답은 1 2 4 3 2 혹은 1 2 3 4 2. 이게 검색되나?
    # 중간값을 4나 3으로 할 때. 즉 1 2, 4, 3 3 4 2에서 1 2 4, 3, 3 4 2까지에서 답이 나올 수 있는데
    # 문제없는 듯 하다. 애초에 중복값이 있다는 것은 둘 다 중앙에 한번은 올거라는 뜻이아럿.. 흠 잘 모르겠는데 쨌든 문제 없는 것 같다
    """
    up = [0] * n
    down = [0] * n
    bitonic = [0] * n
    u_last = 0
    d_last = 0
    b_last = 0
    up[0], down[0], bitonic[0] = seq[0], seq[0], seq[0]
    for i in seq[1:]:
        # 부분증가수열 업데이트
        if i > up[u_last]:
            u_last += 1
            up[u_last] = i
        elif i < up[u_last]:
            # 부분바이토닉수열 업데이트
            if u_last >= b_last:
                b_last = u_last + 1
                bitonic[b_last] = i
            # 부분증가수열 업데이트
            b_left = bisect.bisect_left(up, i, hi=u_last)
            b_right = bisect.bisect_right(up, i, hi=u_last)
            if b_left == b_right:
                up[b_right] = i
        # 부분감소수열 업데이트
        if i < down[d_last]:
            d_last += 1
            down[d_last] = i
        else:
            b_left = bisect.bisect_left(down[::-1], i, hi=u_last)
            b_right = bisect.bisect_right(down[::-1], i, hi=u_last)
            if b_left == b_right:
                down[d_last + 1 - b_right] = i
        # 부분바이토닉수열 업데이트
        if i < bitonic[b_last]:
            b_last += 1
            bitonic[b_last] = i
        else:
            for j, b in enumerate(bitonic):
                if b > i and :
                    
        print(f'{i}')
        print(f'seq:     {seq}')
        print(f'up:      {up}')
        print(f'down:    {down}')
        print(f'bitonic: {bitonic}')
        print()
    print(max(u_last, d_last, b_last) + 1)
    """
    dp1 = [[seq[0]]]
    dp2 = [[seq[-1]]]
    for i in range(1, n):
        # dp1 업데이트
        temp = dp1[-1][:]
        if seq[i] > temp[-1]:
            temp.append(seq[i])
        elif seq[i] < temp[-1]:
            b_left = bisect.bisect_left(temp, seq[i])
            b_right = bisect.bisect_right(temp, seq[i])
            if b_left == b_right:
                temp[b_right] = seq[i]
        dp1.append(temp)
        # dp2 업데이트
        temp = dp2[-1][:]
        if seq[-1 - i] > temp[-1]:
            temp.append(seq[-1 - i])
        elif seq[-1 - i] < temp[-1]:
            b_left = bisect.bisect_left(temp, seq[-1 - i])
            b_right = bisect.bisect_right(temp, seq[-1 - i])
            if b_left == b_right:
                temp[b_right] = seq[-1 - i]
        dp2.append(temp)
    print(dp1)
    print(dp2)
    ans = 0
    for i in range(1, n - 1):
        mid = seq[i]
        left = dp1[i - 1]
        right = dp2[n - i - 2]
        if mid == left[-1]:
            left = left[:-1] if len(left) > 1 else left
        if mid == right[-1]:
            right = right[:-1] if len(right) > 1 else right
        if mid > left[-1] and mid > right[-1]:
            ans = max(ans, len(left) + len(right) + 1)
    ans = max(ans, len(dp1[-1]), len(dp2[-1]))
    print(ans)


solve()
