import sys
read = sys.stdin.readline
N,M = map(int,read().split())
r,c,d = map(int,read().split())
mat = []
for i in range(N):
    mat.append(list(map(int,read().split())))

cleans = {}
# 0,1,2,3 북 동 남 서
dd = [(-1,0),(0,1),(1,0),(0,-1)]
def cleaning(r,c,d):
    cleans[(r,c)] = 1
    q = [(r,c)]
    while q:
        Next,fg = [],0
        for v in q:
            for i in range(4):
                d = (d-1)%4
                nx,ny = v[0] + dd[d][0], v[1] + dd[d][1]
                if mat[nx][ny] != 1 and (nx,ny) not in cleans:
                    cleans[(nx,ny)] = 1
                    Next.append((nx,ny))
                    fg = 1
                    break
                if i == 1:
                    bx,by = nx,ny            
            if fg:
                break
            else: # 네방향이 청소 or 벽
                if mat[bx][by] != 1:
                    Next.append( (bx,by) )
        q = Next
    return len(cleans)

print(cleaning(r,c,d))