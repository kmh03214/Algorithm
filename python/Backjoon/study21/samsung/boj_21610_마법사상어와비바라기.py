import sys
read = sys.stdin.readline

N,M = map(int,read().split())
mat = [list(map(int,read().split())) for i in range(N)]
orders = [list(map(int,read().split())) for i in range(M)]

cloud = [(N-1,0),(N-1,1),(N-2,0),(N-2,1)]
d = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)] # 대각선 1,3,5,7

for o in orders:
    bug = {}
    for v in cloud:
        nx,ny = (v[0] + o[1]*d[o[0]-1][0])%N, (v[1] + o[1]*d[o[0]-1][1])%N
        mat[nx][ny] += 1
        bug[(nx,ny)] = 1
    
    for b in bug:
        cnt = 0
        for dd in [d[2*i+1] for i in range(4)]:
            nx, ny = b[0] + dd[0], b[1] + dd[1]
            if 0 <= nx < N and 0 <= ny < N and mat[nx][ny] > 0:
                cnt += 1
        mat[b[0]][b[1]] += cnt

    next_cloud = []
    for i in range(N):
        for j in range(N):
            if (i,j) not in bug and mat[i][j] >= 2:
                mat[i][j] -= 2
                next_cloud.append((i,j))
    cloud = next_cloud
print(sum([sum(m) for m in mat]))
