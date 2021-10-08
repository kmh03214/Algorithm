import sys
read = sys.stdin.readline
N,M,T = map(int, read().split())
mat = [list(map(int,read().split())) for i in range(N)]
order = [list(map(int,read().split())) for i in range(T)]

def bfs(s):
    q = [s]
    while q:
        Next = []
        for v in q:
            for d in [(0,1),(1,0),(0,-1),(-1,0)]:
                nx,ny = v[0]+d[0],v[1]+d[1]
                if 0 <= nx < N and -1 <= ny < M and (nx,ny) not in check and mat[nx][ny] == mat[v[0]][v[1]]:
                    check[(nx,ny)], check2[(v[0],v[1])], check2[(nx,ny)] = 1, 1, 1
                    Next.append((nx,ny))
        q = Next

for x,d,k in order: # x배수 d방향 k칸 0이면 시계 1이면 반시계
    cnt = 1
    while x*cnt - 1 < N:
        arr = mat[x*cnt-1]
        if d:
            mat[x*cnt-1] = arr[k:] + arr[:k]
        else:
            mat[x*cnt-1] = arr[-k:] + arr[:-k]
        cnt += 1

    check,check2, total,Len = {},{}, 0,0
    for i in range(N):
        for j in range(M):
            if mat[i][j] != 0:
                total += mat[i][j]
                Len += 1
            if mat[i][j] != 0 and (i,j) not in check:
                check[(i,j)] = 1
                bfs((i,j))
    if check2:
        for v in check2:
            mat[v[0]][v[1]] = 0
    else:
        if Len:
            avg = total/Len
        else:
            continue
        for i in range(N):
            for j in range(M):
                if mat[i][j] != 0:
                    if mat[i][j] < avg:
                        mat[i][j] += 1
                    elif mat[i][j] > avg:
                        mat[i][j] -= 1
print(sum([sum(m) for m in mat]))


