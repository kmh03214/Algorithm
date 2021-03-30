dd = [(-1,0),(0,1),(1,0),(0,-1)]
def simulation(start,d):
    sx,sy = start
    q = [start]
    sol = 0
    while q:
        Next = []
        for v in q:
            x,y = v[0],v[1]
            nx,ny = x + dd[d][0], y + dd[d][1]
            if 0<= nx < N and 0 <= ny < N:
                number = mat[nx][ny]
                if (nx,ny) == (sx,sy) or number == -1: # 스타팅포인트와 같거나 블랙홀
                    return sol
                    # 게임 끝
                elif number in blocks:
                    if 1<= number < 6: # 방향전환
                        sol += 1
                        d = blocks[number][d]
                        Next.append((nx,ny))
                    else: # 위치변환
                        pos = blocks[number][(nx,ny)]
                        Next.append(pos)
                else:
                    Next.append((nx,ny))
            else: # 벽에부딪힘
                sol += 1
                d = blocks[5][d] # 반대 방향전환
                Next.append((nx,ny))
        q = Next

T = int(input())
for test in range(1,T+1):
    blocks = {
        1: [2,3,1,0],
        2: [1,3,0,2],
        3: [3,2,0,1],
        4: [2,0,3,1],
        5: [2,3,0,1]
    }

    N = int(input())
    w_hall = {} 
    mat,start_points = [],[]
    for i in range(N):
        a = list(map(int,input().split()))
        for j in range(N):
            if a[j] == 0:
                start_points.append((i,j))
            if 6 <= a[j] <= 10:
                if a[j] not in w_hall:
                    w_hall[a[j]] = (i,j)
                else:
                    blocks[a[j]] = { w_hall[a[j]] : (i,j) , (i,j) : w_hall[a[j]] }
        mat.append(a)
    
    SOL = []
    for start in start_points:
        for d in range(4):
            ret = simulation(start,d)
            SOL.append(ret)

    print('#%d %d'%(test, max(SOL)))

