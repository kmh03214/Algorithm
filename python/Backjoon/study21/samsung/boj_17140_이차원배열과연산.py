r,c,k = map(int,input().split())
mat, time, fg = [list(map(int, input().split())) for i in range(3)], 0, 0

def oper(arr):
    tmp,ret = {},[]
    for i in range(len(arr)):
        if arr[i] not in tmp:
            tmp[arr[i]] = 1
        else:
            tmp[arr[i]] += 1
    if 0 in tmp:
        del tmp[0]
    for x,y in sorted(tmp.items(), key = lambda x:(x[1],x[0])):
        ret.append(x)
        ret.append(y)
    if len(ret) > 100:
        return ret[:100]
    else:
        return ret

while time < 100:
    if r-1 < len(mat) and c-1 < len(mat[0]) and mat[r-1][c-1] == k:
        fg = 1
        break
    time += 1
    next_mat, max_len = [], 0

    if len(mat) >= len(mat[0]): # R연산    
        for m in mat:
            a = oper(m)
            max_len = max(max_len,len(a))
            next_mat.append(a)
        mat = [m + [0]*(max_len-len(m)) for m in next_mat]
    else:
        for m in zip(*mat):
            a = oper(m)
            max_len = max(max_len,len(a))
            next_mat.append(a)
        mat = [mm for mm in zip(*[m + [0]*(max_len-len(m)) for m in next_mat])]

if fg:
    print(time)
else:
    print(-1)

