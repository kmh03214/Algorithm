from itertools import permutations
T = int(input())
for test in range(1,T+1):
    N = int(input())
    a = list(map(int,input().split()))
    mat = [[0 for i in range(N+2)] for j in range(N+2)]
    for i in range(N+2):
        for j in range(i,N+2):
            x1,y1,x2,y2 = a[2*i],a[2*i+1], a[2*j],a[2*j+1]
            mat[i][j] = mat[j][i] = abs(x1-x2)+abs(y1-y2)
    sol = []

    for per in permutations([i for i in range(2,N+2)],N):
        q,s = 0,0
        for p in per:
            s += mat[q][p]
            q = p
        s+=mat[q][1]
        sol.append(s)

    print("#%d %d"%(test,min(sol)))

