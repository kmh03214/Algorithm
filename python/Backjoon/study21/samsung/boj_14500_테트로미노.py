import sys
read = sys.stdin.readline
N,M = map(int,read().split())
mat = []
for i in range(N):
    mat.append(list(map(int,read().split())))

check, dx,dy, sol, max_val = {}, [1,-1,0,0],[0,0,1,-1],0, max(map(max,mat))
def dfs(s,depth, sol2):
    global sol
    if sol2 + max_val *(4-depth) < sol:
        return
    if depth == 4:
        sol = max(sol,sol2)
        return

    for i in range(4):
        nx,ny = s[0]+dx[i], s[1]+dy[i]
        if 0 <= nx < N and 0 <= ny < M and (nx,ny) not in check:
            check[(nx,ny)] = 1
            if depth == 2:
                dfs(s, depth+1, sol2 + mat[nx][ny])
            dfs((nx,ny), depth+1, sol2 + mat[nx][ny])
            del check[(nx,ny)]
            
for r in range(N):
    for c in range(M):
        check[(r,c)] = 1
        dfs((r,c),1,mat[r][c])
        del check[(r,c)]

print(sol)

# 500 * 500 * 4 = 1000000