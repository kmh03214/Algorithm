import sys
read = sys.stdin.readline
N,M = map(int,read().split())
mat = []
for i in range(N):
    a = list(map(int,read().split()))
    mat.append(a)

sol_set = []
dx,dy = [1,-1,0,0],[0,0,1,-1]
def dfs(start, depth, check, score):
    if depth == 4:
        sol_set.append(score)
        return
    
    for i in range(4):
        nx,ny = start[0]+dx[i] ,start[1]+dy[i]
        if 0 <= nx < N and 0 <= ny < M and (nx,ny) not in check:
            check[(nx,ny)] = 1
            dfs((nx,ny), depth+1, check, score + mat[nx][ny])
            del check[(nx,ny)]
    return

def fuck_block(start):
    r,c = start
    a = [[(r,c-1),(r,c),(r,c+1),(r+1,c)],
    [(r,c-1),(r,c),(r,c+1),(r-1,c)],
    [(r-1,c),(r,c),(r,c+1),(r+1,c)],
    [(r-1,c),(r,c),(r,c-1),(r+1,c)]]
    for i in range(4):
        score = 0
        for v in a[i]:
            if 0 <= v[0] < N and 0<= v[1] < M:
                score += mat[v[0]][v[1]]
            else:
                break
        if score:
            sol_set.append(score)
            
for i in range(N):
    for j in range(M):
        dfs((i,j), 1, {(i,j):1}, mat[i][j])
        fuck_block((i,j))
print(max(sol_set))