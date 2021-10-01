import sys
from itertools import combinations

read = sys.stdin.readline
N, M = map(int, read().split())
mat, houses, chikens = [], [], []
for i in range(N):
    a = list(map(int,read().split()))
    for j in range(N):
        if a[j] == 1:
            houses.append((i,j))
        if a[j] == 2:
            chikens.append((i,j))

# M개 고르기.
sol = []
for combi in combinations(chikens,M):
    s = []
    for h in houses:
        s.append(min([abs(h[0] - c[0])+abs(h[1] - c[1]) for c in combi]))
    sol.append(sum(s))
print(min(sol))