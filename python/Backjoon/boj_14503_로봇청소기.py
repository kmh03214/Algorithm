import sys
read = sys.stdin.readline
N,M = map(int,read().split())
r,c,d = map(int,read().split())
mat = []
for i in range(N):
    a = list(map(int,read().split()))
    mat.append(a)

dx,dy = [-1,0,1,0], [0,1,0,-1] # 북 동 남 서
def bfs( cur_pos, cur_dir ):
    q = [cur_pos]
    clean = {cur_pos : 1}

    while q:
        for v in q:
            fg = 0
            mat[v[0]][v[1]] = 2 # 현재 위치 청소
            for i in range(4):
                d = (cur_dir-i+3)%4
                nx, ny = v[0] + dx[d], v[1] + dy[d]
                if mat[nx][ny] == 0 and (nx,ny) not in clean:
                    q = [(nx,ny)]
                    cur_pos = (nx,ny)
                    clean[(nx,ny)] = 1
                    cur_dir = d
                    fg = 1
                    break
            if fg == 0:
                back = (cur_dir+2)%4
                bx,by = v[0] + dx[back], v[1] + dy[back]
                if mat[bx][by] == 2:
                    q = [(bx,by)]
                else:
                    return
bfs((r,c), d)
sol = 0
for i in range(N):
    sol += mat[i].count(2)
print(sol)


