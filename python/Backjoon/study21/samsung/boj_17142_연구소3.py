import sys
from itertools import combinations
read = sys.stdin.readline
N,M = map(int,read().split())
virus_pos, mat = [], []
for i in range(N):
    a = list(map(int,read().split()))
    for j in range(N):
        if a[j] == 2:
            virus_pos.append((i,j))
    mat.append(a)

def bfs(start, mat = [m.copy() for m in mat]):
    q, check, time, ret = start, {s:1 for s in start}, 0, 1
    while q:
        Next,fg = [],0
        for v in q:
            for d in [(0,1),(1,0),(0,-1),(-1,0)]:
                nx,ny = v[0] + d[0] , v[1] + d[1]
                if 0 <= nx < N and 0 <= ny < N and mat[nx][ny] != 1 and (nx,ny) not in check:
                    if not fg and mat[nx][ny] == 0:
                        fg = 1
                    check[(nx,ny)] = 1
                    Next.append((nx,ny))

        if not Next:
            if len(check) != zero_cnt + len(virus_pos):
                return 0
            return time

        q = Next
        if fg:
            time += ret
            ret = 1
        else:
            ret += 1

zero_cnt, sol = sum([m.count(0) for m in mat]), []
if zero_cnt:
    for combi in combinations(virus_pos,M):
        s = bfs(combi)
        if s:
            sol.append(s)
    if sol:
        print(min(sol))
    else:
        print(-1)
else:
    print(0)

# 5 1
# 2 2 2 1 1
# 2 1 1 1 1
# 0 1 1 1 1
# 2 1 1 1 1
# 2 2 2 1 1

# 5 1
# 2 1 1 1 1
# 2 1 1 1 1
# 0 1 1 1 1
# 2 1 1 1 1
# 0 1 1 1 1