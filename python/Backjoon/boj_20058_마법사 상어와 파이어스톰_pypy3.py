import sys
read = sys.stdin.readline
mat = []
N,Q = map(int,read().split())
for i in range(2**N):
    mat.append(list(map(int, read().split())))
order = list(map(int,read().split()))
N_ = 2**N

def dnq(a,b,c,d,depth):
    if depth == L:
        # 90도 회전
        r_mat = [m[b:d] for m in mat[a:c]]
        r_mat = [list(reversed(i)) for i in zip(*r_mat)]
        return r_mat
    else:
        ind = [(a, b, (a+c)//2, (b+d)//2), (a, (b+d)//2, (a+c)//2, d), ((a+c)//2, b, c, (b+d)//2), ((a+c)//2, (b+d)//2, c, d)]
        for i in range(4):
            x,y,z,w = ind[i]
            ret = dnq(x,y,z,w,depth-1)
            if ret != 'end':
                for i in range(x,z):
                    for j in range(y,w):
                        mat[i][j] = ret[i-x][j-y]
    return 'end'
dx,dy = [1,0,-1,0],[0,1,0,-1]
def melt():
    melt_pos = []
    for i in range(N_):
        for j in range(N_):
            cnt = 0
            for d in range(4):
                nx, ny = i+dx[d], j+dy[d]
                if 0<= nx < N_ and 0<= ny < N_:
                    if mat[nx][ny] > 0:
                        cnt += 1
            if cnt < 3 and mat[i][j] > 0:
                melt_pos.append((i,j))
    for pos in melt_pos:
        mat[pos[0]][pos[1]] -= 1

def bfs(start):
    q = [start]
    ret = 0
    while q:
        Next = []
        for v in q:
            r,c = v[0],v[1]
            for i in range(4):
                nx,ny = r+dx[i], c+dy[i]
                if 0 <= nx < N_ and 0 <= ny < N_ and mat[nx][ny] !=0:
                    mat[nx][ny] = 0
                    Next.append((nx,ny))
                    ret += 1
        q = Next
    return ret

def find_bigice():
    for i in range(N_):
        for j in range(N_):
            if mat[i][j] != 0:
                sol2.append(bfs((i,j)))



for L in order:
    if L != 0:
        dnq(0,0,2**N,2**N,N)
    melt()


sol1,sol2 = 0,[]

for m in mat:
    sol1 += sum(m)
find_bigice()
print(sol1)
print(max(sol2))

