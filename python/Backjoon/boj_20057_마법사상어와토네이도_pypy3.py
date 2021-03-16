import sys
read = sys.stdin.readline
N = int(read())
mat = []
for i in range(N):
    mat.append(list(map(int,read().split())))

def rotation_90(m):
    return [list(reversed(i)) for i in zip(*m)]
blow = [[0,0,2,0,0],
[0,10,7,1,0],
[5,0,0,0,0],
[0,10,7,1,0],
[0,0,2,0,0]]

blows = {0:blow}
for i in range(3):
    blow = rotation_90(blow)
    blows[3-i] = blow
direction = []
for k in range(3,3+(N//2)):
    direction.extend([0] + [1]*(2*(k-2)-1) + [2]*(2*(k-2)) + [3]*(2*(k-2)) + [0]*(2*(k-2)))

dx, dy = [0,1,0,-1], [-1,0,1,0]
r,c = N//2, N//2
sol = 0
for d in direction:
    blow = blows[d]
    nr , nc = r + dx[d], c + dy[d]
    total_sand, total_spread_sand,out_sand, mat[nr][nc] = mat[nr][nc], 0, 0, 0
    if total_sand == 0:
        r,c = nr,nc
        continue
    for i in range(5):
        for j in range(5):
            spread_sand = int(total_sand * blow[i][j]/100)
            if 0 <= nr-2+i < N and 0 <= nc-2+j < N:
                mat[nr-2+i][nc-2+j] += spread_sand
                total_spread_sand += spread_sand
            else:
                out_sand += spread_sand
    ar,ac = nr + dx[d], nc + dy[d]
    if 0 <= ar < N and 0 <= ac < N:
        mat[ar][ac] += (total_sand - total_spread_sand - out_sand)
    else:
        out_sand += (total_sand - total_spread_sand - out_sand)
    r,c = nr,nc
    sol += out_sand
print(sol)