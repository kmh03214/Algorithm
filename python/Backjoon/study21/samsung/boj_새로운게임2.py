import sys
read = sys.stdin.readline
N,K = map(int,read().split())
mat = [list(map(int,read().split())) for i in range(N)]
player = [ (lambda x:[x[0]-1,x[1]-1,x[2]-1])(list(map(int,read().split()))) for i in range(K)]
# 오 왼 위 아래
dd,time = [(0,1),(0,-1),(-1,0),(1,0)],0
board = [[[] for i in range(N)] for j in range(N)]
for i in range(len(player)):
    board[player[i][0]][player[i][1]].append(i)

reverse_d,fg = {0:1,1:0,2:3,3:2},0

def move(x,y,d,arr,color):
    if color == 0:
        board[x][y] += arr
        for num in arr:
            player[num][0],player[num][1] = [x,y]
    if color == 1:
        arr.reverse()
        board[x][y] += arr
        for num in arr:
            player[num][0],player[num][1] = [x,y]
    if color == 2:
        nd = reverse_d[d]
        nx,ny = x + dd[nd][0],y + dd[nd][1]
        if not (0<=nx < N and 0<= ny < N) or mat[nx][ny] == 2:
            nx,ny = x,y
        if mat[nx][ny] == 1:
            arr.reverse()
        board[nx][ny] += arr
        for num in arr:
            player[num] = [nx,ny,nd]

while time < 1000:
    for p_num,p in enumerate(player):
        x,y,d = p
        nx,ny = x+dd[d][0],y+dd[d][1]
        idx = board[x][y].index(p_num)
        
        board[x][y], stack = board[x][y][:idx], board[x][y][idx:]
        if 0<= nx < N and 0 <= ny < N:
            if mat[nx][ny] != 2:
                move(nx,ny,d,stack, mat[nx][ny])
            else:
                move(x,y,d,stack,2)
        else:
            move(x,y,d,stack,2)
    for p in player:
        x,y,d = p
        if len(board[x][y]) >= 4:
            fg = 1
            break
    if fg:
        break
    time+=1
if fg:
    print(time+1)
else:
    print(-1)