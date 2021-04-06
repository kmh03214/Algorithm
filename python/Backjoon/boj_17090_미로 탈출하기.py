import sys
read = sys.stdin.readline
N,M = map(int,read().split())
mat = []
for i in range(N):
    mat.append(' '.join(read()).split())

direct = {'D':(1,0),'U':(-1,0),'R':(0,1),'L':(0,-1)}
check = {}
# 500*500 = 250000 * 2
def bfs(start):
    q,history = [start],[start]
    check[start],fg = 1,0
    while q:
        Next = []
        for v in q:
            r,c = v[0],v[1]
            nx,ny = r + direct[mat[r][c]][0], c + direct[mat[r][c]][1]
            if 0 <= nx < N and 0 <= ny < M:
                if (nx,ny) not in check:
                    check[(nx,ny)] = 1
                    Next.append((nx,ny))
                    history.append((nx,ny))
                else:
                    if check[(nx,ny)] == 2:
                        history.append((r,c))
                        fg = 2
            else:
                history.append((r,c))
                fg = 2
        q = Next
    if fg:
        for h in history:
            check[h] = 2

for i in range(N):
    for j in range(M):
        if (i,j) not in check:
            bfs((i,j))
print(sum([1 for ch in check if check[ch]==2]))

