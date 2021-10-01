import sys
read = sys.stdin.readline
N,L,R = map(int,read().split())
mat = [list(map(int,read().split())) for i in range(N)]

dd = [(0,1),(1,0),(0,-1),(-1,0)]
def bfs(s):
    q, cal, Sum = [s], [s], mat[s[0]][s[1]]
    while q:
        Next = []
        for v in q:
            for i in range(4):
                nx,ny = v[0] + dd[i][0], v[1] + dd[i][1]
                if 0 <= nx < N and 0 <= ny < N and L <= abs(mat[v[0]][v[1]] - mat[nx][ny]) <= R and (nx,ny) not in check:
                    check[(nx,ny)] = 1
                    Next.append((nx,ny))
                    cal.append((nx,ny))
                    Sum += mat[nx][ny]
        q = Next
    avg = Sum//len(cal)
    if len(cal) != 1:
        for c in cal:
            mat[c[0]][c[1]] = avg
        return 1
    else:
        return 0
sol = 0
while 1:
    check = {}
    fg = 0
    for i in range(N):
        for j in range(N):
            if (i,j) not in check:
                check[(i,j)] = 1
                ret = bfs((i,j))
                if ret:
                    fg = 1
    if not fg:
        break
    sol+=1
print(sol)