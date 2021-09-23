import sys
read = sys.stdin.readline
N,M,x,y,K = map(int,read().split())
mat = []
for i in range(N):
    mat.append(list(map(int,read().split())))
order = list(map(int,read().split()))

# 동 서 북 남
# 이동칸에 쓰인수가 0 -> 주사위 바닥면 수 칸에 복사 / 칸에 쓰인 수가 주사위 바닥으로 복사후 칸=0
# 4,1,3,6
# 2,1,5,6
dice = [0,0,0,0,0,0,0]
def roll_dice(d):
    if d == 1:
        dice[4],dice[1],dice[3],dice[6] = dice[1], dice[3], dice[6], dice[4]
    if d == 2:
        dice[4],dice[1],dice[3],dice[6] = dice[6], dice[4], dice[1], dice[3]
    if d == 3:
        dice[2],dice[1],dice[5],dice[6] = dice[6], dice[2], dice[1], dice[5]
    if d == 4:
        dice[2],dice[1],dice[5],dice[6] = dice[1], dice[5], dice[6], dice[2]
dd = [(0,0),(0,1),(0,-1),(-1,0),(1,0)]
def move(r,c,d):
    nx,ny = r+dd[d][0], c+ dd[d][1]
    if 0 <= nx < N and 0 <= ny < M:
        roll_dice(d)
        if mat[nx][ny] == 0:
            mat[nx][ny] = dice[1]
        else:
            dice[1], mat[nx][ny] = mat[nx][ny], 0
        print(dice[6])
        return nx,ny
    else:
        return x,y
for o in order:
    x,y = move(x,y,o)