dd = [(1,-1),(1,1),(-1,1),(-1,-1)]
def play(x,y,r1,r2):
    d,eats = 0,{}
    for k in range(2):
        for i in range(r1):
            x,y = x + dd[d][0] , y + dd[d][1]
            if not (0<= x < N and 0<= y < N) or mat[x][y] in eats:
                return -1
            eats[mat[x][y]] = 1
        d += 1
        for i in range(r2):
            x,y = x + dd[d][0] , y + dd[d][1]
            if not (0<= x < N and 0<= y < N) or mat[x][y] in eats:
                return -1
            eats[mat[x][y]] = 1
        d += 1
    return len(eats)
    
T = int(input())
for test in range(T):
    N = int(input())
    mat = [list(map(int,input().split())) for i in range(N)]
    sol = -1
    for i in range(N):
        for j in range(N):
            for r1 in range(1,N):
                for r2 in range(1,N-r1):
                    sol = max(sol, play(i,j,r1,r2))

    print("#%d %d"%(test+1, sol))


