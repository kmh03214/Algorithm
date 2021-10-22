T = int(input())

dd = [(0,0),(0,-1),(1,0),(0,1),(-1,0)]
for test in range(1,T+1):
    M,A = map(int,input().split())
    user1 = list(map(int,input().split()))
    user2 = list(map(int,input().split()))

    battery, sol = {}, 0
    for i in range(A):
        x,y,c,p = map(int,input().split())
        x,y = x-1,y-1
        battery[(x,y)] = [(i,p)]
        q,check,cnt = [(x,y)], {(x,y):1},0
        while q:
            cnt += 1
            Next = []
            for v in q:
                for k in range(1,5):
                    nx,ny = v[0]+dd[k][0], v[1]+dd[k][1] 
                    if 0 <= nx < 10 and 0 <= ny < 10 and (nx,ny) not in check:
                        if (nx,ny) not in battery:
                            battery[(nx,ny)] = [(i,p)]
                        else:
                            battery[(nx,ny)].append((i,p))
                        Next.append((nx,ny))
                        check[(nx,ny)] = 1
            q = Next
            if cnt == c:
                break
    [battery[b].sort(key = lambda x: x[1]) for b in battery]

    x1,y1,x2,y2 = 0,0,9,9
    if (x1,y1) in battery:
        sol += battery[(x1,y1)][-1][1]
    if (x2,y2) in battery:
        sol += battery[(x2,y2)][-1][1]

    for m in range(M):
        d1,d2 = user1[m],user2[m]
        x1,y1,x2,y2 = x1+dd[d1][0], y1+dd[d1][1], x2+dd[d2][0], y2+dd[d2][1]

        if (x1,y1) in battery and (x2,y2) in battery:
            if (x1,y1) == (x2,y2):
                mp = battery[(x1,y1)]
                if len(mp) < 2:
                    sol += mp[-1][1]
                else:
                    sol += (mp[-1][1] + mp[-2][1])
            else:
                mp1 = battery[(x1,y1)]
                mp2 = battery[(x2,y2)]

                if len(mp1) == len(mp2) == 1:
                    if mp1[-1][0] == mp2[-1][0]:
                        sol += mp1[-1][1]
                    else:
                        sol += (mp1[-1][1] + mp2[-1][1])
                else:
                    if mp1[-1][0] == mp2[-1][0]:
                        if len(mp1) > 1 and len(mp2) > 1:
                            sol += (mp1[-1][1] + max(mp1[-2][1], mp2[-2][1]))
                        elif len(mp1) > 1 and not len(mp2) > 1:
                            sol += (mp2[-1][1] + mp1[-2][1])
                        elif not len(mp1) > 1 and len(mp2) > 1:
                            sol += (mp1[-1][1] + mp2[-2][1])
                    else:
                        sol += (mp1[-1][1] + mp2[-1][1])
        elif (x1,y1) in battery and (x2,y2) not in battery:
            sol += battery[(x1,y1)][-1][1]
        elif (x1,y1) not in battery and (x2,y2) in battery:
            sol += battery[(x2,y2)][-1][1]
        

    print("#%d %d"%(test, sol))

# 1
# 11 2
# 2 2 2 2 2 2 2 2 2 0 4
# 1 1 1 1 1 1 1 1 1 3 0
# 10 1 2 10
# 9 2 1 20

