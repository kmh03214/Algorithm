from queue import deque
import sys
read = sys.stdin.readline
N = int(read())
K = int(read())
mat = [[0 for i in range(N)] for i in range(N)]
for i in range(K):
    ax,ay = map(int,read().split())
    mat[ax-1][ay-1] = 1
L = int(read())
order = [read().split() for i in range(L)] + [('100000000','end')]

snake = deque([(0,0)])

dd = [(0,1),(1,0),(0,-1),(-1,0)] # 오 아래 왼 위
def move(d):
    hx,hy = snake.popleft()
    nhx,nhy = hx + dd[d][0], hy + dd[d][1]
    if 0 <= nhx < N and 0 <= nhy < N and (nhx,nhy) not in snake:
        snake.appendleft((hx,hy))
        snake.appendleft((nhx,nhy))
        if mat[nhx][nhy] != 1:
            snake.pop()
        mat[nhx][nhy] = 0
    else:
        return 1,d
    return 0,d

s, d, fg = 0, 0, None
for o in order:
    for i in range(s,int(o[0])):
        r,d = move(d)
        if r:
            fg = 1
            break
    if fg:
        break
    d = (lambda x : (x+1)%4 if o[1] == 'D' else (x-1)%4)(d)
    s = int(o[0])
print(i+1)