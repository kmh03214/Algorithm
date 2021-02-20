import sys
read = sys.stdin.readline
R,C,M = map(int,read().split())

# mat = [[0 for i in range(C)] for j in range(R)]
# shark = []
# for i in range(M):
#     r,c,s,d,z = map(int,read().split())
#     mat[r-1][c-1] = (s,d,z)
#     shark.append((r-1,c-1))

def move(r,c,s,d,z):
    if d == 1 or d == 3:
        s %= ((R-1)*2)
        r = r + ((R-1)*2 - s)
        q, r = r // ((R-1)*2), r % ((R-1)*2) # 몫, 나머지
        if q%2 == 1:
            d = (d+2)%4

    if d == 2 or d == 4:
        s %= ((C-1)*2)
        c = c + ((C-1)*2 - s)
        
        print(s,c)
        q = c // (C-1) # 몫, 나머지
        
        if q%2 == 1:
            c -= c%(C-1)

            d = (d+2)%4
            if d == 0:
                d = 4
    return r,c,s,d,z

r,c,s,d,z = 1,3,8,4,1
for i in range(2):
    r,c,s,d,z = move(r,c,s,d,z)
    print(r,c,s,d,z)




