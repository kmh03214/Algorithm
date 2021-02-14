import sys
read = sys.stdin.readline
N,M = map(int,read().split())
mat = []
viruses = []
for i in range(N):
    a = list(map(int,read().split()))
    for j in range(N):
        if a[j] == 2:
            viruses.append((i,j))
    mat.append(a)

def combinations(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations(arr[i+1:],r-1):
                yield [arr[i]] + next

def bfs(start):
    q = start
    check = {i:1 for i in q}
    # mat copy
    mat_ = []
    remain = 0
    for m in mat:
        mat_.append(m.copy())
        remain += m.count(0)
    
    dx, dy = [1,-1,0,0],[0,0,1,-1]
    time = 0
    tmp_t = 0
    while q:
        Next = []
        fg = 0
        if remain == 0:
            break
        for v in q:
            r,c = v[0],v[1]
            for i in range(4):
                nx, ny = r+dx[i], c+dy[i]
                if 0 <= nx < N and 0 <= ny < N and (nx,ny) not in check and mat_[nx][ny] != 1:
                    Next.append((nx,ny))
                    check[(nx,ny)] = 1
                    if mat_[nx][ny] == 0:
                        remain -= 1                
                    mat_[nx][ny] = 2
        q = Next
        time += 1
    return time, mat_
    


sol = []
for virus in combinations(viruses,M):
    time, res = bfs(virus)

    flag = 1
    for m in res:
        if m.count(0):
            flag = 0
            break
    if flag:
        sol.append(time)

if sol:
    print(min(sol))
else:
    print(-1)



    