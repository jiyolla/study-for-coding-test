import sys
import math


def solve():
    read = sys.stdin.readline
    n = int(read())
    w = int(read())
    # work[0]은 A의 초기 위치, work[1]은 B의 초기 위치, 사건 지점은 work[2:w+2].
    work = [[1, 1], [n, n]] + [list(map(int, read().split())) for _ in range(w)]
    # 어떻게 state를 정의해야 optimal substructure가 존재하게 할 수 있을까?
    # 어떻게 이 상태에 이르렀는지와 상관없게 최적의 결정을 할 수 있게.
    # 거꾸로 생각해보자.
    # 마지막 지점도 방문은 해야 돼. 근데 어떤 위치에 있던 어떤 차가 방문하냐의 문제이다.
    # 1개의 지점을 방문한 상태에서 차 한 대가 바로 마지막 지점을 방문하고 나머지는 다 나머지 차가 방문하는 것
    # + 2개의 지점을 방문한 상태에서 
    # + 3개의 지점을 방문한 상태에서 한 차 마지막 지점 방문...
    # + ...
    # + 99개 지점을 방문한 상태에서 한 차가 마지막 지점 방문
    # 이중에서 제일 작은 것을 고르면 반드시 정답이 되는가?
    # ㅇㅇ 있을 거 같음
    # car_a/b[i]는 a/b차가 i번째 일까지 최적 처리 했을 때의 마지막 위치(work에서 index), 1 <= i <= w
    # ex: car_a[1] = 0(사건1을 b차가 처리하는 게 최적일 때) or 2(사건1을 a차가 처리하는 게 최적일 때)
    car_a = [0] + [0] * w
    car_b = [1] + [0] * w
    # d[i]는 i번째 일까지 최적 처리 했을 때 최소 이동거리의 합
    # ex: d[1] = dist(work[car_a[0]], work[2]) or dist(work[car_b[0]], work[2])
    d = [0] + [math.inf] * w

    def dist(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    # sum_dist[i]는 1번째일부터 i번째 일까지 한 차가 연속처리 했을 때 이동하는 거리의 합
    # 1번째일 처리는 끝났다고 가정하기에 sum_dist[1]은 0이다. 이렇게 처리한 이유는 두 차가 같은 sum_dist를 사용할 수 있기 위해서.
    sum_dist = [0] * (w + 1)
    for i in range(2, w + 1):
        sum_dist[i] = sum_dist[i - 1] + dist(work[i + 1], work[i])

    traceback = []
    # i번째 일을 처리한다
    for i in range(1, w + 1):
        # j = 0 ~ i-1번째 일을 처리한 상태에서 한 차가 바로 i번째 일을 처리한다
        for j in range(i):
            # d_a/b는 j번일을 처리한 상태에서 차a/b가 i번 일을 처리하러 갈 때의 거리
            d_a = dist(work[car_a[j]], work[i + 1])
            d_b = dist(work[car_b[j]], work[i + 1])
            # 둘 다 초기 위치에 있고, 첫 지점이 마지막 지점이 아닐 때는 상대가 첫 지점을 방문하는 거리를 추가해야 됨
            # d_straight에는 1번째 일이 처리됐다고 가정하기 때문
            if j == 0 and i > 1:
                d_a += dist(work[car_b[0]], work[2])
                d_b += dist(work[car_a[0]], work[2])
            # d_straight는 선택되지 않은 차가 나머지 일을 다 처리할 때의 거리
            # = j + 1번째 일에서 i - 1번쨰 일까지 한 차가 연속처리할 때의 이동거리
            d_straight = sum_dist[i - 1] - sum_dist[j]
            # print(f'i: {i}, j: {j}, d_a: {d_a}, d_b: {d_b}, d_straight: {d_straight}')
            if d_b > d_a:
                new_d = d_a + d_straight + d[j]
                if new_d < d[i]:
                    d[i] = new_d
                    # i + 1이 work에서 i번째 일임
                    car_a[i] = i + 1
                    car_b[i] = i if i - j > 1 else car_b[i]
                    # traceback[x] = (j, i, c)에 대해서
                    # j + 1번 일부터 i번 일의 처리에 관한 것이며, i번 일을 a가 처리한다
                    # 중간 fill in 여부는 i - j에 달림
                    traceback.append((j, i, '1'))
            else:
                new_d = d_b + d_straight + d[j]
                if new_d < d[i]:
                    d[i] = new_d
                    car_a[i] = i if i - j > 1 else car_a[i]
                    car_b[i] = i + 1
                    traceback.append((j, i, '2'))
            # print(f'car_a: {car_a}, car_b: {car_b}, d: {d}')
    print(d[-1])
    # 자, 이제 traceback구현.
    last = w
    ans = []
    for s, e, car in traceback[::-1]:
        print(s, e, car)
        if e > last:
            continue
        last = s
        # last pos
        ans.append(car)
        # fill in
        other_car = '1' if car == '2' else '2'
        for i in range(e - s - 1):
            ans.append(other_car)
        if s == 0:
            break
    print('\n'.join(ans[::-1]))


solve()
