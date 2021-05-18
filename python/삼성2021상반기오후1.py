# 출처 
# https://leebroscode.com/missions/2/frequent-problems/tree-tycoon/description

N,M = map(int,input().split())
mat = []
for i in range(N):
    mat.append(list(map(int,input().split())))
winds = []
clouds = [(N-2,0),(N-2,1),(N-1,0),(N-1,1)]
for i in range(M):
    winds.append(list(map(int,input().split())))
dd = { 1: (0,1), 2: (-1,1),3: (-1,0) , 4: (-1,-1) , 5:(0,-1) , 6: (1,-1) ,7: (1,0) ,8:(1,1)}
dx,dy = [-1,1,1,-1],[-1,-1,1,1]
for wind in winds:
    d,power = wind
    tmp = {}
    for cloud in clouds:
        r,c = cloud
        nr,nc = (r + power*dd[d][0])%N, (c + power*dd[d][1])%N
        mat[nr][nc] += 1
        tmp[(nr,nc)] = 1
    for key in tmp:
        r,c = key
        for i in range(4):
            nr,nc = r+dx[i],c+dy[i]
            if 0<=nr < N and 0 <=nc < N and mat[nr][nc] >= 1:
                mat[r][c] += 1
    next_clouds = []
    for i in range(N):
        for j in range(N):
            if (i,j) not in tmp and mat[i][j] >= 2:
                mat[i][j] -= 2
                next_clouds.append((i,j))
    clouds = next_clouds
s = 0
for i in range(N):
    for j in range(N):
        s += mat[i][j]
print(s)