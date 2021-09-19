import sys
read = sys.stdin.readline

N,M = map(int,read().split())
mat = []
for i in range(N):
    mat.append(list(map(int,read().split())))

dx,dy = [1,-1,0,0],[0,0,1,-1]
def bfs(start):
    q = start
    Next_start = []
    while q:
        Next = []
        for v in q:
            for i in range(4):
                nx,ny = v[0]+dx[i], v[1]+dy[i]
                if 0 <= nx < N and 0 <= ny < M and (nx,ny) not in check:
                    if mat[nx][ny] == 1:
                        Next_start.append((nx,ny))
                        check[(nx,ny)] = 1
                        continue
                    check[(nx,ny)] = 1
                    Next.append((nx,ny))
        q = Next
    return Next_start

time = 0
start = [(0,0)]
check = {start[0]:1}
while 1:
    time += 1
    bef_start = start.copy()
    start = bfs(start)
    if len(check) == N*M:
        break
    for s in start:
        mat[s[0]][s[1]] = 0


if not start:
    print(time-1)
    print(len(bef_start))
else:
    print(time)
    print(len(start))

