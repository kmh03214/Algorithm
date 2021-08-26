import sys
read = sys.stdin.readline
direct = {}
N = int(read())
for i in range(1,9):
    direct[i] = list(map(int,read().split()))

arr = []
tmp = {}
order = []
for i in range(N):
    a = tuple(map(int,read().split()))
    if a[1] != 0:
        arr.append(a)
    else:
        arr.append(0)
        tmp[i] = [(a[0],i) for i in range(1,5)]
        order.append(i)
arr1 = []
arr2 = []
arr3 = []
arr4 = []
for o in order:
    if not arr1:
        arr1 = tmp[o]
        continue
    if not arr2:
        arr2 = tmp[o]
        continue
    if not arr3:
        arr3 = tmp[o]
        continue
    if not arr4:
        arr4 = tmp[o]
        continue
if not arr1:
    arr1 = [()]
if not arr2:
    arr2 = [()]
if not arr3:
    arr3 = [()]
if not arr4:
    arr4 = [()]
from itertools import product
iterator = []
if arr1 != [()]:
    for pro in product(arr1,arr2,arr3,arr4,repeat = 1):
        arr_c = arr.copy()
        for o in range(len(order)):
            p = pro[o]
            idx = order[o]
            arr_c[idx] = p
        iterator.append(arr_c)
else:
    iterator = [arr]

sol = []

def block_drop(mat,block):
    global score
    num,pos = block
    pos -= 1
    for i in range(len(mat)):
        if mat[-i-1][pos] == 0:
            mat[-i-1][pos] = num
        else:
            tmp = [0,0,0,0]
            tmp[pos] = num
            mat = [tmp] + mat
    if mat[-1].count(0) == 0:
        score += 1
        mat.pop()
        if len(mat) == 0:
            mat = [[0,0,0,0]]
    return mat
dd = [0,(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
def move_block(mat):
    mat = [[0,0,0,0]] + mat
    next_mat = [[0,0,0,0] for i in range(len(mat))]
    for i in range(len(mat)):
        for j in range(4):
            if mat[i][j] != 0:
                for k in direct[mat[i][j]]:
                    d = dd[k]
                    nr,nc = i + d[0], j + d[1]
                    if 0<= nr < len(mat) and 0<= nc < 4:
                        if next_mat[nr][nc] != 0 and mat[i][j] > next_mat[nr][nc]:
                            next_mat[nr][nc] = mat[i][j]
                        elif next_mat[nr][nc] == 0:
                            next_mat[nr][nc] = mat[i][j]
                        break
    nn_mat = [[0,0,0,0] for i in range(len(next_mat))]
    for j in range(4):
        tmp = []
        for i in range(len(next_mat)):
            if next_mat[-i-1][j] != 0:
                tmp.append(next_mat[-i-1][j])
        for i in range(len(tmp)):
            nn_mat[-i-1][j] = tmp[i]
    global score

    while nn_mat[0].count(0) == 4:
        nn_mat.pop(0)
        if len(nn_mat) == 0:
            nn_mat = [[0,0,0,0]]
            break
    while nn_mat[-1].count(0) == 0:
        nn_mat.pop()
        score += 1
        if len(nn_mat) == 0:
            nn_mat = [[0,0,0,0]]
            break
    return nn_mat
sol = []
for iter in iterator:
    mat = [[0,0,0,0]]
    score = 0
    for block in iter:
        mat = block_drop(mat,block)
        mat = move_block(mat)
    sol.append(score)
    print(mat)
print(max(sol))




