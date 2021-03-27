import sys
read = sys.stdin.readline
N = int(read())
mat = []
for i in range(N):
    mat.append(list(map(int,read().split())))

sol = []
def dnq(m,N):
    # 모두 같은색인지 검사
    tmp,div = m[0][0], 0
    for i in range(N):
        for j in range(N):
            if tmp != m[i][j]: # 다른게 등장한다면, 분할하여 전달한다.
                div = 1
                break
    if div:
        mid = N//2
        m1,m2,m3,m4 = [i[:mid] for i in m[:mid]],[i[mid:] for i in m[:mid]], [ i[:mid] for i in m[mid:] ], [ i[mid:] for i in m[mid:]]
        r1,r2,r3,r4 = dnq(m1,mid), dnq(m2,mid), dnq(m3,mid), dnq(m4,mid)
        sol.extend([r1,r2,r3,r4])
    else: # 나누지 않았다면
        return tmp # 칼라
    
    return sol.count(0), sol.count(1)

tmp,fg = mat[0][0],0
for i in range(N):
    for j in range(N):
        if tmp != mat[i][j]: # 다른게 등장한다면, 분할하여 전달한다.
            fg = 1
            break

if fg == 1:
    a,b = dnq(mat,N)
    print(a)
    print(b)
else:
    if mat[0][0]:
        print(0)
        print(1)
    else:
        print(1)
        print(0)



