import sys
read = sys.stdin.readline
N = int(read())
mat = []
for i in range(N):
    mat.append(list(map(int,read().split())))

def condition(r,c,d1,d2,board):
    if 0 <= r < x+d1 and 0<= c <= y and board[r][c] != 5:
        return 1
    elif 0 <= r <= x+d2 and y < c < N and board[r][c] != 5:
        return 2
    elif x+d1 <= r <= N-1 and 0 <= c <= y-d1+d2-1 and board[r][c] != 5:
        return 3
    elif x+d2 < r <= N-1 and y-d1+d2-1 <= c <= N-1 and board[r][c] != 5:
        return 4
    else:
        return 5

def bfs(start,board):
    q = start
    check = {i:1 for i in start}
    dx,dy = [1,-1,0,0],[0,0,1,-1]
    while q:
        Next = []
        for v in q:
            r,c = v[0],v[1]
            board[r][c] = 5
            for i in range(4):
                nx,ny = r+dx[i],c+dy[i]
                if 0<= nx < N and 0< ny < N and board[nx][ny] != 5:
                    Next.append((nx,ny))
                    check[(nx,ny)] = 1
        q = Next


def divide(x,y,d1,d2):
    # d1, d2 >= 1 / 1 <= x < x+d1+d2 <= N / 1<= y-d1 < y < y+d2 <= N
    board = [[0 for i in range(N)] for j in range(N)]
    st = []
    for i in range(d1):
        board[x+i][y-i] = 5
        st.append((x+i+1,y-i))

    for j in range(d2):
        board[x+j][y+j] = 5
        st.append((x+j+1,y+j))

    for j in range(d2+1):
        board[x+d1+j][y-d1+j] = 5

    for i in range(d1+1):
        board[x+d2+i][y+d2-i] = 5
    
    bfs(st,board)

    humans = [0,0,0,0,0]
    for i in range(N):
        for j in range(N):
             humans[condition(i,j,d1,d2,board)-1] += mat[i][j]
    return humans


sol = []
for d1 in range(1,N):
    for d2 in range(1,N):
        for x in range(1,N):
            for y in range(1,N):
                if d1 >= 1 and d2 >= 1 and 1<= x and x+d1+d2 <= N-1 and 1 <= y-d1 and y+d2 <= N-1:
                    humans = divide(x,y,d1,d2)
                    sol.append(max(humans)-min(humans))
print(min(sol))


