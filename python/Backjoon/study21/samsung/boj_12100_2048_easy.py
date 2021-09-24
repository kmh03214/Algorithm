import sys
from itertools import product

read = sys.stdin.readline
N = int(read())
mat = []
for i in range(N):
    mat.append(list(map(int,read().split())))

# N <= 20
def move(arr,reverse):
    if reverse:
        arr.reverse()
    bef, ret = 0, []
    for i in range(len(arr)):
        if arr[i] == 0:
            continue
        if bef == arr[i]:
            ret.append(2*bef)
            bef = 0
            continue
        elif bef:
            ret.append(bef)
        bef = arr[i]
    ret += [bef] + [0]*(N-len(ret)-1)
    if reverse:
        ret.reverse()
        return ret
    return ret

sol = 0
for prod in product([0,1,2,3], repeat = 5):
    m = []
    for a in mat:
        m.append(a.copy())
    
    for d in prod:
        Next = []
        if d%2 == 0:
            for arr in m:
                if d == 0:
                    Next.append(move(arr,1))
                else:
                    Next.append(move(arr,0))
        else:
            for arr in zip(*m):
                if d == 1:
                    Next.append(move(list(arr),1))
                else:
                    Next.append(move(list(arr),0))
            Next = [list(a) for a in zip(*Next)]
        m = Next
    sol = max(sol,max([max(arr) for arr in m]))
print(sol)