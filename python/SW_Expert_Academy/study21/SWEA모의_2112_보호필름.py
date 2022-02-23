from itertools import combinations
T = int(input())

def powerset(s): # [1,2,3,4,5]
    masks = [1 << i for i in range(len(s))] # 1 10 100 1000 10000
    for i in range(1 << len(s)): # 2^N
        yield [ss for mask,ss in zip(masks,s) if mask&i], [ss for mask,ss in zip(masks,s) if not mask&i]

# D < 13, W <20 (DW = 260)
def test(mat):
    for i in range(W):
        bef,cnt,fg = mat[0][i],0,0
        for j in range(D):
            if mat[j][i] == bef:
                cnt += 1
            else:
                cnt = 1
                bef = mat[j][i]

            if cnt >= K:
                fg = 'unit_pass'
                break
        if fg != 'unit_pass':
            return 0
    return 1

# 13 + 13C2 + 13C3 .... 13C13 = 2^13 = 8192
sol = []
for num in range(T):
    D,W,K = map(int,input().split())
    if K == 1:
        print("#%d %d"%(num+1,1))
        continue

    mat = [list(map(int,input().split())) for i in range(D)]
    arr, end = [i for i in range(D)], 0
    for c in range(D+1):
        for combi in combinations(arr,c):
            for s1,s2 in powerset(combi):
                mat_c = [m.copy() for m in mat]
                for idx in s1:
                    mat_c[idx] = [0]*W
                for idx in s2:
                    mat_c[idx] = [1]*W
                if test(mat_c):
                    end = 1
                    break
            if end:
                break
        if end:
            break
    sol.append(c)
    print("#%d %d"%(num+1,c))

# [2, 0, 4, 2, 2, 0, 3, 2, 3, 4]


