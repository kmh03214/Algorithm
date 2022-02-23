# 방향을 N번 회전하고 멈추는 경우의 수
# N번 회전했을 때, 더이상 갈 수 있는 경로가 없다면 멈춤.
# N번 회전해서 갈 수 있는 모든 경우 중, 더 이상 갈 수 없는 경로의 개수를 센다.

# 1200만 = 3* 2^22 / 대칭이라 생각하면 400만. / 200만.

# N = int(input())
# print([0, 0, 0, 0, 2, 2, 4, 8, 24, 34, 76, 140, 306, 520, 1092, 1968, 4020, 7186, 14418, 26160, 51834, 94152, 184448, 336928][N-1])

# 0 -> -1,1 / 
# 1 -> 0,2 /
# 2 -> 1,3 /
# 3 -> 2,4 /
# 4 -> 3,5
# 5 -> 4,6 

dd = [(1,0,0), (0,1,0), (0,0,1), (-1,0,0), (0,-1,0), (0,0,-1)]

sol = [0]
check = {(0,0,0):1}

def dfs(s,d,depth):
    if depth > N:
        return
    
    if depth == 0:
        a = [0]
    else:
        a = [-1,1]

    for i in a:
        nd = (d+i)%6
        ns = (s[0] + dd[nd][0], s[1] + dd[nd][1], s[2] + dd[nd][2])

        if ns in check:
            if depth == N:
                sol[0] += 1
        
        else:
            check[ns] = 1
            dfs(ns, nd, depth+1)
            del check[ns]
a = []
for N in range(1,23):
    sol = [0]
    check = {(0,0,0):1}
    dfs((0,0,0),0,0)
    a.append(sol[0])
print(a)