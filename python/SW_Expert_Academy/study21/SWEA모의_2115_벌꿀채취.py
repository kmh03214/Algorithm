from itertools import combinations

T = int(input())
def choose(arr):
    ret = 0
    for c in range(1,M+1):
        for combi in combinations(arr,c):
            if sum(combi) <= C:
                ret = max(sum([com**2 for com in combi]),ret)
    return ret    

for test in range(T):
    N,M,C = map(int,input().split())
    mat = [list(map(int,input().split())) for i in range(N)]

    sol = 0
    for i in range(N):
        for j in range(N):
            if j+M <= N:
                a = mat[i][j:j+M] # 일꾼 1번채취
                
                for x in range(i,N):
                    if x == i:
                        for y in range(j+M, N):
                            if y+M < N:
                                b = mat[x][y:y+M]
                                sol = max(sol, choose(a)+choose(b))
                    else:
                        for y in range(N):
                            if y+M <= N:
                                b = mat[x][y:y+M]
                                sol = max(sol, choose(a)+choose(b))
    print(sol)
    print("#%d %d"%(test+1, sol))