import sys
read = sys.stdin.readline
R,C,T = map(int,read().split())
cleaner, mat, dust, time = [], [], {}, 0

for i in range(R):
    a = list(map(int,read().split()))
    for j in range(C):
        if a[j] == -1:
            cleaner.append((i,j))
        elif a[j] != 0:
            dust[(i,j)] = a[j]
    mat.append(a)

dd = [(0,1),(1,0),(0,-1),(-1,0)]
def clean(s, up):
    a, row = [], s[0]
    if up != 1:
        row = R-row-1
    for z in [1,-1]:
        for i in range(C-1):
            s[0],s[1] = s[0] + z*dd[0][0], s[1] + z*dd[0][1]
            a.append(tuple(s))
        for j in range(row):
            s[0],s[1] = s[0] + up*z*dd[3][0], s[1] + up*z*dd[3][1]
            a.append(tuple(s))
    return a
    
cu,cd = clean(list(cleaner[0]),1),clean(list(cleaner[1]),-1)

def wind(arr):
    sx,sy = arr[0]
    for i in range(len(arr)-1):
        nx,ny = arr[i]
        mat[sx][sy], mat[nx][ny], dust[(nx,ny)] = mat[nx][ny], mat[sx][sy], mat[sx][sy]
    mat[sx][sy], dust[(sx,sy)] = 0, 0
    
while time != T:
    next_dust = {}
    for x,y in dust:
        cnt_dir,div = 0, dust[(x,y)]//5
        for i in range(4):
            nx,ny = x + dd[i][0], y + dd[i][1]
            if 0 <= nx < R and 0 <= ny < C and (nx,ny) not in cleaner:
                if (nx,ny) not in next_dust:
                    next_dust[(nx,ny)] = div
                else:
                    next_dust[(nx,ny)] += div
                cnt_dir += 1
        if (x,y) not in next_dust:
            next_dust[(x,y)] = dust[(x,y)] - cnt_dir*(div)
        else:
            next_dust[(x,y)] += (dust[(x,y)] - cnt_dir*(div))
    dust = next_dust
    for d in dust:
        mat[d[0]][d[1]] = dust[d]
    wind(cu), wind(cd)
    time+=1
print(sum([sum(m) for m in mat])+2)






