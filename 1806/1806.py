import math


def solve():
    n, s = map(int, input().split())
    seq = list(map(int, input().split()))
    # 길이가 N인 수열이 들어온다.
    # 연속합이 S이상 되는 원소들의 최소 길이를 구한다.
    # l,r로 현재 수열의 양 끝을 가리킨다.
    # 즉 l,r은 포함
    # 처음에 l = r = 0으로 시작하고
    # acc로 해당 수열의 합을 표현한다.
    # l = r = 이면 길이가 1인 수열이기에 acc = seq[0]이 맞음
    # 그 후에 acc의 값에 따라서 l을 옯길지, r옯길지를 정한다.
    # acc가 S보다 크다면, 그전에
    # l,r모두 한쪽으로만 움직인다.
    # 위에 이어서, l을 움직인다.
    # 근데 그전에 먼저 해당 수열의 길이를 기록할 필요가 있다. 조건에 부합하니, 후보 중에 하나다.
    # l을 움직이고 싶은데 l을 움직이면 r보다 커진다? 즉 길이가 1인 수열로 조건에 부합했다는 건데
    # 그러면 사실 더 검색할 것도 없다. 최솟값을 찾은 것이다.
    # 그렇지 않다면, l을 움직이고 나면 acc는 l이 움직인만큼 작아지고,
    # 위에 작업을 똑같이 하면 된다.
    # l이 r을 넘는 순간 끝나도 상관없다.
    r = 0
    acc = seq[0]
    ans = math.inf
    for l in range(n):
        if acc >= s:
            ans = r - l + 1 if r - l + 1 < ans else ans
            # print(f'skip: l: {l}, r: {r}, acc: {acc}, ans: {ans}')
            if r == l:
                ans = 1
                break
        else:
            for nr in range(r + 1, n):
                acc += seq[nr]
                # print(f'l: {l}, r: {r}, nr: {nr}, acc: {acc}, ans: {ans}')
                if acc >= s:
                    ans = nr - l + 1 if nr - l + 1 < ans else ans
                    r = nr
                    break
            else:
                break
        acc -= seq[l]
    print(0 if math.isinf(ans) else ans)


solve()
