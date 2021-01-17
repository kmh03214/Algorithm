import sys
read = sys.stdin.readline
N,M = map(int,read().split())
mat = []
for i in range(N):
    a = list(map(int,read().split()))
    mat.append(a)

dx,dy = [1,-1,0,0],[0,0,1,-1]
visited = [[False for _ in range(M)] for _ in range(N)]
max_val = max(map(max, mat))

def dfs(start, depth, score):
    global ans
    if score + max_val * (4 - depth) < ans:
        return
    if depth == 4:
        ans = max(ans, score)
        return
    
    for i in range(4):
        nx,ny = start[0]+dx[i] ,start[1]+dy[i]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False:
            visited[nx][ny] = True
            if depth == 2:
                dfs((start[0], start[1]), depth + 1, score + mat[nx][ny])
            dfs((nx,ny), depth+1, score + mat[nx][ny])
            visited[nx][ny] = False
    return

ans = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs((i,j), 1, mat[i][j])
        visited[i][j] = False
print(ans)