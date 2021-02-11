import sys
read = sys.stdin.readline
N,L,R = map(int,read().split())
mat,unions = [],[]
for i in range(N):
    a = list(map(int,read().split()))
    mat.append(a)

def bfs():
    flag = 0
    Max = N*N
    chk_arr = [[False for i in range(N)] for j in range(N)]

    for i in range(N):
        for j in range(N):
            if chk_arr[i][j] == False:
                chk_arr[i][j] = True
                q = [(i,j)]
                dx,dy = [1,-1,0,0], [0,0,1,-1]

                union = [(i,j)]
                total_human = mat[i][j]

                while q:
                    Next = []
                    for v in q:
                        r,c = v
                        for d in range(4):
                            nx,ny = r + dx[d], c + dy[d]
                            if 0 <= nx < N and 0<= ny < N and chk_arr[nx][ny] == False and L <= abs(mat[r][c]-mat[nx][ny]) <= R:
                                chk_arr[nx][ny] = True
                                Next.append((nx,ny))
                                union.append((nx,ny))
                                total_human += mat[nx][ny]

                    q = Next
                if len(union) > 1:
                    flag = 1
                    unions.append(union)
    return flag

sol = 0
flag = 1
while bfs():
    sol+=1
    for union in unions:
        human_per_union = sum([mat[i[0]][i[1]] for i in union]) // len(union)
        for u in union:
            mat[u[0]][u[1]] = human_per_union
    unions = []
print(sol)
