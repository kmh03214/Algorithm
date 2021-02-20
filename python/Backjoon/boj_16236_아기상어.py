import sys
read = sys.stdin.readline
N = int(read())
mat,shark = [], []

for i in range(N):
    a = list(map(int,read().split()))
    for j in range(N):
        if a[j] == 9:
            shark.append((i,j))
            shark.append(2)
            shark.append(0)
    mat.append(a)

def bfs(shark):
    q, check, eats,time = [shark[0]], {shark[0]:1}, [],0
    mat[shark[0][0]][shark[0][1]] = 0
    dx,dy = [1,0,-1,0],[0,1,0,-1]

    # 먹을고기 탐색
    while q:
        Next = []
        time += 1
        for v in q:
            r,c = v[0],v[1]
            for i in range(4):
                nx,ny = r+dx[i], c+dy[i]
                if 0 <= nx < N and 0 <= ny < N and (nx,ny) not in check and mat[nx][ny] <= shark[1]:
                    if mat[nx][ny] < shark[1] and mat[nx][ny] != 0:
                        eats.append((nx,ny))
                    Next.append((nx,ny))
                    check[(nx,ny)] = 1

        if eats:
            eats.sort()
            shark[0] = eats[0] # 아기상어 물고기 먹으러 이동
            shark[2] += 1 # 현재상태에서 먹은 물고기 개수
            if shark[2] == shark[1]:
                shark[1] += 1 # 물고기 먹고 상어 크기 증가
                shark[2] = 0
            mat[eats[0][0]][eats[0][1]] = 0 # 물고기 먹고 사라짐
            return 'eat', time
        q = Next
    return 'hungry', 0
sol = 0
while True:
    flag, time = bfs(shark)
    if flag == 'eat':
        sol += time
    else:
        break
    
print(sol)

        