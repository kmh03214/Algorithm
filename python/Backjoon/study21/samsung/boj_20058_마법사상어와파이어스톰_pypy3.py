import sys
read = sys.stdin.readline
N, Q = map(int,read().split())
mat = [list(map(int,read().split())) for i in range(2**N)]
level = list(map(int,read().split()))

def divide(sx,sy,n):
    if 2**L == n:
        div_mat = [[mat[sx+i][sy+j] for j in range(n)] for i in range(n)]
        # 회전 / 값 채우기
        for i,m in enumerate(zip(*div_mat)):
            for j,v in enumerate(reversed(m)):
                next_mat[sx+i][sy+j] = v
        return
    else:
        nn = n//2
        [divide(sx+i*nn, sy+j*nn, nn) for i in range(2) for j in range(2)]

def melting(mat):
    check = {}
    for i in range(2**N):
        for j in range(2**N):
            if mat[i][j] == 0:
                continue
            cnt = 0
            for d in [(0,1),(0,-1),(1,0),(-1,0)]:
                nx,ny = i + d[0], j + d[1]
                if 0 <= nx < 2**N and 0 <= ny < 2**N and mat[nx][ny] > 0:
                    cnt += 1
            if cnt < 3:
                check[(i,j)] = 1
    for c in check:
        mat[c[0]][c[1]] -= 1
    return mat

def bfs(s):
    q, cnt = [s] ,1
    while q:
        Next = []
        for v in q:
            for d in [(0,1),(1,0),(0,-1),(-1,0)]:
                nx,ny = v[0]+d[0],v[1]+d[1]
                if 0 <= nx < 2**N and 0 <= ny < 2**N and (nx,ny) not in check and mat[nx][ny] != 0:
                    Next.append((nx,ny))
                    check[(nx,ny)] = 1
                    cnt += 1
        q = Next
    return cnt

for L in level:
    next_mat = [[0 for i in range(2**N)] for j in range(2**N)]
    if L:
        divide(0,0,2**N)
    else:
        next_mat = mat
    
    mat = melting(next_mat)
    
sol1,sol2,check = 0,0,{}
for i in range(2**N):
    for j in range(2**N):
        sol1 += mat[i][j]
        if mat[i][j] != 0 and (i,j) not in check:
            check[(i,j)] = 1
            sol2 = max(sol2, bfs((i,j)))
print(sol1)
print(sol2)


