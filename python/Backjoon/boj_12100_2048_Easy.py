import sys
read = sys.stdin.readline

N = int(read())

mat_ = []
for i in range(N):
    mat_.append(list(map(int,read().split())))

direction = [0,1,2,3]
pool = []
def dfs(arr,before,depth):
    if depth == 5:
        yield pool
        return

    for i in arr:
        pool.append(i)
        for next in dfs(arr,i,depth+1):
            yield next
        pool.pop()

def merge(arr, rev = False): # arr를 받아서 연산후 되돌려주는 함수
    a = []
    if rev == True:
        fg = 0
        bef = arr[N-1]
        for i in range(N,0,-1):
            if fg == 1:
                fg = 0
                continue
            if arr[i-1] == 0:
                continue
            if bef == arr[i-2]:
                bef = 0
                if i-2 == -1:
                    a = [arr[i-1]] + a
                    continue
                a = [arr[i-1]*2] + a
                fg = 1
            else:
                bef = arr[i-2]
                a = [arr[i-1]] + a
        if len(a) != N:
            a = [0]*(N-len(a)) + a
    else:
        fg = 0
        bef = arr[0]
        for i in range(N):
            if arr[i] == 0:
                continue
            if fg == 1:
                fg = 0
                continue
            if bef == arr[i]:
                if i == 0:
                    continue
                bef = 0
                if i == N:
                    a = a + [arr[i]]
                    continue
                a = a + [arr[i]*2]
                fg = 1
            else:
                if i == N-1 or arr[i+1] == 0:
                    continue
                bef = arr[i]
                a = a + [arr[i]]
        if len(a) != N:
            a = a + [0]*(N-len(a))
    return a

sol = []
for step in dfs(direction,5,0):
    mat = []
    for m in mat_:
        mat.append(m.copy())
    for d_ in step:
        if d_ == 0: # 상 기울이기 == 좌 기울이기
            cnt = 0
            for m in zip(*mat):
                arr = merge(m,rev=False)
                for i in range(len(arr)):
                    mat[i][cnt] = arr[i]
                cnt += 1

        if d_ == 1: # 하
            cnt = 0
            for m in zip(*mat):
                arr = merge(m,rev=True)
                for i in range(len(arr)):
                    mat[i][cnt] = arr[i]
                cnt += 1

        if d_ == 2: # 좌
            cnt = 0
            for m in mat:
                arr = merge(m,rev=False)
                for i in range(len(arr)):
                    mat[cnt][i] = arr[i]
                cnt+=1
        if d_ == 3: # 우
            cnt = 0
            for m in mat:
                arr = merge(m,rev=True)
                for i in range(len(arr)):
                    mat[cnt][i] = arr[i]
                cnt+=1
    M = 0
    for m in mat:
        Max = max(m)
        if M < Max:
            M = Max
    sol.append(M)
    break

print(max(sol))

