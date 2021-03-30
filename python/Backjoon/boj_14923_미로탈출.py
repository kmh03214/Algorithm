import sys
read = sys.stdin.readline
N,M = map(int,read().split())
sx,sy = map(int,read().split())
ex,ey = map(int,read().split())
mat = []
for i in range(N):
    mat.append(list(map(int,read().split())))

dx,dy = [1,-1,0,0], [0,0,1,-1]
def bfs(sx,sy):
    check = {(sx,sy,1):0} # magic 이 있는 큐 원소를 따로 관리 0은 없는 원소
    q = [(sx,sy,1)]
    cnt = 1
    while q:
        Next = []
        for v in q:
            x,y,magic = v[0],v[1],v[2]
            if (x,y) == (ex-1,ey-1):
                return check[(x,y,magic)]
            for i in range(4):
                nx,ny = x + dx[i] , y + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    if mat[nx][ny] == 1:
                        if magic and (nx,ny,0) not in check: # 벽인데 magic이 있으면 magic을 쓴다.
                            check[(nx,ny,0)] = cnt
                            Next.append((nx,ny,0))
                    else:
                        if (nx,ny,magic) not in check:
                            check[(nx,ny,magic)] = cnt
                            Next.append((nx,ny,magic))
        q = Next
        cnt += 1
    return -1

print(bfs(sx-1,sy-1))