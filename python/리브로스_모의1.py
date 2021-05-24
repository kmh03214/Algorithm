import sys
from itertools import combinations
read = sys.stdin.readline
N = int(read())
mat = []
start,end = 0,0
coin_pos,coin = {}, []
for i in range(N):
    a = ' '.join(read()).split()
    for j in range(N):
        if a[j] == 'S':
            start = (i,j)
        if a[j] == 'E':
            end = (i,j)
        if a[j] in '123456789':
            coin.append(a[j])
            coin_pos[a[j]] = (i,j)
    mat.append(a)
dx,dy = [1,-1,0,0],[0,0,1,-1]
def bfs(start,target):
    q = [start]
    check = {start:1}
    cnt = 0
    while q:
        Next = []
        for v in q:
            if v == target:
                return cnt
            r,c = v[0],v[1]
            for i in range(4):
                nr,nc = r+dx[i],c+dy[i]
                if 0<= nr < N and 0 <= nc < N and (nr,nc) not in check and mat[nr][nc] != '#':
                    Next.append((nr,nc))
                    check[(nr,nc)] = 1
        q = Next
        cnt += 1
    return -1

coin.sort()
sol =[]
start_cp = start
for combi in combinations(coin,3):
    target_pos = [coin_pos[c] for c in combi] + [end] # 거쳐갈 좌표
    s,fg = 0,0
    start = start_cp
    for target in target_pos:
        ret = bfs(start,target)
        if ret == -1:
            fg = 1
            break # 해당 경로 실패
        else:
            start = target
            s += ret
    if fg == 0:
        sol.append(s)
if sol:
    print(min(sol))
else:
    print(-1)