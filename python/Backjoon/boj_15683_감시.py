import sys
import itertools
read = sys.stdin.readline

N,M = map(int,read().split())
mat,cctv,prod = [],[],[]
for i in range(N):
    a = list(map(int,read().split()))
    for j in range(M):
        if a[j] in [1,2,3,4,5]:
            if a[j] == 1 or a[j] == 3 or a[j] == 4:
                prod.append([0,1,2,3])
            elif a[j] == 2:
                prod.append([0,1])
            else:
                prod.append([0])
            cctv.append((i,j,a[j]))
    mat.append(a)

def direct(cctv_num,d_idx):
    if cctv_num == 1:
        return [d_idx]
    elif cctv_num == 2:
        return [d_idx%4,(d_idx+2)%4]
    elif cctv_num == 3:
        return [d_idx%4,(d_idx+1)%4]
    elif cctv_num == 4:
        return [d_idx%4, (d_idx+1)%4, (d_idx+2)%4]
    else:
        return [d_idx%4, (d_idx+1)%4, (d_idx+2)%4, (d_idx+3)%4]

def gamsi(pos, ds):
    dx = [-1,0,1,0] # 북 동 남 서
    dy = [0,1,0,-1]
    for d in ds:
        q = [pos]
        while q:
            Next = []
            for v in q:
                nx,ny = v[0] + dx[d], v[1] + dy[d]
                if 0 <= nx < N and 0 <= ny < M and mat_c[nx][ny] != 6:
                    Next = [(nx,ny)]
                    mat_c[nx][ny] = '#'
            q = Next
sol = []
for p in itertools.product([0,1,2,3],repeat=len(cctv)):
    mat_c = []
    for m in mat:
        mat_c.append(m.copy())
    
    for i in range(len(p)):
        cctv_pos = (cctv[i][0],cctv[i][1])
        directions = direct(mat[cctv_pos[0]][cctv_pos[1]],p[i])
        gamsi( cctv_pos , directions)
    s = 0
    for mm in mat_c:
        s += mm.count(0)
    sol.append(s)

print(min(sol))










