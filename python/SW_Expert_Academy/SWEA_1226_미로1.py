dx,dy = [1,-1,0,0],[0,0,1,-1]
def bfs(start):
    q = [start]
    check = {start:1}
    while q:
        Next = []
        for v in q:
            x,y = v[0],v[1]
            if mat[x][y] == '3':
                return 1
            for i in range(4):
                nx,ny = x+dx[i], y+dy[i]
                if 0<= nx <16 and 0<= ny < 16 and (nx,ny) not in check and mat[nx][ny] != '1':
                    Next.append((nx,ny))
                    check[(nx,ny)] = 1
        q = Next
    return 0
for test in range(1,11):
    mat = []
    num = int(input())
    for i in range(16):
        a = ' '.join(input()).split()
        for j in range(16):
            if a[j] == '2':
                start = (i,j)
        mat.append(a)

    print("#%d %d"%(test,bfs(start)))

