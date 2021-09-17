import sys


def solve():
    s1 = input()
    s2 = input()
    # LCS문제 어떻게 풀더라...?
    # 두 개의 문자열이 주어지는데, 가장 긴 공통 부분 수(문자)열을 찾으라라.
    # 한 수열의 원소들을 하나씩 방문하면서, 상대 수열과 비교를 하는데
    # ACAYKP
    # CAPCAK라고 하면
    # 첫 수열에서 A를 고르고, 다른 수열에서 CA를 거쳐서 A를 찾았다.
    # 음...
    # dp[i]는 기방문한 첫 문자열의 부분 문자열 중,
    # 두번째 문자열과의 공통 문자열의 길이가 i + 1인 문자열 중,
    # 두번째 문자열에서의 마지막 원소의 위치가 가장 작은 문자열의 마지막 원소 위치이다.
    # 그러면 새로운 문자가 들어올 때 dp를 돌면서 마지막 위치에서 새 문자를 검색하면 될 듯하다.
    # 음 여기서 최적화를 좀 더 하자면, 매번 새 문자의 위치를 찾는 것보다
    # 총 26개의 문자밖에 없으니까 그냥 한번 전수방문해서 테이블을 미리 만들어놓으면 좋을 듯.
    # s1 <= s2
    s1, s2 = (s1, s2) if len(s1) < len(s2) else (s2, s1)
    # idx[c]는 문자c가 s2에서 나타나는 위치의 리스트
    idx = {chr(ord('A') + i): [] for i in range(26)}
    for i, c in enumerate(s2):
        idx[c].append(i)
    mem = []
    traceback = []
    for i, c in enumerate(s1):
        if idx[c]:
            mem.append(idx[c][0])
            traceback.append((i, 0))
            break
    for j in range(i + 1, len(s1)):
        # mem에 지금까지 방문한 문자열의 매칭에 대한 정보가 담겨 있다.
        # 예를 들면, mem[-1]은 지금까지 방문한 문자열 중 길이가 가장 긴 놈의 마지막 매칭의 위치(s2에서)가 담겨 있고
        # mem[1]은 길이가 2인 매칭의 가장 빠른 매칭 위치가 나타나 있다.
        # 자 이정보를 어떻게 활용할까?
        # 현재 문자 c가 주어졌을 때 mem을 한번 다 도는 것이다.
        # s2에서 mem[1]에 위치에 출발해서 c를 검색하는 것이다.
        # 그리고 그 위치가 mem[2]보다 작으면 mem[2]를 업데하는 식이다.
        # 단, 업데한 mem[2]를 가지고 위에 작업을 하면 안 된다.
        # 원래의 mem[2]를 갖고 해야 한다.
        # 그러면 아싸리 mem[-1]부터 하면 되지 않을까
        # mem[-1]은 예외적으로 매칭이 찾아지면 append를 하고
        # 음 여기서 검색할 때, LIS처럼 bisect을 이용하지 못하는 게 살짝 아쉬워서
        # 위에 문자에 대한 s2위치 정리를 했다.
        # idx[문자]하면 s2에서 문자가 나타나는 위치 리스트가 나타난다. 그러면 한결 검색이 빨라질 것 같다
        # iterator도 만들까 했는데, 생각해보니 항상 더 나중 위치에서 검색하는 것은 아니기에 안 된다.
        # 예를 들어 원래는 후반에서 매칭됐는데 나중에 초반에 있는 문자가 나타나서 초반으로 땡겨지면 iter가 앞에 있던 녀석들을 못 찾는다.
        # 아니 생각해보니 여기서는 bisect을 쓸 수가 있네???
        # 근데 bisect보다 여기서 iter쓰는게 더 빠를 수도?
        # bisect에서 검색 범위를 계속 수정해주면 bisect이 무조건 더 빠르긴 한데...
        # 일단 그냥 iter로 구현하자. 이게 구현이 좀 더 쉽다.
        c = s1[j]
        idx_iter = iter(idx[c])
        new_mem = mem[:]
        try:
            cur_idx = next(idx_iter)
            if cur_idx < mem[0]:
                new_mem[0] = cur_idx
                traceback.append((j, 0))
            for k in range(len(mem) - 1):
                while cur_idx <= mem[k]:
                    cur_idx = next(idx_iter)
                if cur_idx < mem[k + 1]:
                    new_mem[k + 1] = cur_idx
                    traceback.append((j, k + 1))
            while cur_idx <= mem[-1]:
                cur_idx = next(idx_iter)
            new_mem.append(cur_idx)
            traceback.append((j, len(mem)))
        except StopIteration:
            pass
        mem = new_mem
    cur_len = len(mem)
    print(cur_len)
    # 자, 이제 traceback을 구현하면 된다
    # 여기서 traceback을 어떻게 하냐 흠...
    # 그 LIS할 때처럼, s1의 각 문자가 mem에 영향 줄 경우, 영향 줄 때 mem의 idx를 기록하면 될 것 같다.
    # 근데 LIS와 다르게, LIS는 각 숫자가 정확히 한번만 영향을 끼치는데, 여기는 좀 다르다.
    # 영향 아예 안 끼칠 수도 있고, 여러번 끼칠 수도 있다. 흠..
    # 근데 문제 없는 것 같다.
    # traceback에 tuple로 (해당 문자, mem수정 위치)를 기록하고
    # 거꾸로 traceback을 순회하면서 mem수정위치가 1씩 작은 놈들만 계속 출력하면 되겠다. ㅇㅋ
    ans = []
    selected = [False] * len(s1)
    for j, i in traceback[::-1]:
        if i == cur_len - 1 and not selected[j]:
            cur_len -= 1
            selected[j] = True
            ans.append(s1[j])
            if cur_len == 0:
                break
    if ans:
        print(''.join(ans[::-1]))


solve()
