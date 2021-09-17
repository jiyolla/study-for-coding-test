import sys
from collections import OrderedDict
sys.setrecursionlimit(10**7)

def solve():
    n = int(input())
    dst = list(map(int, input().split()))
    p = list(map(int, input().split()))
    od_p = sorted(OrderedDict({i: p[i] for i in range(n)}).items(), key=lambda x:x[1], reverse=True)
    """
    def grd(dest):
        if dest == 0:
            return 0
        best_p = min(p[:dest])
        best_i = p.index(best_p)
        return grd(best_i) + best_p*sum(dst[best_i:dest])
    print(grd(n - 1))
    """
    # 최악의 경우 10만번 재귀해서 시간초과가 뜬 거 같다. 겨우만 10만번으로 시간초과가 뜨나..?
    # 재귀로 안 푼다면 흠...
    """
    dest = n - 1
    ans = 0
    while dest > 0:
        best_p = min(p[:dest])
        best_i = p.index(best_p)
        ans += best_p * sum(dst[best_i:dest])
        dest = best_i
    print(ans)
    """
    # 여전히 시간 초과. 아무래도 min이랑 index를 10만번하는게 문제인듯. sum은 도합 10만번해서 문제 없음.
    # min은 지금 거의 n^2걸린다. 흠...
    # dict을 만들어서 원래 위치와 소팅한 위치를 페어로 만들어서 저장하고 이 dict을 순회할까?
    dest = n - 1
    ans = 0
    while dest > 0:
        best = od_p.pop()
        while best[0] >= dest:
            best = od_p.pop()
        ans += best[1] * sum(dst[best[0]:dest])
        dest = best[0]
    print(ans)
    # 아 1등 코드 보니까, 굳이 뒤에서 시작할 필요가 없었다는 깨달음의 허탈함이...


solve()
