N,M = map(int,input().split())
mat,attacks = [],[]
for i in range(N):
    mat.append(list(map(int,input().split())))
for i in range(M):
    attacks.append(list(map(int,input().split()))) # 방향 범위

tower = (N//2, N//2)
dx,dy = [0,1,0,-1], [-1,0,1,0]

# 1,1 / 2,2 / 3,3 / 4,4 / 4 -> N : 5
def rotation():
    arr = []
    r,c = tower
    num = 0
    for i in range(1,N):
        for k in range(2):
            for j in range(i):
                r,c = r+dx[num%4],c+dy[num%4]
                arr.append((r,c))
            num += 1
    for i in range(N-1):
        r,c = r+dx[num%4],c+dy[num%4]
        arr.append((r,c))
    return arr

dd = {0:(0,1),1:(1,0),2:(0,-1),3:(-1,0)}
score = 0
for attack in attacks:
    d, power = attack
    r,c = tower
    for i in range(power):
        r,c = r + dd[d][0], c+ dd[d][1]
        if mat[r][c] > 0:
            score += mat[r][c]
            mat[r][c] = 0
    arr = rotation()

    tmp = []
    for pos in arr:
        r,c = pos
        if mat[r][c] > 0:
            tmp.append(mat[r][c])
            
    while True:
        next_tmp = []
        before,cnt = 0, 1
        fg = 0
        for v in tmp:
            if before == v:
                cnt+=1
            else:
                if cnt > 3:
                    fg = 1
                    for i in range(cnt):
                        next_tmp.pop()
                    score += (before*cnt)
                before = v
                cnt = 1
            next_tmp.append(v)
        tmp = next_tmp
        if fg == 0:
            if cnt > 3:
                fg = 1
                for i in range(cnt):
                    tmp.pop()
                score += (before*cnt)
            break
    
    next_mat = [[0 for i in range(N)] for j in range(N)]
    if tmp:
        virus = []
        before,cnt = tmp[0],0
        for v in tmp:
            if v == before:
                cnt += 1
            else:
                virus.append(cnt)
                virus.append(before)
                cnt = 1
                before = v
        virus.append(cnt)
        virus.append(before)
        for i in range(len(virus)):
            if i > N*N-2:
                break
            v = virus[i]
            r,c = arr[i]
            next_mat[r][c] = v
    mat = next_mat
print(score)