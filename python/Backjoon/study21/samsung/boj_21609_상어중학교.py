import sys
read = sys.stdin.readline
N,M = map(int,read().split())
mat = [list(map(int,read().split())) for i in range(N)]

def find_group(s):
    q, ret_group,rainbow_cnt,general = [s],{s:1},0,[]
    if mat[s[0]][s[1]]:
        general.append(s)

    color = mat[s[0]][s[1]]
    while q:
        Next = []
        for v in q:
            for d in [(0,1),(1,0),(0,-1),(-1,0)]:
                nx,ny = v[0] + d[0], v[1] + d[1]
                if 0<= nx < N and 0 <= ny < N and mat[nx][ny] != -1 and mat[nx][ny] != '' and (nx,ny) not in ret_group:
                    if mat[nx][ny] and color != mat[nx][ny]:
                        continue
                    if mat[nx][ny] == 0:
                        rainbow_cnt += 1
                    else:
                        general.append((nx,ny))
                    Next.append((nx,ny))
                    check[(nx,ny)] = 1
                    ret_group[(nx,ny)] = 1
        q = Next
    if len(ret_group) > 1:
        # 무지개블록이 아닌 것(general) 중 기준블록
        general.sort()
        if general:
            return general[0][0],general[0][1],ret_group,rainbow_cnt
        else:
            return s[0],s[1],0,0
    else:
        return s[0],s[1],0,0
def gravity(mat):
    for j in range(N):
        limit = N
        fg = 0
        for i in range(N-1,-1,-1):
            val = mat[i][j]
            if val == -1:
                limit = i+1
                continue
            if val == '':
                continue

            for k in range(i+1,limit):
                if mat[k][j] != '':
                    mat[i][j] = ''
                    mat[k-1][j] = val
                    fg = 1
                    break

            if not fg:
                mat[i][j] = ''
                if limit == N:
                    mat[limit-1][j] = val
                    continue
                if mat[limit][j] == -1:
                    mat[limit-1][j] = val
                else:
                    mat[k][j] = val
    return mat


# 블록그룹이 없을 때 까지 반복
score = 0
while True:
    check = {}
    groups = []
    for i in range(N):
        for j in range(N):
            if (i,j) not in check and mat[i][j] != -1 and mat[i][j] != '':
                x,y,group,rainbow = find_group((i,j))
                if group:
                    groups.append((group,x,y,rainbow))
    if not groups:
        break
    largest_group = sorted(groups, key = lambda x:(-len(x[0]),-x[3],-x[1],-x[2] ))[0]

    for x,y in largest_group[0]:
        mat[x][y] = ''
    score += (len(largest_group[0]))**2

    # 중력
    mat = gravity(mat)
    # 반시계 90 회전
    mat = [list(m) for m in reversed(list(zip(*mat)))]
    
    # 중력
    mat = gravity(mat)
    
print(score)

