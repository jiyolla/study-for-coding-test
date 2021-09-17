def solve():
    n = int(input())
    w = list(map(int, input().split()))
    m = int(input())
    q = list(map(int, input().split()))

    # 주어진 추들을 더하고 빼고 해서 특정 무게를 맞출 수 있냐에 대해서 답하는 문제이다.
    # 그냥 전수조사로는 dfs나 bfs로 할 수 있겠고, 그러면 걸리는 시간은 각각의 추의 가능성이 3가지가 있으니, 3^30.
    # 근데 생각해보면 dfs문제 풀 때도, dp처럼 memoization기법을 써서 가지치기를 상당히 한 거 같다.
    mem = {0: True}
    for i in w:
        temp = {}
        for j in mem.keys():
            temp[j - i] = True
            temp[j + i] = True
        mem.update(temp)
    print(' '.join(['Y' if i in mem else 'N' for i in q]))


solve()
