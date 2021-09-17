import sys


def solve():
    read = sys.stdin.readline

    def root(u):
        while uf[u][0] != u:
            uf[u][0] = uf[uf[u][0]][0]
            u = uf[u][0]
        return u
    res = []
    for _ in range(int(read())):
        f = int(read())
        # uf[name] = [parent_name, count_name]
        uf = {}
        # lazy업데이트를 못하는 건가...?
        # 일단 확실한 것은 입력 받자마자 합집합을 하고 바로 그 상태의 값을 출력해야 됨
        # 다 처리하고 나중에 그때의 값을 다시 찾는 것은 너무 복잡하고 아마 비효율적일 것임.
        # 그럼 매 합집합을 다 했을 때 항상 최신의 size()를 부를 수 있어야 한다라...
        # 매번 바로 root까지 압축을 해야겠네...흠.. 시간이 될려나

        for _ in range(f):
            u1, u2 = read().split()
            if u1 not in uf:
                uf[u1] = [u1, 1]
            if u2 not in uf:
                uf[u2] = [u2, 1]
            root_u1 = root(u1)
            root_u2 = root(u2)
            if root_u1 == root_u2:
                res.append(str(uf[root_u1][1]))
            else:
                if uf[root_u1][1] < uf[root_u2][1]:
                    uf[root_u1][0] = root_u2
                    uf[root_u2][1] += uf[root_u1][1]
                    res.append(str(uf[root_u2][1]))
                else:
                    uf[root_u2][0] = root_u1
                    uf[root_u1][1] += uf[root_u2][1]
                    res.append(str(uf[root_u1][1]))
    print('\n'.join(res))
    # 역C...시간 초과...


solve()
