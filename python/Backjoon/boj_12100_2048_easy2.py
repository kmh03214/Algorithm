import sys
read = sys.stdin.readline
N = int(read())
mat = []
for i in range(N):
    mat.append(list(map(int,read().split())))

def product(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in product(arr,r-1):
                yield next + [arr[i]]
def left():
    n_mat = []
    for ma in mat:
        m = []
        for e in ma:
            if e:
                m.append(e)
        arr = []
        bef = 0
        for i in range(len(m)):
            if bef == 0:
                bef = m[i]
                if i == len(m) - 1:
                    arr.append(bef)
            else:
                if bef == m[i]:
                    arr.append(2*bef)
                    bef = 0
                else:
                    arr.append(bef)
                    bef = m[i]
                    if bef != 0:
                        bef = m[i]
                        if i == len(m)-1:
                            arr.append(bef)
        n_mat.append(arr + (N-len(arr))*[0])
    return n_mat
def right():
    n_mat = []
    for ma in mat:
        m = []
        for e in ma:
            if e:
                m.append(e)
        m.reverse()
        arr = []
        bef = 0
        for i in range(len(m)):
            if bef == 0:
                bef = m[i]
                if i == len(m) - 1:
                    arr.append(bef)
            else:
                if bef == m[i]:
                    arr.append(2*bef)
                    bef = 0
                else:
                    arr.append(bef)
                    bef = m[i]
                    if bef != 0:
                        bef = m[i]
                        if i == len(m)-1:
                            arr.append(bef)
        arr.reverse()
        n_mat.append((N-len(arr))*[0] + arr)
    return n_mat

def up():
    n_mat = [[0 for i in range(N)] for j in range(N)]
    for k in range(N):
        m = []
        for j in range(N):
            if mat[j][k]:
                m.append(mat[j][k])
        arr = []
        bef = 0
        for i in range(len(m)):
            if bef == 0:
                bef = m[i]
                if i == len(m) - 1:
                    arr.append(bef)
            else:
                if bef == m[i]:
                    arr.append(2*bef)
                    bef = 0
                else:
                    arr.append(bef)
                    bef = m[i]
                    if bef != 0:
                        bef = m[i]
                        if i == len(m)-1:
                            arr.append(bef)
        for j in range(len(arr)):
            n_mat[j][k] = arr[j]
    return n_mat

def down():
    n_mat = [[0 for i in range(N)] for j in range(N)]
    for k in range(N):
        m = []
        for j in range(N):
            if mat[j][k]:
                m.append(mat[j][k])
        m.reverse()
        arr = []
        bef = 0
        for i in range(len(m)):
            if bef == 0:
                bef = m[i]
                if i == len(m) - 1:
                    arr.append(bef)
            else:
                if bef == m[i]:
                    arr.append(2*bef)
                    bef = 0
                else:
                    arr.append(bef)
                    bef = m[i]
                    if bef != 0:
                        bef = m[i]
                        if i == len(m)-1:
                            arr.append(bef)
        for j in range(len(arr)):
            n_mat[-j-1][k] = arr[j]
    return n_mat
sol = 0
mat_c = []
for m in mat:
    mat_c.append(m.copy())
for pro in product([1,2,3,4],5):
    for d in pro:
        if d == 1:
            mat = left()
        if d == 2:
            mat = right()
        if d == 3:
            mat = up()
        if d == 4:
            mat = down()
    for m in mat:
        M = max(m)
        if sol < M:
            sol = M
    mat = []
    for m in mat_c:
        mat.append(m.copy())
print(sol)