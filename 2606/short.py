n=int(input())+1
c=[[]for i in range(n)]
v=[0]*n
for e in range(int(input())+1):
    x=input()
    print(x)
    a,b=list(map(int,x.split()))
    c[a]+=[b]
    c[b]+=[a]
def d(n):
    if v[n]==0:
        v[n]=1
        for m in c[n]:
            d(m)
d(1)
print(sum(v[2:]))
