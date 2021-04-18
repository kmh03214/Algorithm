dx,dy = [1,-1,0,0],[0,0,1,-1]
def bfs(start):
    q,s = [start],0
    check = {start:1}
    while q:
        Next = []
        for v in q:
            x,y = v[0],v[1]
            for i in range(4):
                nx,ny = x+dx[i], y+dy[i]
                if 0<=nx < N and 0 <= ny < N and (nx,ny) not in check and mat[nx][ny] == mat[x][y]+1:
                    check[(nx,ny)]= 1
                    Next.append((nx,ny))
                    s += 1
        q = Next
    return s

T = int(input())
for test in range(1,T+1):
    sol = []
    N = int(input())
    mat = []
    for i in range(N):
        mat.append(list(map(int,input().split())))
    
    for i in range(N):
        for j in range(N):
            v,s = mat[i][j], bfs((i,j))
            if not sol:
                sol.append((v,s))
            else:
                if sol[0][1] < s:
                    sol = [(v,s)]
                elif sol[0][1] == s:
                    sol.append((v,s))
    ss = min(sol)
    print("#%d %d %d"%(test, ss[0], ss[1]+1 ))

