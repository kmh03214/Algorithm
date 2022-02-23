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
        if (x,y) not in battery:
            battery[(x,y)] = [(i,p)]
        else:
            battery[(x,y)].append((i,p))
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

# d = [(0,0),(0,-1),(1,0),(0,1),(-1,0)] # 그대로, 상,우,하,좌
# def make_bcs(x,y,cc,p):
#     q = [(x,y)]
#     bc = {(x,y):p}
#     cnt = 0
#     while q:
#         Next = []
#         cnt += 1
#         for v in q:
#             r,c = v[0],v[1]
#             for i in range(1,5):
#                 nx,ny = r + d[i][0], c + d[i][1]
#                 if 0<= nx < 10 and 0 <= ny < 10 and (nx,ny) not in bc:
#                     bc[(nx,ny)] = p
#                     Next.append((nx,ny))
#         q = Next
#         if cnt == cc:
#             break
#     return bc
# def charge(Apos,Bpos,BCS):
#     A, B = [], []
#     for BC in BCS:
#         a,b = 0,0
#         if Apos in BC:
#             a = BC[Apos]
#         if Bpos in BC:
#             b = BC[Bpos]
#         A.append(a)
#         B.append(b)
#     # 완탐
#     ret = []
#     for i in range(len(A)):
#         for j in range(len(B)):
#             if i == j and A[i] == B[j]:
#                 a = A[i] // 2
#                 ret.append((a,a))
#             else:
#                 ret.append((A[i],B[j]))
#     ret.sort(key = lambda x : x[0]+x[1])
#     maxA,maxB = ret[-1][0],ret[-1][1]
#     return maxA, maxB

# T = int(input())

# for test in range(T):

#     M,A = map(int,input().split())
#     a_pos , userA = (0,0), list(map(int,input().split()))
#     b_pos , userB = (9,9), list(map(int,input().split()))

#     BCS = []

#     for i in range(A):
#         x,y,cc,p = map(int,input().split()) # ap 정보
#         BCS.append(make_bcs(x-1,y-1,cc,p))
    
#     a_charge, b_charge = charge(a_pos,b_pos,BCS)
#     for i in range(M):
#         dir_a, dir_b = d[userA[i]], d[userB[i]]
#         a_pos, b_pos = (a_pos[0]+dir_a[0],a_pos[1]+dir_a[1]),(b_pos[0]+dir_b[0], b_pos[1]+dir_b[1])
#         tmpa,tmpb = charge(a_pos,b_pos,BCS)
#         a_charge += tmpa
#         b_charge += tmpb
    
#     print('#%d %d'%(test+1, a_charge+b_charge))
