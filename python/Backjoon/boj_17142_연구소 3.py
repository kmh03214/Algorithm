import sys
read = sys.stdin.readline
N, M = map(int,read().split())
mat, virus = [], []
for i in range(N):
    a = list(map(int,read().split()))
    mat.append(a)
    for j in range(N):
        if a[j] == 2:
            virus.append((i,j))

def combinations(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations(arr[i+1:],r-1):
                yield next + [arr[i]]

act_virus = list(combinations(virus,M))

def bfs(start,arr):
    dx, dy, time = [1,-1,0,0], [0,0,1,-1], 0
    q = start
    check = {}
    for i in start:
        check[i] = 1
    while q:
        Next, flag = [], 0
        for v in q:
            r, c = v[0], v[1]
            for i in range(4):
                nr, nc = r + dx[i], c + dy[i]
                if (nr,nc) not in check and 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 1:
                    if arr[nr][nc] != 2:
                        flag = 1
                    check[(nr,nc)] = 1
                    arr[nr][nc] = 2
                    Next.append((nr,nc))
        time += 1
        if flag == 0:
            flag2 = 1
            for i in arr:
                if i.count(0):
                    flag2 = 0
                    break
            if flag2:
                time -= 1

        q = Next
    # q가 비었다는 건, 바이러스가 확산이 끝남, (빈곳이 있는지 확인해야함.)
    for i in arr:
        if i.count(0):
            return -1
    
    return time
sol = []
for i in range(len(act_virus)):
    m = []
    for cp in mat:
        m.append(cp.copy())
    s = bfs(act_virus[i],m)
    if s != -1:
        sol.append(s)

if sol:
    print(min(sol))
else:
    print(-1)
