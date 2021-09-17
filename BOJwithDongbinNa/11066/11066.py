@profile
def solve():
    t = int(input())
    for _ in range(t):
        k = int(input())
        chp = list(map(int, input().split()))
        # 자 생각해보자
        # 직관적으로 생각했을 때 일찍 합친 파일이 여러번 시간을 잡아 먹기 때문에
        # 그리디하게 생각했을 때 큰 파일일 수록 마지막에 합치고 싶을 것이다
        # 그러나 이렇게 쉽게 우선순위를 적을 수 있는가?
        # 아주 큰 파일이 아주 작은 파일들로 둘러 싸여 있을 때에도 가능한가?
        # 가능하지 작은  흠...
        # dp적으로 생각해보자 이제
        # dp[i]를 뭐로 정의하는가?
        # 기본적을 한번 합칠 때마다 하나의 파일만 붙기 때문에 모든 입력들은 총 챕터 수 - 1만큼은 합쳐야 한다
        # dp[i]를 ith챕터까지 최소의 비용으로 합친 비용이라고 하자
        # dp[i + 1]은 그러면, dp[i] + ch[i]이거나, dp[i - 1] + 음 아니야
        # dp[i][j]를 i번째 챕터에서 j번째 챕터까지 합치는 데 최소 비용으로 할까?
        # 아니야..
        # 새로 하나의 챕터거 주어졌을 때
        # 합이 제일 작은 연속의 두 개를 합친다라는 그리디의 반례가 뭐가 있을까?
        # 8 0 8 5 5 5 5 1
        # 8 0 8 5 5 5 6
        # 4 8 5 5 5 5 6
        # 4 8 10 10 6
        # 12 10 10 6
        # 12 10 16
        # 22 16
        # 38
        """
        res = 0
        for i in range(k - 1):
            adj_sum = [chp[j] + chp[j + 1] for j in range(len(chp) - 1)]
            tmp = min(adj_sum)
            chp[adj_sum.index(tmp)] = tmp
            chp.pop(adj_sum.index(tmp) + 1)
            res += tmp
        print(res)
        """
        # 오호라 그냥 예제도 좋은 반례였다. 왜 그러지?
        # 40 30 30 50
        # 40 60 50| 60
        # 100 50| 100
        # 150| 150
        # 70 30 50|70
        # 70 80| 80
        # 150 | 150
        # 왜지?
        # 총3번의 더하기 연산한 건 똑같고
        # 각 원소들이 몇 번 더하기에 참여했는지 살펴보자
        # 첫번째 방법의 경우, 40 * 2 + 30 * 3 + 30 * 3 + 50 * 1
        # 두번째 방법의 경우, 40 * 2 + 30 * 2 + 30 * 2 + 50 * 2
        # 흠....
        # 겉으로는 더하기의 횟수가 모두 같지만, 각 원소별로 쪼갰을 때는 다르다.
        # dp[i][j]를 j에서 시작하는 길이가 i인 챕터수열의 합의 최솟값으로 정의하면 해결된다!
        dp = [[], [0] * k, [chp[i] + chp[i + 1] for i in range(k - 1)]]
        last_opt = [1] * (k - 1)
        for i in range(3, k + 1):
            temp = []
            cur_opt = [0] * (k - i + 1)
            for j in range(k - i + 1):
                #print(f'i:{i}, j:{j}, last_opt:{last_opt}')
                min_pre = 2**32
                for m in range(last_opt[j], last_opt[j + 1] + 2):
                    if min_pre > dp[m][j] + dp[i - m][j + m]:
                        min_pre = dp[m][j] + dp[i - m][j + m]
                        cur_opt[j] = m
                #print(cur_opt)
                sum_cost = sum(chp[j:j + i])
                temp.append(min_pre + sum_cost)
            last_opt = cur_opt
            dp.append(temp)
        print(dp[k][0])


solve()
