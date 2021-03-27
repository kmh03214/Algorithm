import sys
read = sys.stdin.readline
DOORS = {s:1 for s in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
KEYS = {s:1 for s in 'abcdefghijklmnopqrstuvwxyz'}
def open_door(k):
    for i in k:
        if i == '0':
            return 'nokey'
        if i.upper() in doors:
            for door_xy in doors[i.upper()]:
                x, y = door_xy
                mat[x][y] = '.'
                if x == 0 or y == 0 or x == N-1 or y == M-1:
                    start_point.append((x,y))
    return 'open door complete'
def bfs(start):
    dx,dy = [1,0,-1,0],[0,1,0,-1]
    q = start
    check = {s:1 for s in q}
    cnt,KEY = 0,''
    while q:
        Next = []
        for v in q:
            r,c = v[0],v[1]
            for i in range(4):
                nx,ny = r+dx[i], c+dy[i]
                if 0<= nx< N and 0 <= ny < M and (nx,ny) not in check:
                    if mat[nx][ny] == '.':
                        check[(nx,ny)] = 1
                        Next.append((nx,ny))
                    elif mat[nx][ny] == '$':
                        cnt += 1
                        mat[nx][ny] = '.'
                        Next.append((nx,ny))
                        check[(nx,ny)] = 1
                    elif mat[nx][ny] == '*' or mat[nx][ny] in DOORS:
                        pass
                    else: # key획득
                        KEY += mat[nx][ny]
                        check[(nx,ny)] = 1
                        mat[nx][ny] = '.'
                        if nx == 0 or ny == 0 or nx ==N-1 or ny == M-1:
                            start_point.append((nx,ny))
        q = Next
    return cnt, KEY

T = int(read())
for test in range(T):
    N, M = map(int,read().split())
    mat = []
    doors = {}
    start_point = []
    sol = 0
    for i in range(N):
        a = ' '.join(read()).split()
        for j in range(M):
            if a[j] in DOORS:
                if a[j] not in doors:
                    doors[a[j]] = [(i,j)]
                else:
                    doors[a[j]].append((i,j))

            if (a[j] == '.' or a[j] == '$' or a[j] in KEYS) and (i == 0 or j == 0 or i == N-1 or j == M-1):
                start_point.append((i,j))
        mat.append(a)
    keys = read()
    for k in keys:
        if k.upper() in doors:
            for door_pos in doors[k.upper()]:
                x,y = door_pos
                if x == 0 or y == 0 or x == N-1 or y == M-1:
                    start_point.append((x,y))
                    mat[x][y] = '.'
    for v in start_point:
        if mat[v[0]][v[1]] == '$':
            sol += 1
            mat[v[0]][v[1]] = '.'

    while keys:
        open_door(keys)
        cnt, keys = bfs(start_point)
        sol += cnt
    print(sol)



