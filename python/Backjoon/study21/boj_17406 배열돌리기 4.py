import sys
from itertools import permutations
read = sys.stdin.readline

N,M,K = map(int,read().split())
arr = []
for i in range(N):
    arr.append(list(map(int,read().split())))

oper = [list(map(int,read().split())) for i in range(K)]

def rotation(mat,r,c,z):
    # 1,8,16,24 -> ((z-1)*2)*4
    dxy = [(0,1),(1,0),(0,-1),(-1,0)]
    for zi in range(z+1):
        x,y = r-(zi),c-(zi)
        for j in range(4):
            for i in range(2*(zi)):
                nx,ny = x + dxy[j][0], y + dxy[j][1]
                mat[nx][ny], mat[r-(zi)][c-(zi)] = mat[r-(zi)][c-(zi)], mat[nx][ny]
                x, y = nx, ny
    return mat
sol = 100*50*50
for per in permutations(oper,len(oper)):
    mat = []
    for i in arr:
        mat.append(i.copy())

    for t in per:
        mat = rotation(mat,t[0]-1,t[1]-1,t[2])

    for i in mat:
        sol = min(sol,sum(i))
print(sol)


# def dfs(mat,depth):
    
#     if depth == K:
#         return

