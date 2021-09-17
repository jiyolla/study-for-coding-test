def solve():
    m, n = map(int, input().split())
    x, y = 0, 0
    dx, dy = 1, 0
    illegal = False
    for _ in range(n):
        cmd = input().split()
        if cmd[0] == 'MOVE':
            x += dx * int(cmd[1])
            y += dy * int(cmd[1])
            if x > m or y > m or x < 0 or y < 0:
                illegal = True
                break
        if cmd[0] == 'TURN':
            if cmd[1] == '0':
                # 1 0, 0 1, -1 0, 0 -1
                dx, dy = dy * -1, dx
            if cmd[1] == '1':
                # 1 0, 0 -1, -1 0, 0 1
                dx, dy = dy, dx * -1
    print('-1' if illegal else f'{x} {y}')


solve()
