dd = [(-1,0),(1,0),(0,-1),(0,1)] # 상 하 좌 우
def search(start):
    q = [start]
    check,sols = {start:1},[]
    sales = M*mat[start[0]][start[1]] # 초기 매출
    if sales:
        inbound_home = 1 # 보안구역 내부 집 개수
        sols.append(1)
    else:
        inbound_home = 0

    while q:
        Next = []
        if len(check) > home_cnt*M: # 최대 매출보다 운영비용이 높아지는 순간
            break
        for v in q:
            r,c = v[0],v[1]
            for i in range(4):
                nx,ny = r+dd[i][0], c+dd[i][1]
                if (nx,ny) not in check:
                    check[(nx,ny)] = 1
                    Next.append((nx,ny))
                    if 0<= nx < N and 0 <= ny < N and mat[nx][ny] == 1:
                        sales += M
                        inbound_home += 1
        q = Next
        if sales >= len(check):
            sols.append(inbound_home) 
    return sols

T = int(input())

for test in range(1,T+1):
    N,M = map(int,input().split())
    mat,home_cnt = [],0
    for i in range(N):
        a = list(map(int,input().split()))
        home_cnt += a.count(1)
        mat.append(a)
    
    sol = 0
    for i in range(N):
        for j in range(N):
            sols = search((i,j))
            if sols:
                sol = max(max(sols),sol)
    print('#%d %d'%(test, sol))

