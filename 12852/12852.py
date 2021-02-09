def solve():
    n = int(input())

    mem = {1: 0, 2: 1}
    track = []

    def ans(n):
        if n in mem:
            return mem[n]
        mem[n] = min(ans(n//2) + n % 2, ans(n//3) + n % 3) + 1
        return mem[n]

    def ans_track(n):
        # expected output shown only when all cache is ready
        track.append(str(n))
        if n == 1:
            return
        if n == 2:
            track.append('1')
            return
        if mem[n//2] + n % 2 < mem[n//3] + n % 3:
            if n % 2 == 1:
                track.append(str(n - 1))
            ans_track(n // 2)
        else:
            for i in range(1, n % 3 + 1):
                track.append(str(n - i))
            ans_track(n // 3)
    print(ans(n))
    ans_track(n)
    print(' '.join(track))


solve()
