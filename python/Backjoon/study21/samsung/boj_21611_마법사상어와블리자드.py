import sys
read = sys.stdin.readline
N, M = map(int,read().split())
mat = [list(map(int,read().split())) for i in range(N)]
magic = [list(map(int,read().split())) for i in range(M)]

dd = [(-1,0),(1,0),(0,-1),(0,1)]

x,y = cx,cy = N//2,N//2
arr, d = [], 0

dirs = [(0,-1),(1,0),(0,1),(-1,0)]
for i in range(N-1):
    for j in range(2):
        for k in range(i+1):
            x,y = x+dirs[d][0], y+dirs[d][1]
            arr.append((x,y))
        d = (d+1)%4
arr += [(x+i*dirs[d][0],y+i*dirs[d][1]) for i in range(1,N)]

sol = 0
def cast(d,s):
    global sol
    for i in range(1,s+1):
        x,y = cx + i*dd[d][0], cy + i*dd[d][1]
        mat[x][y] = 0

def sorting(mat):
    global sol
    next_mat = [[0 for i in range(N)] for j in range(N)]

    tmp = []
    for x,y in arr:
        if mat[x][y]:
            tmp.append(mat[x][y])
    
    while True:
        bef, cnt, next_tmp, fg = tmp[0], 0, [], 1
        for i,v in enumerate(tmp):
            if bef == v:
                cnt += 1
            else:
                if cnt >= 4:
                    sol += (bef*cnt)
                    fg,cnt,bef = 0,1,v
                    continue
                next_tmp += [bef]*cnt
                cnt = 1
                bef = v
        if cnt < 4:
            next_tmp += [bef]*cnt
        if fg:
            break
        tmp = next_tmp
    
    bef,cnt,next_tmp = tmp[0],0,[]
    for i,v in enumerate(tmp):
        if len(next_tmp) >= N*N-2:
            break
        if bef == v:
            cnt += 1
        else:
            next_tmp.append(cnt)
            next_tmp.append(bef)
            bef,cnt = v,1
    tmp = next_tmp
    for i,val in enumerate(tmp):
        if not tmp[i]:
            break
        next_mat[arr[i][0]][arr[i][1]] = tmp[i]
    return next_mat

for d,s in magic:
    cast(d-1,s)
    mat = sorting(mat)

print(sol)


