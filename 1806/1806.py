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
            # print(f'skip: l: {l}, r: {r}, acc: {acc}')
            acc -= seq[l]
            if r == l:
                ans = 1
                break
            continue
        end_reached = True
        for nr in range(r + 1, n):
            acc += seq[nr]
            # print(f'l: {l}, r: {r}, nr: {nr}, acc: {acc}, ans: {ans}')
            if acc >= s:
                ans = nr - l + 1 if nr - l + 1 < ans else ans
                r = nr
                end_reached = False
                break
        if end_reached:
            break
        acc -= seq[l]
    print(0 if math.isinf(ans) else ans)
    # 아 이거 굉장히 드러운데 코드가..역시 통과 못하지
    # 왜케 복잡해졌지?
    # 로직을 다시 한번 풀어서 말해보자.
    # l,r로 현재 수열의 양 끝을 가리킴
    # 수열의 길이는 그러면 쉽게 구해지고
    # acc로 현재 수열의 합을 저장함
    # l,r을 움직일 대마다 acc그에 맞게 수정해주면 됨
    # 이거를 구현하기 위해서
    # 기본적으로 가장 바깥 루프에서 l을 0에서 n-1까지 순회시킴
    # 즉 가장 바깥 루프가 도든 것은 l이 움직이는 것
    # 그래서 가장 바깥 루프가 돌 때는 항상 acc-=seq[l]이 수반됨
    # 여기가지 문제 없고
    # 루프 안에서는 어떤 일이 벌어지냐
    # 가장 먼저 l혹시 r을 뛰어넘었는지 확인한다
    # 언제 이런 일이 발생하지? r이 움직이지 않고 l이 증가할 때
    # 언제 저런 일이 발생하지? 두 번째조건이나, 두 번째 조건이 충족될 때 밖에 없는데
    # 잘보면 두 번째 조건에서 지금 체크를 해주기 때문에 이거 삭제해도 됨.
    # 자 그리고 acc가 s를 만족하는지를 확인하는데, 만족한다면
    # 감소시켜아하는 거니까 r움직이지 말고 l을 움직여야 됨
    # 그래서 바로 다음 루프로 가고, 혹시 같으면 1이니까 끝난 거고
    # 그렇지 않다하면, acc<s인거니까 r을 움직여야 됨
    # 


solve()
