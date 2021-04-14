dx,dy = [1,-1,0,0],[0,0,1,-1]

def bfs(start):
    q = [start]
    check = {start:0}
    while q:
        Next = set()
        for v in q:
            x,y = v[0],v[1]
            for i in range(4):
                nx,ny = x+dx[i], y + dy[i]
                if 0<= nx < N and 0 <= ny < N:
                    if (nx,ny) not in check:
                        check[(nx,ny)] = mat[nx][ny]+check[(x,y)]
                        Next.add((nx,ny))
                    else:
                        if mat[nx][ny] + check[(x,y)] < check[(nx,ny)]:
                            check[(nx,ny)] = mat[nx][ny] + check[(x,y)]
                            Next.add((nx,ny))
        q = list(Next)
    return check[(0,0)]


T = int(input())
for test in range(1,T+1):
    N = int(input())
    mat = []
    for i in range(N):
        mat.append( list(map(int, ' '.join(input()).split())) )
    # start = (0,0), end = (N-1,N-1)
    print("#%d %d"%(test, bfs((N-1,N-1))))

    
