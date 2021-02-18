from collections import deque


def solve():
    print_buffer = []
    for _ in range(int(input())):
        a, b = map(int, input().split())

        q = deque()
        q.append(a)
        # mem[i] = (steps to i, prev_i to i, last_op to i)
        mem = [() for _ in range(10000)]
        mem[a] = (0, a, 'INIT')
        found = False
        step = 0
        q_sum = 0
        while q and not found:
            step += 1
            q_sum += len(q)
            for _ in range(len(q)):
                cur = q.popleft()
                D = cur * 2 % 10000
                S = cur - 1 if cur != 0 else 9999
                L = cur * 10 % 10000 + cur//1000
                R = cur // 10 + cur % 10 * 1000
                if not mem[D]:
                    mem[D] = (step, cur, 'D')
                    if D == b:
                        found = True
                        break
                    q.append(D)
                if not mem[S]:
                    mem[S] = (step, cur, 'S')
                    if S == b:
                        found = True
                        break
                    q.append(S)
                if not mem[L]:
                    mem[L] = (step, cur, 'L')
                    if L == b:
                        found = True
                        break
                    q.append(L)
                if not mem[R]:
                    mem[R] = (step, cur, 'R')
                    if R == b:
                        found = True
                        break
                    q.append(R)
        cur = b
        traceback = []
        while cur != a:
            traceback.append(mem[cur][2])
            cur = mem[cur][1]
        print_buffer.append(''.join(traceback[::-1]))
    print('\n'.join(print_buffer))
    print(q_sum)
    # 좋은 아이디어가 떠올랐다. 각 숫자를 노드 하나로 표현하고,
    # LSDR의 의해서 변환될 수 있는 숫자를 일방향으로 연결되어 있다고 표현하는 것이다.
    # 그러면 테스트케이스 수에 상관없이 한번만 벨만포드 돌리면 된다.
    # 아근데 벨만포드가 O(VE)혹은 O(E^2)인데, 그러면 10000 * 10000 * 4이네....
    # 벨만포드 말고 그냥 다익스트라만 돌리면 O(E log V)이라..
    # 테스트케이스가 대충 100개 이하면 다익스트라 이득이네
    # 원래 알고리즘의 시간복자도는 어떻게 되지?
    # 오히려 더 빠른 거 같은데...? O(V)는 될 거 같은데, 모든 점을 최대 1번 방문하니까
    

solve()
