import sys
read = sys.stdin.readline
N,M = map(int,read().split())
mat = []
for i in range(N):
    mat.append(' '.join(read()).split())

check, sol = {}, {'wolf':0, 'sheep':0}
dd = [(0,1),(1,0),(0,-1),(-1,0)]
def bfs(s):
    q = [s]
    check[s] = 1
    wolf,sheep = 0,0
    while q:
        Next = []
        for v in q:
            if mat[v[0]][v[1]] == 'v':
                wolf += 1
            if mat[v[0]][v[1]] == 'k':
                sheep += 1
            for i in range(4):
                nx, ny = v[0] + dd[i][0], v[1] + dd[i][1]
                if 0 <= nx < N and 0 <= ny < M and (nx,ny) not in check and mat[nx][ny] != '#':
                    
                    check[(nx,ny)] = 1
                    Next.append((nx,ny))
        q = Next
    if wolf < sheep:
        sol['sheep'] += sheep
    else:
        sol['wolf'] += wolf

for i in range(N):
    for j in range(M):
        if (i,j) not in check and mat[i][j] != '#':
            bfs((i,j))

print(sol['sheep'], sol['wolf'])