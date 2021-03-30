import sys
read = sys.stdin.readline
N,M = map(int,read().split())
mat,sheeps,wolves = [],[],[]
for i in range(N):
    a = ' '.join(read()).split()
    for j in range(M):
        if a[j] == 'S':
            sheeps.append((i,j))
        if a[j] == 'W':
            wolves.append((i,j))
    mat.append(a)
dx,dy = [1,-1,0,0],[0,0,1,-1]
def bfs_1(sheeps): # 울타리치기
    for v in sheeps:
        for i in range(4):
            nx,ny = v[0]+dx[i], v[1]+dy[i]
            if 0<= nx < N and 0 <= ny < M and mat[nx][ny] == '.':
                mat[nx][ny] = 'D'

def bfs(start):
    q = [s for s in start]
    check = {s:1 for s in start}
    while q:
        Next = []
        for v in q:
            x,y = v[0],v[1]
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and mat[nx][ny] == 'S':
                    return 0
                if 0 <= nx < N and 0<= ny < M and (nx,ny) not in check and mat[nx][ny] == '.':
                    Next.append((nx,ny))
                    check[(nx,ny)] = 1
        q = Next
    return 1
bfs_1(sheeps)
ret = bfs(wolves)
if ret:
    print(ret)
    for m in mat:
        print(''.join(m))
else:
    print(ret)