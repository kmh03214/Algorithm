import sys
read = sys.stdin.readline
N,M, x,y, K = map(int, read().split()) # N, M <20 ,xy주사위좌표, 명령 K <1000
mat = []
for i in range(N):
    mat.append(list(map(int, read().split())))

order = list(map(int,read().split())) # 동:1 서:2 북:3 남:4

dice = {i+1:0 for i in range(6)}
def roll_dice(d,x,y):
    d -= 1
    dx, dy = [0,0,-1,1], [1,-1,0,0]
    nx,ny = x + dx[d], y + dy[d]
    if 0 <= nx < N and 0 <= ny < M:
        if d == 0: # 동 / 오른
            dice[3], dice[6], dice[4], dice[1] = dice[1], dice[3], dice[6], dice[4]
        if d == 1: # 서 / 왼
            dice[1], dice[3], dice[6], dice[4] = dice[3], dice[6], dice[4], dice[1]
        if d == 2: # 북 / 위
            dice[2], dice[6], dice[1], dice[5] = dice[1], dice[2], dice[5], dice[6]
        if d == 3: # 남 / 아래 
            dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
        if mat[nx][ny] != 0:
            dice[6] = mat[nx][ny]
            mat[nx][ny] = 0
        else:
            mat[nx][ny] = dice[6]
        print(dice[1])
        return nx,ny
    else:
        return x,y

for i in range(K):
    x,y = roll_dice(order[i],x,y)