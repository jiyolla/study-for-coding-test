import sys;p=sys.stdin.readline;
sys.setrecursionlimit(1000000)
q=int(p())
def T(t, o, s):
    t[s][o]=0
    if o+1 < x and t[s][o+1]==1:
        T(t,o+1,s)
    if o-1>= 0 and t[s][o-1]==1:
        T(t, o-1,s)
    if s -1 >= 0 and t[s-1][o]==1:
        T(t, o,s-1)
    if s +1 < y and t[s+1][o]==1:
        T(t,o,s+1)

for _ in range(q):
    x, y, c = map(int, p().split())
    t = [[0] * x for _ in range(y)]
    for i in range(0,c):
        m,n=map(int,p().split());t[n][m] = 1
    v = 0
    for i in range(0,x):
        for j in range(0, y):
            if t[j][i] == 1:
                T(t, i, j);v+=1
    print(v)

