from collections import deque

@profile
def solve():
    print_buffer = []
    for _ in range(int(input())):
        a, b = map(int, input().split())

        q = deque()
        q.append((a, 0))
        # mem[i] = (steps to i, prev_i to i, last_op to i)
        mem = [() for _ in range(10000)]
        mem[a] = (0, a, 'INIT')
        found = False
        while q and not found:
            for _ in range(len(q)):
                cur, step = q.popleft()
                if cur == b:
                    found = True
                    break
                step += 1
                D = cur * 2 % 10000
                if not mem[D]:
                    mem[D] = (step, cur, 'D')
                    q.append((D, step))
                S = cur - 1 if cur != 0 else 9999
                if not mem[S]:
                    mem[S] = (step, cur, 'S')
                    q.append((S, step))
                L = (cur - cur//1000*1000) * 10 + cur//1000
                if not mem[L]:
                    mem[L] = (step, cur, 'L')
                    q.append((L, step))
                R = cur // 10 + cur % 10 * 1000
                if not mem[R]:
                    mem[R] = (step, cur, 'R')
                    q.append((R, step))
        cur = b
        traceback = []
        while cur != a:
            traceback.append(mem[cur][2])
            cur = mem[cur][1]
        print_buffer.append(''.join(traceback[::-1]))
    print('\n'.join(print_buffer))


solve()
