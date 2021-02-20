import sys
read = sys.stdin.readline
R,C,T = map(int,read().split())
mat = []
air_cleaner = []
dust = []
for i in range(R):
    a = list(map(int,read().split()))
    for j in range(C):
        if a[j] == -1:
            air_cleaner.append((i,j))
        elif a[j] != 0:
            dust.append((i,j))
    mat.append(a)

def air_clean_up(start):
    r,c = start[0],start[1]
    for i in range(r-1):
        mat[r-i-1][0] = mat[r-i-2][0]
    for i in range(C-1):
        mat[0][i] = mat[0][i+1]
    for i in range(r):
        mat[i][c-1] = mat[i+1][c-1]
    for i in range(C-2):
        mat[r][c-1-i] = mat[r][c-2-i]
    mat[r][1] = 0
def air_clean_down(start):
    r,c = start[0],start[1]
    for i in range(r+1,R-1):
        mat[i][0] = mat[i+1][0]
    for i in range(C-1):
        mat[R-1][i] = mat[R-1][i+1]
    for i in range(R-2,r-1,-1):
        mat[i+1][c-1] = mat[i][c-1]
    for i in range(C-2):
        mat[r][c-1-i] = mat[r][c-2-i]
    mat[r][1] = 0

def bfs(start):
    q = start
    dx,dy = [1,-1,0,0],[0,0,1,-1]
    mat_c = [[0 for i in range(C)] for j in range(R)]
    check = {}
    while q:
        Next = []
        for v in q:
            r,c = v[0],v[1]
            cnt = 0
            if mat[r][c] < 5:
                continue
            for i in range(4):
                nx,ny = r+dx[i],c+dy[i]
                if 0<= nx < R and 0<= ny < C and (nx,ny) not in air_cleaner:
                    mat_c[nx][ny] += mat[r][c] // 5
                    cnt += 1
            mat[r][c] -= (mat[r][c]//5)*cnt
        q = Next

    for i in range(R):
        for j in range(C):
            mat[i][j] += mat_c[i][j]

for i in range(T):
    bfs(dust)
    air_clean_up(air_cleaner[0])
    air_clean_down(air_cleaner[1])
    dust = []
    for r in range(R):
        for c in range(C):
            if mat[r][c] > 4:
                dust.append((r,c))

print(sum([ sum(mat[i]) for i in range(R) ] )+2)


