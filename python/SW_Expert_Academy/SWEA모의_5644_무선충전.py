d = [(0,0),(0,-1),(1,0),(0,1),(-1,0)] # 그대로, 상,우,하,좌
def make_bcs(x,y,cc,p):
    q = [(x,y)]
    bc = {(x,y):p}
    cnt = 0
    while q:
        Next = []
        cnt += 1
        for v in q:
            r,c = v[0],v[1]
            for i in range(1,5):
                nx,ny = r + d[i][0], c + d[i][1]
                if 0<= nx < 10 and 0 <= ny < 10 and (nx,ny) not in bc:
                    bc[(nx,ny)] = p
                    Next.append((nx,ny))
        q = Next
        if cnt == cc:
            break
    return bc
def charge(Apos,Bpos,BCS):
    A, B = [], []
    for BC in BCS:
        a,b = 0,0
        if Apos in BC:
            a = BC[Apos]
        if Bpos in BC:
            b = BC[Bpos]
        A.append(a)
        B.append(b)
    # 완탐
    ret = []
    for i in range(len(A)):
        for j in range(len(B)):
            if i == j and A[i] == B[j]:
                a = A[i] // 2
                ret.append((a,a))
            else:
                ret.append((A[i],B[j]))
    ret.sort(key = lambda x : x[0]+x[1])
    maxA,maxB = ret[-1][0],ret[-1][1]
    return maxA, maxB

T = int(input())

for test in range(T):

    M,A = map(int,input().split())
    a_pos , userA = (0,0), list(map(int,input().split()))
    b_pos , userB = (9,9), list(map(int,input().split()))

    BCS = []

    for i in range(A):
        x,y,cc,p = map(int,input().split()) # ap 정보
        BCS.append(make_bcs(x-1,y-1,cc,p))
    
    a_charge, b_charge = charge(a_pos,b_pos,BCS)
    for i in range(M):
        dir_a, dir_b = d[userA[i]], d[userB[i]]
        a_pos, b_pos = (a_pos[0]+dir_a[0],a_pos[1]+dir_a[1]),(b_pos[0]+dir_b[0], b_pos[1]+dir_b[1])
        tmpa,tmpb = charge(a_pos,b_pos,BCS)
        a_charge += tmpa
        b_charge += tmpb
    
    print('#%d %d'%(test, a_charge+b_charge))







# 1
# 20 3
# 2 2 3 2 2 2 2 3 3 4 4 3 2 2 3 3 3 2 2 3
# 4 4 1 4 4 1 4 4 1 1 1 4 1 4 3 3 3 3 3 3
# 4 4 1 100
# 7 10 3 40
# 6 3 2 70


