import sys


def solve():
    read = sys.stdin.readline
    m = int(read())
    all_s = [str(i) for i in range(1, 21)]
    s = []
    div = 520912
    for i in range(m // div):
        ans = []
        for _ in range(div):
            cmd = read().split()
            if cmd[0] == 'add':
                if cmd[1] not in s:
                    s.append(cmd[1])
            if cmd[0] == 'remove':
                if cmd[1] in s:
                    s.remove(cmd[1])
            if cmd[0] == 'check':
                ans.append('1' if cmd[1] in s else '0')
            if cmd[0] == 'toggle':
                if cmd[1] in s:
                    s.remove(cmd[1])
                else:
                    s.append(cmd[1])
            if cmd[0] == 'all':
                s = all_s
            if cmd[0] == 'empty':
                s = []
        print('\n'.join([i for i in ans]))
    ans = []
    for _ in range(m % div):
        cmd = read().split()
        if cmd[0] == 'add':
            if cmd[1] not in s:
                s.append(cmd[1])
        if cmd[0] == 'remove':
            if cmd[1] in s:
                s.remove(cmd[1])
        if cmd[0] == 'check':
            ans.append('1' if cmd[1] in s else '0')
        if cmd[0] == 'toggle':
            if cmd[1] in s:
                s.remove(cmd[1])
            else:
                s.append(cmd[1])
        if cmd[0] == 'all':
            s = all_s
        if cmd[0] == 'empty':
            s = []
    print('\n'.join([i for i in ans]))


solve()
