import sys
from functools import lru_cache
sys.setrecursionlimit(10**7)

def solve():
    read = sys.stdin.readline
    ans = []
    for _ in range(int(read())):
        n, k = map(int, read().split())
        delay = [0] + list(map(int, read().split()))
        prereq = [[] for _ in range(n + 1)]
        for _ in range(k):
            x, y = map(int, read().split())
            prereq[y].append(x)
        # 음 생각해보자.
        # 3665의 1등 답에서 실질적으로 누가 누구를 가리키는지 알 필요 없다는 것을 봤다.
        # 이 문제도 같을까?
        # 아닌 것 같다. 그때는 간선에 웨이트가 없었다. 아닌가...?
        # 지금처럼 웨이트가 있어도 결과적으로 흠.. 헷갈리군
        # 아 일단 다 잊어버리고 어떻게 풀지 생각해보자.
        # 목표 건물이 있다.
        # 목표 건물부터 출발하는 게 당연한 것 같다.
        # 물론 바텀업으로 시작할 수도 있겠...있나?
        # 바탐업으로 모든 건물의 최소 시간을 구할 수 있을 것 같긴한데...
        # 직관상 탑다운이 나을 거 같다.
        # 자 목표 건물이 있다.
        # 목표 건물의 필요 조건을 확인한다. 
        # 흠 이거 dp에 가까운데...?
        # dp로 함 풀어보겠다.
        @lru_cache(None)
        def delayTotal(b):
            return max([delayTotal(p) for p in prereq[b]], default=0) + delay[b]
        ans.append(str(delayTotal(int(read()))))
    print('\n'.join(ans))


solve()
