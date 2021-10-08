import sys
read = sys.stdin.readline
N = int(read())
mat = [list(map(int,read().split())) for i in range(N)]

dd = [(1,-1),(1,1),(-1,1),(-1,-1)]
def make(x,y,d1,d2):
    m = [[6 for i in range(N)] for j in range(N)]
    m[x][y] = 0

    for i in range(d1):
        x,y = x+dd[0][0], y+dd[0][1]
        m[x][y] = 0
    for i in range(d2):
        x,y = x+dd[1][0], y+dd[1][1]
        m[x][y] = 0
    
    for i in range(d1):
        x,y = x+dd[2][0], y+dd[2][1]
        m[x][y] = 0
    
    for i in range(d2):
        x,y = x+dd[3][0], y+dd[3][1]
        m[x][y] = 0
    return m

sol = 10000000000000000
for r in range(N):
    for c in range(N):
        for d1 in range(1,N):
            for d2 in range(1,N):
                pop = {1:0,2:0,3:0,4:0,0:0}
                if 0<= r < r+d1+d2 < N and 0 <= c-d1 < c < c+d2 < N:
                    fg = 0
                    mask = make(r,c,d1,d2)
                    for i in range(N):
                        for j in range(N):
                            if mask[i][j] == 0 and mask[i].count(0) == 2:
                                fg = 1
                                continue
                            if fg:
                                if mask[i][j] == 0:
                                    fg = 0
                                mask[i][j] = 0
                else:
                    continue

                for i in range(N):
                    for j in range(N):
                        if mask[i][j] == 0:
                            continue
                        if 0 <= i < r+d1 and 0<= j <= c:
                            mask[i][j] = 1
                        if 0 <= i <= r+d2 and c < j <= N-1:
                            mask[i][j] = 2
                        if r+d1 <= i <= N-1 and 0 <= j <= c-d1+d2:
                            mask[i][j] = 3
                        if r+d2 < i <= N-1 and c-d1+d2 <= j <= N-1:
                            mask[i][j] = 4
                for i in range(N):
                    for j in range(N):
                        pop[mask[i][j]] += mat[i][j]
                sol = min(sol, max(pop.values())-min(pop.values()))
print(sol)


    
