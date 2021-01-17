import sys
read = sys.stdin.readline
N = int(read())
T,P = [0], [0]

for i in range(N):
    t,p = map(int,read().split())
    T.append(t)
    P.append(p)

sol = []
def DFS(day, money):
    if day > N:
        sol.append(money)
        return
    if day < N+1 and day + T[day] <= N+1:
        DFS(day + T[day], money + P[day])
    DFS(day+1, money)
    
DFS(1,0)
print(max(sol))

# 7
# 3 10
# 5 20
# 1 10
# 1 20
# 4 15
# 1 40
# 2 200