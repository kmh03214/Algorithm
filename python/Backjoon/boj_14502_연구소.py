import sys
read = sys.stdin.readline
N,M = map(int,read().split())
mat,nomi,virus = [],[],[]
for i in range(N):
    a = list(map(int,read().split()))
    mat.append(a)
    for j in range(M):
        if a[j] == 0:
            nomi.append((i,j))
        if a[j] == 2:
            virus.append((i,j))

def combinations(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations(arr[i+1:],r-1):
                yield [arr[i]] + next
mat_copy = []
min_sol, min_virus = 0, len(nomi) # 안전영역 크기, 최소 바이러스
dx,dy = [1,-1,0,0], [0,0,1,-1]
def bfs(mat,virus):
    q, cur_virus = virus, 3
    check = {v:1 for v in virus}
    while q:
        Next = []
        for v in q:
            r,c = v[0],v[1]
            for i in range(4):
                nr,nc = r+dx[i],c+dy[i]
                if min_virus < cur_virus:
                    return len(nomi) - cur_virus
                if 0 <= nr < N and 0 <= nc < M and mat[nr][nc] == 0 and (nr,nc) not in check:
                    mat[nr][nc] = 2
                    Next.append((nr,nc))
                    check[(nr,nc)] = 1
                    cur_virus += 1
        q = Next
    return len(nomi) - cur_virus

for walls in combinations(nomi,3):
    # 맵 초기화
    mat_copy = []
    for m in mat:
        mat_copy.append(m.copy())

    # 벽 세우기
    for wall in walls:
        mat_copy[wall[0]][wall[1]] = 1
    
    sol = bfs(mat_copy,virus) # 바이러스 퍼트리기
    if sol > min_sol:
        min_sol = sol
print(min_sol)