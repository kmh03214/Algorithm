import sys
read = sys.stdin.readline
R,C,M = map(int,read().split())
mat = []
sharks = {}
for i in range(M):
    r,c,s,d,z = map(int,read().split())
    sharks[(r-1,c-1)] = (s,d-1,z)

dd = [(-1,0),(1,0),(0,1),(0,-1)] # 위 아래 오른 왼
reverse_d = {0:1,1:0,2:3,3:2}
def move(r,c,d,s):
    if d <= 1:
        s %= (2*(R-1))
    else:
        s %= (2*(C-1))
    
    for i in range(s):
        r,c = r+dd[d][0], c+dd[d][1]
        if not (0<= r < R and 0 <= c < C):
            d = reverse_d[d]
            r,c = r+2*dd[d][0], c+2*dd[d][1]
    return r,c,d

sol = 0
for c in range(C):
    for r in range(R):
        if (r,c) in sharks:
            sol += sharks[(r,c)][2]
            del sharks[(r,c)]
            break
    Next = {}
    for shark in sharks:
        r,c = shark
        s,d,z = sharks[shark]
        nr,nc,nd = move(r,c,d,s)
        if (nr,nc) not in Next:
            Next[(nr,nc)] = (s,nd,z)
        else:
            if Next[(nr,nc)][2] < z:
                Next[(nr,nc)] = (s,nd,z)
    sharks = Next
print(sol)