import sys
read = sys.stdin.readline
N = int(read())
mat = [list(map(int,read().split())) for i in range(N)]

s = N//2,N//2

# 1,1 / 2,2 / 3,3 / 4,4 / 5,5 / 6,6 / 7
# 0,1,2,3 왼 아래 오른 위
dd, d, D =[], 0, [(0,-1),(1,0),(0,1),(-1,0)]

for i in range(N-1):
    for j in range(2*i+2):
        if j == (2*i+2)//2:
            d+=1
        dd.append(d%4)
    d+=1
dd += [(dd[-1]+1)%4]*(i+1)
mask = [[0,0,2,0,0],[0,10,7,1,0],[5,0,0,0,0],[0,10,7,1,0],[0,0,2,0,0]]
masks = {0:mask}
for i in range(3):
    masks[3-i] = [list(reversed(m)) for m in zip(*masks[(-i)%4])]

out = 0
for d in dd:
    s = s[0] + D[d][0], s[1] + D[d][1]
    alpha = s[0] + D[d][0], s[1] + D[d][1]
    
    msk, sand, mat[s[0]][s[1]], spread = masks[d], mat[s[0]][s[1]], 0, 0
    
    for i in range(-2,3):
        for j in range(-2,3):
            x,y = s[0]+i,s[1]+j
            add = int(sand * (msk[i+2][j+2]/100))
            if 0 <= x < N and 0 <= y < N:
                mat[x][y] += add
            else:
                out += add
            spread += add
    if 0 <= alpha[0] < N and 0 <= alpha[1] < N:
        mat[alpha[0]][alpha[1]] += (sand-spread)
    else:
        out += (sand-spread)
print(out)
