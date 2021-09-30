import sys
read = sys.stdin.readline
N,L = map(int,read().split())
mat = [list(map(int,read().split())) for i in range(N)]

def possible(arr):
    bef, cnt = arr[0], 1
    for i in range(1, len(arr)):
        if bef == arr[i]:
            cnt += 1
        else:
            if bef == arr[i] - 1: # 오른쪽이 더 높다.
                if cnt >= L:
                    cnt, bef = 1, arr[i]
                    continue
                else:
                    return 0
                
            elif bef == arr[i] + 1:
                try:
                    for j in range(i, i+L):
                        if arr[j] != arr[i]:
                            return 0
                    cnt = -L+1
                    bef = arr[i]
                except:
                    return 0
            else:
                return 0
    return 1
sol = 0
for m in mat:
    sol += possible(m)

for m in zip(*mat):
    sol += possible(m)
print(sol)

