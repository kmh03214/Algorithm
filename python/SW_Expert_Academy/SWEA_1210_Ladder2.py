N = 100
dx,dy = [0,0,-1],[1,-1,0] # 우좌상
def bfs(start):
    q = [start]
    check = {start:1}
    while q:
        Next = []
        for v in q:
            x,y = v[0],v[1]
            if x == 0:
                return y
            for i in range(3):
                nx,ny = x+dx[i],y+dy[i]
                if 0<= nx < N and 0 <= ny < N and (nx,ny) not in check and mat[nx][ny] == 1:
                    check[(nx,ny)] = 1
                    Next.append((nx,ny))
                    break
        q = Next

T = 10
for test in range(1,T+1):
    num = int(input())
    sol,mat = 0,[]
    for i in range(N):
        mat.append(list(map(int,input().split())))
    px,py = N-1, mat[-1].index(2) # 목적지
    print(bfs((px,py)))


    # print("#%d %d"%(test,sol))