import sys
read = sys.stdin.readline
N = int(read())
mat = []
for i in range(N):
    mat.append(list(map(int,read().split())))
def check(r,c,l): # mat에서 해당 좌표가 모두 같은 수인지 확인하는 함수
    s = mat[r][c]
    for i in range(l):
        for j in range(l):
            if mat[r+i][c+j] != s:
                return 'FAIL'
    return s
sol = {-1:0,0:0,1:0}
def dnq(r,c,l):
    ret = check(r,c,l)
    if ret != 'FAIL':
        sol[ret] += 1
        return
    else:
        l = l//3 # 0 3 6
        for i in range(3):
            for j in range(3):
                dnq(r+(i*l), c+(j*l),l)
                
    
dnq(0,0,N)
print(sol[-1])
print(sol[0])
print(sol[1])
