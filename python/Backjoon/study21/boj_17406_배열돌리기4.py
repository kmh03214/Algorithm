
import sys
from itertools import permutations

dd = [(0,1),(1,0),(0,-1),(-1,0)]
def rotation(r,c,s):
    for z in range(s):
        for i in range(1, 2*(s-z)+1):
            mat_[r-s+z][c-s+z], mat_[r-s+z][c-s+z+i] = mat_[r-s+z][c-s+z+i], mat_[r-s+z][c-s+z]
        for i in range(1, 2*(s-z)+1):
            mat_[r-s+z][c-s+z], mat_[r-s+z+i][c+s-z] = mat_[r-s+z+i][c+s-z], mat_[r-s+z][c-s+z]
        for i in range(1, 2*(s-z)+1):
            mat_[r-s+z][c-s+z], mat_[r+s-z][c+s-z-i] = mat_[r+s-z][c+s-z-i], mat_[r-s+z][c-s+z]
        for i in range(1, 2*(s-z)+1):
            mat_[r-s+z][c-s+z], mat_[r+s-z-i][c-s+z] = mat_[r+s-z-i][c-s+z], mat_[r-s+z][c-s+z]

read = sys.stdin.readline
N,M,K = map(int,read().split())
mat = [list(map(int,read().split())) for i in range(N)]
orders = [list(map(int,read().split())) for i in range(K)]

sol = float('inf')
for per in permutations(orders):
    mat_ = [m.copy() for m in mat]
    for r,c,s in per:
        rotation(r-1,c-1,s)
    sol = min(sol, min([sum(m) for m in mat_]))
print(sol)

# def rotation(mat,r,c,z):
#     # 1,8,16,24 -> ((z-1)*2)*4
#     dxy = [(0,1),(1,0),(0,-1),(-1,0)]
#     for zi in range(z+1):
#         x,y = r-(zi),c-(zi)
#         for j in range(4):
#             for i in range(2*(zi)):
#                 nx,ny = x + dxy[j][0], y + dxy[j][1]
#                 mat[nx][ny], mat[r-(zi)][c-(zi)] = mat[r-(zi)][c-(zi)], mat[nx][ny]
#                 x, y = nx, ny
#     return mat