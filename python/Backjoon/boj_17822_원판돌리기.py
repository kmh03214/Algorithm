import sys
read = sys.stdin.readline

N,M,T = map(int,read().split())

mat = []
orders = []
for i in range(N):
    mat.append(list(map(int,read().split())))

for i in range(T):
    orders.append(list(map(int,read().split()))) # 배수만큼,방향,몇 칸

def rotation(x,d,k):
    if d == 0: # ->
        for i in range(1,N+1):
            row_idx = x*i-1
            if row_idx > N-1:
                break
            mat[row_idx] = mat[row_idx][M-k:] + mat[row_idx][:M-k]
    else:
        for i in range(1,N+1):
            row_idx = x*i-1
            if row_idx > N-1:
                break
            mat[row_idx] = mat[row_idx][k:] + mat[row_idx][:k]

def find_same_neighbor(start):
    q = [start]
    delete = []
    dx,dy = [1,-1,0,0],[0,0,1,-1]
    num = mat[start[0]][start[1]]
    while q:
        Next = []
        for v in q:
            r,c = v[0],v[1]
            for i in range(4):
                nx,ny = r+dx[i],c+dy[i]
                if ny == M:
                    ny = 0
                if ny == -1:
                    ny = M-1
                if 0 <= nx < N and 0 <= ny < M and (nx,ny) not in check and mat[nx][ny] == num:
                    check[(nx,ny)] = 1
                    Next.append((nx,ny))
                    if len(delete) == 0:
                        delete.append((r,c))
                    delete.append((nx,ny))
        q = Next
    
    return delete



for order in orders:
    x,d,k = order[0],order[1],order[2]
    rotation(x,d,k)

    check = {}
    deletes = []
    for i in range(N):
        for j in range(M):
            if (i,j) not in check and mat[i][j] != 0:
                check[(i,j)] = 1
                deletes += find_same_neighbor((i,j))
    if deletes:
        for delete in deletes:
            mat[delete[0]][delete[1]] = 0
    else:
        total,cnt = 0,0
        for i in range(N):
            for j in range(M):
                if mat[i][j] != 0:
                    total += mat[i][j]
                    cnt += 1
        if cnt == 0:
            continue
        mean = total/cnt
        for i in range(N):
            for j in range(M):
                if mat[i][j] == 0:
                    continue
                if mat[i][j] > mean:
                    mat[i][j] -= 1
                elif mat[i][j] < mean:
                    mat[i][j] += 1

print(sum([sum(i) for i in mat]))
                

