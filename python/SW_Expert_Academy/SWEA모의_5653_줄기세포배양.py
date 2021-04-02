T = int(input())
dx,dy = [1,-1,0,0],[0,0,1,-1]
for test in range(1,T+1):

    N,M,K = map(int,input().split())
    no_active,check = [],{}
    for i in range(N):
        a = list(map(int, input().split()))
        for j in range(M):
            if a[j] != 0:
                no_active.append([i,j,a[j],0]) # r,c,생명력,지난시간
                check[(i,j)] = 1
    
    
    active, dead = {},[]
    time = 0

    while time != K:
        time += 1
        Next_no_act = []
        # 번식
        tmp,del_tmp = {},[]
        for v in active:
            active[v] += 1
            if active[v] == 1:
                for i in range(4):
                    nx,ny = v[0]+dx[i],v[1]+dy[i]
                    if (nx,ny) in tmp:
                        if tmp[(nx,ny)] < v[2]:
                            Next_no_act.remove([nx,ny,tmp[(nx,ny)],0])
                            tmp[(nx,ny)] = v[2] # 생명력 수치가 높은 줄기세포가 해당 그리드 셀 혼자 차지
                            Next_no_act.append([nx,ny,v[2],0])
                    if (nx,ny) not in check:
                        tmp[(nx,ny)] = v[2]
                        check[(nx,ny)] = 1
                        Next_no_act.append([nx,ny,v[2],0])
            if active[v] == v[2]:
                del_tmp.append(v)

        for v in del_tmp:
            del active[v]
            dead.append(v)
        for cell in no_active:
            # r,c,life,t = cell[0],cell[1],cell[2],cell[3]
            cell[3] += 1
            if cell[3] == cell[2]: # 활성변화
                active[(cell[0],cell[1],cell[2])] = 0
            else:
                Next_no_act.append(cell)

        no_active = Next_no_act
        
        
        
    print('#%d %d'%(test, len(no_active)+len(active)))


