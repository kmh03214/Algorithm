import sys
read = sys.stdin.readline

N,M = map(int,read().split())
mat,virus,safe = [],[],[]
for i in range(N):
    a = list(map(int,read().split()))
    for j in range(M):
        if a[j] == 0:
            safe.append((i,j))
        if a[j] == 2:
            virus.append((i,j))
    mat.append(a)

def combinations(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations(arr[i+1:],r-1):            
                yield next + [arr[i]]
dx,dy = [1,-1,0,0],[0,0,1,-1]
def pollution(virus,wall):
    mat_c = []
    for m in mat:
        mat_c.append(m.copy())

    for w in wall:
        mat_c[w[0]][w[1]] = 1
    check = {v:1 for v in virus}
    while virus:
        Next = []
        for v in virus:
            for i in range(4):
                nx,ny = v[0]+dx[i],v[1]+dy[i]
                if 0 <= nx < N and 0 <= ny < M and (nx,ny) not in check and mat_c[nx][ny] != 1:
                    check[(nx,ny)], mat_c[nx][ny] = 1, 2
                    Next.append((nx,ny))
        virus = Next
    return sum([a.count(0) for a in mat_c])
s = 0
for combi in combinations(safe,3):
    s = max(s,pollution(virus, combi))
print(s)