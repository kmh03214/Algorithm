import sys
read = sys.stdin.readline

N,M,K = map(int,read().split())
mat = [list(map(int,read().split())) for i in range(N)]

dd = [(0,1),(1,0),(0,-1),(-1,0)]

#   2
# 4 6 3
#   5
#   1

dice = [1,2,3,4,5,6]

def roll_dice(d):
    if d == 0:
        dice[2],dice[0],dice[3],dice[5] = dice[0],dice[3],dice[5],dice[2]
    if d == 1:
        dice[1],dice[5],dice[4],dice[0] = dice[5],dice[4],dice[0],dice[1]
    if d == 2:
        dice[0],dice[3],dice[5],dice[2] = dice[2],dice[0],dice[3],dice[5]
    if d == 3:
        dice[5],dice[4],dice[0],dice[1] = dice[1],dice[5],dice[4],dice[0]

def bfs(start):
    q = [start]
    check = {start:1}
    while q:
        Next = []
        for v in q:
            for dx,dy in dd:
                nx,ny = v[0]+dx, v[1]+dy
                if 0<=nx<N and 0<=ny < M and (nx,ny) not in check and mat[nx][ny] == val:
                    check[(nx,ny)]= 1
                    Next.append((nx,ny))
        q = Next
    return len(check)


x,y,d = 0,0,0
sol = 0
for i in range(K):
    x,y = x + dd[d][0], y + dd[d][1]
    if not (0 <= x < N and 0 <= y < M):
        d = (d+2)%4
        x,y = x + 2*dd[d][0], y + 2*dd[d][1]
    roll_dice(d)

    val = mat[x][y]
    sol += (val*bfs((x,y)))

    if dice[5] > val:
        d = (d+1)%4
    if dice[5] < val:
        d = (d-1)%4
print(sol)
