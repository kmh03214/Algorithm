import sys
read = sys.stdin.readline
N,M,K = map(int,read().split())
mat = [[0 for i in range(N)] for j in range(N)]

fireball = {}
for i in range(M):
    r,c,m,s,d = map(int,read().split())
    mat[r-1][c-1] = [[m,d,s]]
    fireball[(r-1,c-1)] = 1
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

def move_order(fireballs):
    n_fireball, overtwo = {}, {}
    pos = {}
    for ball in fireballs:
        r,c = ball
        for m,d,s in mat[r][c]:
            nr,nc = (r+ (s * dx[d]))%(N), (c + (s*dy[d]))%(N)
            if (nr,nc) not in n_fireball:
                n_fireball[(nr,nc)] = 1
                pos[(nr,nc)] = [[m,d,s]]
            else:
                pos[(nr,nc)].append([m,d,s])
                overtwo[(nr,nc)] = (nr,nc)
        mat[r][c] = 0
    for p in pos:
        mat[p[0]][p[1]] = pos[p]

    return n_fireball, overtwo

def divide(overtwo_):
    n_fireball = {}
    for (r,c) in overtwo_:
        M,D,S,fg = 0,mat[r][c][0][1]%2,0,0
        for (m,d,s) in mat[r][c]:
            M += m
            S += s
            if fg == 0 and D != d%2:
                fg = 1
        M //= 5
        S //= len(mat[r][c])
        if fg == 1:
            D = [1,3,5,7]
        else:
            D = [0,2,4,6]
        
        for i in D:
            if M == 0:
                mat[r][c] = 0
                del fireball[(r,c)]
                break
            nx,ny = r,c
            if (nx,ny) not in n_fireball:
                n_fireball[(nx,ny)] = 1
                mat[nx][ny] = [[M,i,S]]
            else:
                mat[nx][ny].append([M,i,S])
    return n_fireball


for t in range(K):
    fireball, overtwo = move_order(fireball)
    if overtwo: # 나누기 진행
        n_fireball = divide(overtwo)
    else:
        n_fireball = {}
    for x,y in n_fireball:
        if (x,y) not in fireball:
            fireball[(x,y)] = 1

sol = 0
for fire in fireball:
    r,c = fire
    try:
        for arr in mat[r][c]:
            sol += arr[0]
    except:
        continue
print(sol)

# import random
# f = open("test.txt", 'w')
# data = '%d %d %d \n' %(50, 2500,1000)
# f.write(data)
# for i in range(50):
#     for j in range(50):
#         r1,r2,r3 = random.randint(0,999),random.randint(0,999),random.randint(0,7)
#         data = '%d %d %d %d %d \n' %(i+1 ,j+1, r1, r2, r3)
#         f.write(data)
# f.close()