import math
from operator import add
import fractions


def solve():
    n = int(input())
    els = [int(input()) for _ in range(n)]
    k = int(input())

    # 재밌는 문제다.
    # 팬으로 끄적인 것을 정리해본다.
    # 일단, 기본적인 나머지 연산에 대한 정리.
    # 1. ab mod c = (a mod c)(b mod c) mod c
    # 2. (a + b) mod c = (a mod c + b mod c) mod c
    # 그러면, 원소 e_1 ~ e_n에 대해서 다음이 성립한다.
    # m개의 원소를 골랐고, 순서대로 e_k1, e_k2, ..., e_km으로 명명해보자.
    # 합친수 = e_k1 * 10^p1 + e_k2 * 10^p2 + ... + e_km * 10^pm
    # 여기서 p1~pm은 적절하게 이해할 걸 믿는다(?)
    # K가 상수이기에, x mod K를 그냥 m(x)으로 표기하겠다.
    # m(합친수) = m(e_k1 * 10^p1 + e_k2 * 10^p2 + ... + e_km * 10^pm)
    # " = m(m(e_k1 * 10^p1) + m(e_k2 * 10^p2) + ... + m(e_km * 10^pm))
    # " = m(m(m(e_k1)m(10^p1)) + ... + m(m(e_km)m(10^pm)))
    # 딱봐도, Optimal substructure의 냄새가 나죠?
    # 여기까지는 오케이.
    # 근데 합친수가 몇 가지냐? N!
    # 단순하게 합친수를 순회하는 것은 안 된다.
    # 음, 두 순열이 있는데, 두 원소의 위치만 다르다고 하자.
    # 아니다.
    # 두 순열이 있는데, 상당부분 겹친다고 해보자.
    # 겹친부분은 이미 계산되어 있을 거고, 아니 잠깐만, 이렇게 해도 두 순열을 모두 방문한 것은 안 바뀌네
    # 모든 순열을 방문하면 안 돼.
    # 모든 순열을 방문하지 않고, mod K는 0인 순열의 개수를 어떻게 파악하지...?
    # 가지치기? 이 조건을 만족하는 순열은 다 만족하니 더 이상 탐색 안 해도 된다. 이런식으로?
    # 흠, K가 작을 때는 상상이 되는데, K가 꽤 커도 되나...?
    # 예를 들어서, K=67에 대해서, 단순하게 뒤자리로 판단하기 힘들 거 같은데, 흠..
    # 위에서 나머지 연산에 관한 정리는 주어진 합친수에 대해서 빠르게(?) 나머지 연산을 하는 데는 도움이 되는데
    # 가지치기로 어떻게 쓰지...?
    # 제일 높은 몇 자리에 무조건 e_x가 온다고 쳐보자, 이 가지에 대해서도 아직 (n-1)!개 가능성이 있다
    # 이 n-1개를 전수방문하지 않고, 그 비율 혹은 mod k = 0인 순열의 개수를 알 수 있느가?
    # 아니면!
    # 거꾸로 빠르게 거를까?
    # k=67를 예시로 들면, 67, 134, 201, 268, 335, 402, 469, 536, 603, 670, 737, 804, 871, 938, 1005, 1072
    # 1139, 1206, 1273, 1340, 1407, 1474, 1541, 1608, 1675, 1742, 1809, 1876, 1943, 2010, 2077, 2144
    # 2211, 2278, 2345, 2412, 2479, 2546, 2613, 2680, 2747, 2814, 2881, 2948, 3015, 3082, 3149
    # 3216, 3283, 3350, 3417, 3484, 3551, 3618, 3685, 3752, 3819, 3886, 3953, 4020, 4087, 4154
    # 4221, 4288, 4355, 4422, 4489, 4556, 4623, 4690, 4757, 4824, 4891, 4958, 5025, 5092, 5159
    # 5226, 5293, 5360, 5427, 5494, 5561, 5628, 5695, 5762, 5829, 5896, 5963, 6030, 6097, 6164
    # 6231, 6298, 6365, 6432, 6499, 6566, 6633, 6700, 6767
    # 와 생각보다 한참 걸렸네
    # ㅈㄴ 아무 생각없이 그냥 뒷2자리가 돌아올 때까지 계속 더했는데, 101배 때 돌아왔네
    # 내가 지금 한 게 뭐냐면, 67*x mod 100이 67일때까지 기다린건데, (67 mod 100 * x mod 100) mod 100한 거고
    # (67* xmod100) mod 100 = 67한 거고
    # 흠..
    # k=67의 경우, 뒤2자리만 봐서는 결정할 수 없는 거 같네? 모든 2자리가 다 나온 거 같은데
    # 왜 그러지? 흠.....
    # 근데 방향은 이쪽이 맞는 것 같다.
    # 말단까지 가서 한 순열을 확정 짓기 전에, 미리 안봐도비디오식으로, 얘는 무조건 된다/안된다 식으로 가지치기 하기.
    # 이것 말고는 전수방문하지 않고, 나누어 떨어지는 순열의 수를 구할 방법이 없지 않나
    # 근데 무조건 된다는 딱바도 말이 안 된다, K가 2같은 거면 몰라도, 67같은 비교적 큰 소수면, 뒷자리에는 뭐든지 올 수 있다.
    # 67이면 뒷자리에 뭐든지 올 수 있기에, 뒷자리만 보고 아예 판단이 안 된다. 앞자리만 봐서도 안 될 거 같은데...
    # 뒷 3자리보면 해결되나? 임의의 K가 주어질 때 뒷 몇 자리를 볼지 어떻게 결정하지?
    # 확실히 앞자리보다는 뒷자리 보는 게 맞는듯.
    # 그럼 일단 K = 2이 같은 간단한 K라고 가정해보자. 그러면 풀 수 있나?
    # 그러면 모든 e_x에 대해서 e_x가 뒤에 올때는 어떨지에 대한 확률이 있다.
    # 아 근데, K가 두 자리고, e_x가 한 자리면 또 골때려지는데 후.....뭔가 구현이 쉽지 않을 거 같은데
    # 임의의 K주어졌을 때, d(K)자리를 봐야 된다고 치자.
    # 그러면 len(e_x)<d(K)인 e_x에 대해서는 서로 조합하고, 다른 애들이랑 붙이고 별 지랄을 다 해야되네 후....
    # 그리고 확실히 안 되는 경우만 가져올 확률이 높아서, 가능성있는 애들은 또 따지고 들어가면서 확인해야 됨...
    """
    mod_10s = [10**int(math.log10(el) + 1) % k for el in els]
    mod_els = [el % k for el in els]
    dp = [[0] * k for _ in range(1 << n)]
    dp[0][0] = 1
    for state in range((1 << n) - 1):
        # solve dp[state with a single more 1 digit]
        target_el_bit = 1
        target_el = 0
        while target_el < n:
            if not (state & target_el_bit):
                # accumulate dp[state | target_el_bit]
                step_1 = [0] * k
                for mod, count in enumerate(dp[state]):
                    step_1[mod * mod_10s[target_el] % k] += count
                step_2 = step_1
                for i in range(k):
                    step_2[i] = step_1[(i + mod_els[target_el]) % k]
                dp[state | target_el_bit] = list(map(add, dp[state | target_el_bit], step_2))
            target_el_bit <<= 1
            target_el += 1
    print(dp[(1 << n) - 1][0])
    """
    mod_10s = [10**int(len(str(el))) % k for el in els]
    mod_els = [el % k for el in els]
    mem = [None] * (1 << n)
    mem[0] = [1]

    def dp(state):
        if mem[state] is not None:
            return mem[state]
        target_el_bit = 1
        target_el = 0
        step_3 = [0] * k
        while target_el_bit <= state:
            if target_el_bit & state:
                step_1 = [0] * k
                for mod, count in enumerate(dp(~target_el_bit & state)):
                    step_1[mod * mod_10s[target_el] % k] += count
                step_2 = [0] * k
                for i in range(k):
                    step_2[(i + mod_els[target_el]) % k] = step_1[i]
                step_3 = list(map(add, step_3, step_2))
            target_el_bit <<= 1
            target_el += 1
        mem[state] = step_3
        return mem[state]
    res = fractions.Fraction(dp((1 << n) - 1)[0], math.factorial(n))
    for i in range(1 << n):
        print(f'{bin(i)}: {mem[i]}')
    print(f'{res.numerator}/{res.denominator}')


solve()
