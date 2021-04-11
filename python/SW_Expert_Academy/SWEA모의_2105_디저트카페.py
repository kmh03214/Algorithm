dx,dy = [-1,1,1,-1 ], [1,1,-1,-1]
def search(start,move):
    check = {start:1}
    x,y = start[0],start[1]
    for i in range(move[0]): # 우상
        x, y = x + dx[0] , y + dy[0]
        if not (0<= x < N and 0<= y < N) or mat[x][y] in memory:
            return
        memory[mat[x][y]] = 1
    for i in range(move[1]): # 우하
        x, y = x + dx[1] , y + dy[1]
        if not(0<= x < N and 0<= y < N) or mat[x][y] in memory:
            return
        memory[mat[x][y]] = 1
    for i in range(move[0]): # 좌하
        x, y = x + dx[2] , y + dy[2]
        if not(0<= x < N and 0<= y < N) or mat[x][y] in memory:
            return
        memory[mat[x][y]] = 1
    for i in range(move[1]-1): # 좌상
        x, y = x + dx[3] , y + dy[3]
        if not (0<= x < N and 0<= y < N) or mat[x][y] in memory:
            return
        memory[mat[x][y]] = 1
    sol.append(len(memory))

T = int(input())
for test in range(1,T+1):
    N = int(input())
    mat = []
    for i in range(N):
        mat.append(list(map(int,input().split())))
    
    sol = []
    for i in range(N):
        for j in range(N):
            # (i,j) -> (i)만큼 우상으로 이동가능 (N-i-1) 만큼 우하로 이동가능.
            # 1,2,3,,,i / 1,2,3 ... N-i-1
            for s1 in range(1,i+1):
                for s2 in range(1, N-i):
                    memory = {mat[i][j]: 1}
                    search((i,j),(s1,s2))
    if sol:
        print('#%d %d'%(test, max(sol)))
    else:
        print('#%d %d'%(test, -1))

