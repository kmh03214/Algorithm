import sys
read = sys.stdin.readline
N = int(read())

dd = [(1,0),(0,-1),(-1,0),(0,1)]

def direction(d,g):
    dirs = [d]
    for i in range(g):
        for j in range(len(dirs)-1,-1,-1):
            dirs.append((dirs[j]+1)%4)
    return dirs

mat = [[0 for i in range(101)] for j in range(101)]
def dragon_curve(x,y,dirs):
    mat[x][y] = 1
    for d in dirs:
        x,y = x+dd[d][0],y+dd[d][1]
        mat[x][y] = 1
for i in range(N):
    x,y,d,g = map(int,read().split())
    dragon_curve(x,y,direction(d,g))

sol = 0
for i in range(100):
    for j in range(100):
        if mat[i][j] and mat[i+1][j] and mat[i][j+1] and mat[i+1][j+1]:
            sol += 1
print(sol)
