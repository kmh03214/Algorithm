import sys
read = sys.stdin.readline
N,M = map(int,read().split())
mat = []
for i in range(N):
    a = list(map(int,read().split()))
    mat.append(a)

sol_set = []
dx,dy = [1,-1,0,0],[0,0,1,-1]
max_val = max(map(max, mat))
ans = 0
def dfs(start, depth, check, score):
    global ans
    if score + max_val * (4 - depth) < ans:
        return

    if depth == 4:
        ans = max(ans,score)
        return
    
    for i in range(4):
        nx,ny = start[0]+dx[i] ,start[1]+dy[i]
        if 0 <= nx < N and 0 <= ny < M and (nx,ny) not in check:
            check[(nx,ny)] = 1
            dfs((nx,ny), depth+1, check, score + mat[nx][ny])
            del check[(nx,ny)]
    return

def fuck_block(start):
    global ans
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
            ans = max(ans,score)
            
for i in range(N):
    for j in range(M):
        dfs((i,j), 1, {(i,j):1}, mat[i][j])
        fuck_block((i,j))
print(ans)