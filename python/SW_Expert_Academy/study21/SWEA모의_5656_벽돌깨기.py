from itertools import combinations_with_replacement

dd = [(0,1),(1,0),(0,-1),(-1,0)]
def drop_the_beat(mat_c, x):
    target = []
    for h in range(H):
        if mat_c[h][x]:
            target.append((h,x))
            break
    if not target:
        return mat_c
    check = {target[0]:1}
    while target:
        Next = []
        for v in target:
            L = mat_c[v[0]][v[1]]-1
            for i in range(4):
                for j in range(L):
                    nx,ny = v[0]+ (j+1)*dd[i][0], v[1]+(j+1)*dd[i][1]
                    if 0 <= nx < H and 0<= ny < W and (nx,ny) not in check and mat_c[nx][ny] != 0:
                        Next.append((nx,ny))
                        check[(nx,ny)] = 1
        target = Next
    for ch in check:
        mat_c[ch[0]][ch[1]] = 0

    next_mat = []
    for m in zip(*mat_c):
        arr = [i for i in m if i != 0]
        next_mat.append([0]*(H-len(arr)) + arr)
    return [list(m) for m in zip(*next_mat)]

T = int(input())
for test in range(1,T+1):
    N,W,H = map(int,input().split())
    mat, arr, sol = [list(map(int,input().split())) for i in range(H)], [i for i in range(W)], W*H

    for combi in combinations_with_replacement(arr,N):
        combi = [2,2,6]
        mat_c = [m.copy() for m in mat]
        for c in combi:
            mat_c = drop_the_beat(mat_c, c)
        
        sol = min(sol,sum([W-m.count(0) for m in mat_c]))


    print("#%d %d"%(test,sol))
