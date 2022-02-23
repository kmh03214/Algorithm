
# 선택할 수 있는 경우 -> (0,0), (0,1)
# 50 x 50 -> (0,0) ~ (47,47) (47^2)개의 선택가능 -> (47^2)*(47^2-1)가지 = 487만

import sys
read = sys.stdin.readline
N,M = map(int,read().split())
A,B = [], []
for i in range(N):
    A.append(list(map(int,' '.join(read()).split())))
for i in range(N):
    B.append(list(map(int,' '.join(read()).split())))

def check(r,c):
    for i in range(r,r+3):
        for j in range(c,c+3):
            if A[i][j] != B[i][j]:
                return 1
    return 0

def reverse_oper(r,c):
    for i in range(r,r+3):
        for j in range(c,c+3):
            if A[i][j] == 1:
                A[i][j] = 0
            else:
                A[i][j] = 1
sol, fg = 0, 0
for r in range(N-2):
    for c in range(M-2):
        if check(r,c):
            reverse_oper(r,c)
            sol += 1

for i in range(N):
    for j in range(M):
        if A[i][j] != B[i][j]:
            fg = 1
            break
if fg:
    print(-1)
else:
    print(sol)

