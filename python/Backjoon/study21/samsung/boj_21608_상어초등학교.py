import sys
read = sys.stdin.readline
N = int(read())
order,likes = [],{}
mat = [[0 for i in range(N)] for j in range(N)]

for i in range(N**2):
    n,a,b,c,d = map(int,read().split())
    order.append(n)
    likes[n] = [a,b,c,d]

def sit(n):
    like = {l:1 for l in likes[n]}
    tmp = {}
    for i in range(N):
        for j in range(N):
            if mat[i][j] != 0:
                continue
            cnt,vac = 0,0
            for d in [(0,1),(1,0),(0,-1),(-1,0)]:
                nx,ny = i+d[0], j+d[1]
                if 0<=nx < N and 0<=ny < N:
                    if mat[nx][ny] in like:
                        cnt += 1
                    if mat[nx][ny] == 0:
                        vac += 1
            if cnt not in tmp:
                tmp[cnt] = [(i,j,vac)]
            else:
                tmp[cnt].append((i,j,vac))
    M = max(tmp)
    tmp2 = tmp[M]
    if len(tmp2) > 1:
        tmp2.sort(key = lambda x : (x[2],-x[0],-x[1]), reverse = True)
        return (tmp2[0][0],tmp2[0][1])
    else:
        return (tmp2[0][0],tmp2[0][1])

for num in order:
    sx,sy = sit(num)
    mat[sx][sy] = num

sol = 0
score = {0:0,1:1,2:10,3:100,4:1000}
for i in range(N):
    for j in range(N):
        num = mat[i][j]
        cnt,like = 0, {l:1 for l in likes[num]}
        for d in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx,ny = i+d[0], j+d[1]
            if 0<=nx < N and 0<=ny < N:
                if mat[nx][ny] in like:
                    cnt += 1
        sol += score[cnt]
print(sol)
