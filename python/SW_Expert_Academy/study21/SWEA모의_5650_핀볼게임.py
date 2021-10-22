def game(x,y,d):
    score = 0
    nx,ny = x,y
    while True:
        nx,ny = nx+dd[d][0], ny+dd[d][1]
        if 0<= nx < N and 0 <= ny < N:
            if 1 <= mat[nx][ny] <= 5:
                d = blocks[mat[nx][ny]][d]
                score += 1
            elif 6 <= mat[nx][ny]:
                nx,ny = worm_hole[(nx,ny)]
        else:
            # 반대로 방향 전환
            score += 1
            d = (d+2)%4
            nx,ny = nx + dd[d][0], ny+dd[d][1]
            if 1<= mat[nx][ny] <= 5:
                d = blocks[mat[nx][ny]][d]
                score += 1
            elif 6 <= mat[nx][ny]:
                nx,ny = worm_hole[(nx,ny)]
        if mat[nx][ny] == -1 or (nx,ny) == (x,y):
            return score

T = int(input())

dd = [(0,1),(1,0),(0,-1),(-1,0)]
blocks = {1:[2,0,3,1], 2:[2,3,1,0], 3:[1,3,0,2] , 4:[3,2,0,1] , 5:[2,3,0,1]} # nextdir = blocks[block_num][dir]
for test in range(1,T+1):
    N = int(input())
    mat, trial = [], []
    worm_hole, tmp = {}, {}
    for i in range(N):
        a = list(map(int,input().split()))
        for j in range(N):
            if a[j] == 0:
                trial.append((i,j))
            if 6 <= a[j] <= 10:
                if a[j] not in tmp:
                    tmp[a[j]] = (i,j)
                else:
                    worm_hole[(i,j)] = tmp[a[j]]
                    worm_hole[tmp[a[j]]] = (i,j)
        mat.append(a)
    sol = 0
    for x,y in trial:
        for i in range(4):
            sol = max(sol,game(x,y,i))
    print("#%d %d"%(test, sol))


