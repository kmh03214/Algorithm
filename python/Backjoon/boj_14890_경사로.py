import sys
read = sys.stdin.readline
N, L = map(int, read().split())
mat = []
for i in range(N):
    a = list(map(int,read().split()))
    mat.append(a)

def is_road(arr):
    try:
        before = 1
        for i in range(N-1):
            if arr[i] - arr[i+1] == 0:
                before += 1
                continue        
            elif arr[i] - arr[i+1] == -1:
                if before >= L:
                    before = 1
                    continue
                else:
                    return 0
            elif arr[i] - arr[i+1] == 1:
                for j in range(L):
                    if arr[i+j+1] != arr[i+1]:
                        return 0
                before = -L+1
                continue
            else:
                return 0
        return 1
    except:
        return 0
sol = 0
for i in range(N):
    sol += is_road(mat[i])
    sol += is_road(list(zip(*mat))[i])
print(sol)