import sys


def solve():
    read = sys.stdin.readline
    n = int(read())
    seq = list(map(int, read().split()))
    # 두 개 용액을 골라서 합이 0에 가깝게 하는 것인데...
    # 투 포인터의 정석에서 근사값을 허락한 것이네
    # 일단 sort
    seq.sort()
    # 만약에 전부 마이너스면, 가장 큰 두 개의 원소가 답이고
    # 전주 플러스면, 가장 작은 두 개의 원소가 답이다.
    # 그냥 양 끝단에서 출발하는 게 아니라,
    # 0에서 투포인터로 양 옆으로 가는 게 맞는 거 같다
    # 그니까 첫 -에서 왼쪽으로 첫 +에서는 오른쪽으로 이런식으로
    # 아닌가..?
    # 그냥 양 끝에서 출발하면 어떻게 돼지?
    # - +이라고 해보자.
    # 합친 것의 절대값을 기존 최솟값과 비교해
    # 작으면 업데하고
    # 크면 합친값이 플러스인가 마이너스인가에 따라서
    # s가 움직이거나 e가 움직여야 한다
    # -700 -695 -690 -80 0 2 120 700이라고 하면
    # 첨에 -9... inf보다 작으니 업데
    # 그 담에 s+1하고 e-1을 비교한다..
    # 
    ans = []
    opt = 0
    s = 0
    e = 0
    for i in range(1, n - 1):
        if seq[i] >= 0:
            if abs(seq[i - 1] + seq[i]) < abs(seq[i + 1] + seq[i]):
                s = i - 1
                e = i
                opt = abs(seq[i - 1] + seq[i])
                ans = [s, e]
            else:
                s = i
                e = i + 1
                opt = abs(seq[i + 1] + seq[i])
                ans = [s, e]
            break
    if not ans:
        s = n - 2
        e = n - 1
        opt = abs(seq[s] + seq[e])
        ans = [s, e]
    while s > 0 and e < n - 1:
        mv_s = abs(seq[s - 1] + seq[e])
        mv_e = abs(seq[s] + seq[e + 1])
        if mv_s < mv_e:
            s -= 1
            if opt > mv_s:
                opt = mv_s
                ans = [s, e]
        else:
            e += 1
            if opt > mv_e:
                opt = mv_e
                ans = [s, e]
    while s > 0:
        now = abs(seq[s] + seq[e])
        mv_s = abs(seq[s - 1] + seq[e])
        if mv_s > now:
            break
        s -= 1
        if opt > mv_s:
            opt = mv_s
            ans = [s, e]
    while e < n - 1:
        now = abs(seq[s] + seq[e])
        mv_e = abs(seq[s] + seq[e + 1])
        if mv_e > now:
            break
        e += 1
        if opt > mv_e:
            opt = mv_e
            ans = [s, e]
    print(seq[ans[0]], seq[ans[1]])


solve()
