def solve():
    n = int(input())
    # 11066: 파일 합치기 문제와 매우 비슷하다.
    # 합치기 대신 곱산 연산을 진행하며, 곱산 연산을 한번 할 때마다 비용이 발생된다.
    # 거의 똑같게 구현할 수 있을 것 같다. 비용 구하는 방정식만 수정해주면 될 것 같다.
    matrix = [list(map(int, input().split())) for _ in range(n)]

    # dp[i][j]는 j에서 시작하는 길이가 i인 연속 행렬곱. 그 행렬의 크기는 matrix[j]의 r * matrix[j + i - 1]의 c.
    dp = [[], [0] * n, [matrix[i][0] * matrix[i][1] * matrix[i + 1][1] for i in range(n - 1)]]
    # """
    last_opt = [1] * (n - 1)
    for i in range(3, n + 1):
        cur_opt = [0] * (n - i + 1)
        temp = []
        for j in range(n - i + 1):
            opt = 2**32
            for k in range(last_opt[j], last_opt[j + 1] + 2):
                # print(f'i:{i}, j:{j}, k:{k}')
                cost = dp[k][j] + dp[i - k][j + k] + matrix[j][0] * matrix[j + k][0] * matrix[j + i - 1][1]
                if opt > cost:
                    opt = cost
                    cur_opt[j] = k
            temp.append(opt)
        dp.append(temp)
        last_opt = cur_opt
    # 최적화 부분에서 파일 합치기와 다른 점이 있다. 이 부분이 해결되지 않으면 시간 안에 해결 못한다.
    # 합치기에서는 최적화의 근거는 크면 클수록 늦게 합쳐야 한다는 것에 있었다. 특히 원소가 하나밖에 차이 나지 않을 때는 말이다.
    # 행렬곱셈에서는 어떤 규칙을 찾아볼 수 있을까? 대가리와 끝을 최대한 작게 유지하고 싶다. 대가리와 끝만 다음 곱셈에 한번 더 참여하기 때문이다.
    # 원소가 하나 추가 되면 일단 끝이 바뀐다. 극단적으로 새로 추가된 원소의 column이 지나치게 크면, cur_opt의 값은 갑자기 끝으로 땡겨지게 된다. 최대한 그 끝이 적게 곱셈 참여하도록 하기 위해서 말이다.
    # 그렇다면 어떻게 하면 cur_opt의 범위를 추론하여 좁힐 수 있을까/ last_opt[+1]이 마지막 원소에 대해 꽤 정보를 제공해줄 수 있을 것 같다.
    # 
    """
    for i in range(3, n + 1):
        temp = []
        for j in range(n - i + 1):
            temp.append(min([dp[k][j] + dp[i - k][j + k] + matrix[j][0] * matrix[j + k][0] * matrix[j + i - 1][1] for k in range(1, i)]))
        dp.append(temp)
    print(dp[n][0])
    """


solve()
