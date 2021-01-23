n = list(map(int, [*open(0)][1:]))
count = [0] * 8001
most_common = 0
lst = []
for i in n:
    count[i + 4000] += 1
    if count[i + 4000] > most_common:
        most_common = count[i + 4000]
        lst = [i]
    elif count[i + 4000] == most_common:
        lst.append(i)
lst.sort()
n.sort()
print(f'{round(sum(n)/len(n))}\n{n[len(n)//2]}\n{lst[1] if len(lst) > 1 else lst[0]}\n{max(n)-min(n)}')
