from itertools import combinations
T = int(input())

def select(honey,limit):
    honey.sort()
    ret = 0
    for k in range(1,M+1):
        for com in combinations(honey,k):
            total,money = 0,0
            for h in com:
                total += h
                money += (h**2)
            if total <= limit:
                if ret < money:
                    ret = money
            else:
                break
    return ret       


for test in range(T):
    N,M,C = map(int,input().split())
    mat,sol = [],[]
    for i in range(N):
        mat.append(list(map(int,input().split())))
    for row in range(N):
        for i in range(0, N-M+1):
            honey1 = mat[row][i:i+M]
            if (i+M + M) <= N: # 10, 4 3 [4,5,6],[7 8 9]
                for j in range(i+M,N-M+1):
                    honey2 = mat[row][j:j+M]
                    money1,money2 = select(honey1,C), select(honey2,C)
                    sol.append(money1+money2)
                for row2 in range(row+1,N):
                    for j in range(0,N-M+1):
                        honey2 = mat[row2][j:j+M]
                        money1,money2 = select(honey1,C), select(honey2,C)
                        sol.append(money1+money2)

            else:
                if row < N-1:
                    for row2 in range(row+1, N):
                        for j in range(0, N-M+1):
                            honey2 = mat[row2][j:j+M]
                            money1,money2 = select(honey1,C), select(honey2,C)
                            sol.append(money1+money2)
    print('#%d %d'%(test+1, max(sol)))
# 1
# 6 3 20
# 8 5 2 4 3 1
# 4 3 6 1 1 8
# 4 4 1 2 3 1
# 1 7 4 9 6 1
# 6 5 1 2 8 4
# 3 1 4 5 1 3