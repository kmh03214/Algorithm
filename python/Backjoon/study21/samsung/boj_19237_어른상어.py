import sys
read = sys.stdin.readline
N,M,K = map(int,read().split())
dd = {1:(-1,0),2:(1,0),3:(0,-1),4:(0,1)}
mat, sharks, priority, smell = [], {}, {}, {}

for i in range(N):
    a = list(map(int,read().split()))
    mat.append(a)
    for j in range(N):
        if a[j] != 0:
            sharks[a[j]] = [i,j]
            smell[(i,j)] = [a[j],K]
            mat[i][j] = a[j]
for num,d in enumerate(map(int,read().split())):
    sharks[num+1].append(d)

for i in range(M):
    priority[i+1] = {}
    for j in range(4):
        priority[i+1][j+1] = list(map(int,read().split()))

def move_shark(r,c,d,num):
    pd, ret = priority[num][d], 0
    for d in pd:
        nx,ny = r + dd[d][0], c+ dd[d][1]
        if 0 <= nx < N and 0 <= ny < N:
            if (nx,ny) not in smell:
                return (nx,ny,d)
            elif ret == 0 and smell[(nx,ny)][0] == num:
                ret = (nx,ny,d)
    return ret

print(1)
time = 0
while time < 1000:
    next_shark = {}
    next_mat = [[0 for i in range(N)] for j in range(N)]
    next_smell = {}

    for num in sharks:
        r,c,d = sharks[num]
        nr,nc,nd = move_shark(r,c,d,num)
        if not next_mat[nr][nc]:
            next_mat[nr][nc] = num
        elif next_mat[nr][nc] > num:
            del next_shark[next_mat[nr][nc]]
            next_mat[nr][nc] = num
        
        next_shark[num] = [nr,nc,nd]
        next_smell[(nr,nc)] = [num,K+1]
    
    for ns in next_smell:
        smell[ns] = next_smell[ns]

    for sm in smell:
        smell[sm][1] -= 1
        if smell[sm][0] == 0:
            del smell[sm]
    sharks = next_shark
    mat = next_mat
    tmp = [[[0,0] for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            if (i,j) in smell:
                tmp[i][j] = smell[(i,j)]

    time += 1
    