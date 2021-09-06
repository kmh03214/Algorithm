times = [300, 60, 10]
T = int(input())
sol = []
for t in times:
    q, T = T//t, T%t
    sol.append(q)
if T:
    print(-1)
else:
    [print(s, end=' ') for s in sol]

