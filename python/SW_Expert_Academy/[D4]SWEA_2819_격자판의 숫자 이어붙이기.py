def dfs(r,c,string):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    if len(string) == 7:
        sol.add(string)
        return

    for i in range(4):
        nx, ny = r + dx[i], c + dy[i]

        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx,ny,string+str(mat[nx][ny]))

T = int(input())
for test in range(T):
    sol = set()
    mat = []
    for i in range(4):
        mat.append(list(map(int,input().split())))
    
    for i in range(4):
        for j in range(4):
            dfs(i,j,str(mat[i][j]))
    
    print("#%d"%(test+1),len(sol))


