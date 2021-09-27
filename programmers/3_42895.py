# https://programmers.co.kr/learn/courses/30/lessons/42895
# N으로 표현

# 언뜻보기에 비슷하게 생긴 문제로 연산자의 수를 최소화하는 문제가 있는데
# 그 문제는 bfs를 이용하면 쉽게 풀 수 있던 걸로 기억한다

# 이 문제는 실수로 분류를 봐버렸다. DP문제라고 한다.
# DP[N][:number]를 만든다고 쳐도
# number를 구성하는 방법이 너무 많다.
# 그리고 DP[N][:number]만으로는 최적의 방법을 못 찾을 수도 있다.
# 테케만 봐도
# DP[5][12] = DP[5][60] + DP[5][1]인 것을 볼 수 있다.
# 즉, 애초에 optimal substructure를 갖지 않는다.

# DP의 핵심은 Optimal substructure와 Overlapping Subproblems이다
# 생각할 때는, 그냥 하위 문제가 풀렸다고 했을 때
# 하위 문제의 답을 이용해서 상수 시간(subproblem개수에 따라서 꼭 상수 시간은 아니어도 괜찮다) 안에 풀 수 있냐로 생각하면 될 것 같다.
# N을 최대 8개를 이용해서 number를 만드는 방법이라...
# 사용 가능한 사칙연산이 4개 있고, 사용 가능한 숫자는 {N, NN, ..., NNNNNNNN, 기타 N을 8개 이하로 사용해서 만들 수 있는 수)
# 흠...

# 완탐으로 하면 너무 오래 걸리나?
# N을 1개 이용해서 만들 수 있는 수
# N을 2개 이용해서 만들 수 있는 수
# N을 3개 이용해서 만들 수 있는 수
# ...
# N을 8개 이용해서 만들 수 있는 수
# N을 n개 이용해서 만들 수 있는 수 = N을 n-1개 이용해서 만들 수 있는 수와 N을 1개 이용해서 만들 수 있는 수를 이용해서
# + n-2와 2 + ... + 1과 n - 1 + 'N'*n
# 근데 이게 단순히 개수만 저장하면 안 되고, 실제 값을 비트마스킹 느낌으로 갖고 있고, 합성할 때 union을 해야 한다.


MAX_n = 8
# A list of set
dp = [set() for _ in range(MAX_n + 1)]

def construct(n, N):
    global dp
    dp[n].add(int(str(N)*n))

    for i in range(1, n):
        opds_1 = dp[i]
        opds_2 = dp[n - i]
        for opd_1 in opds_1:
            for opd_2 in opds_2:
                dp[n].add(opd_1 + opd_2)
                dp[n].add(opd_1 - opd_2)
                dp[n].add(opd_1 * opd_2)
                if opd_2 != 0:# and opd_1 % opd_2 == 0:
                    dp[n].add(opd_1 // opd_2)
                    # dp[n].add(int(opd_1 / opd_2))
    

def solution(N, number):
    for i in range(1, MAX_n + 1):
        construct(i, N)
        if number in dp[i]:
            print(dp)
            return i
    
    return -1

print(solution(2, 2))
