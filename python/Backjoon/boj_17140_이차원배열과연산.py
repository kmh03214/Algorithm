import sys
read = sys.stdin.readline
r,c,k = map(int,read().split())
mat = []
for i in range(3):
    mat.append(list(map(int,read().split())))

def oper(arr):
    new_arr, cnt_dict = [],{}
    for num in arr:
        if num == 0:
            continue
        if num not in cnt_dict:
            cnt_dict[num] = 1
        else:
            cnt_dict[num] += 1

    for num,cnt in sorted(cnt_dict.items(), key= lambda x: (x[1],x[0])):
        new_arr.append(num)
        new_arr.append(cnt)
        if len(new_arr) == 100:
            break
    return new_arr

time = 0
while True:
    if time > 53:
        print(-1)
        break
    try:
        if mat[r-1][c-1] == k:
            print(time)
            break
    except:
        pass

    time += 1
    new_mat = []
    long_len = 0

    if len(mat) >= len(mat[0]): # 행 >= 열
        for m in mat:
            new_array = oper(m)
            new_mat.append(new_array)
            if long_len < len(new_array):
                long_len = len(new_array)
        for i in range(len(new_mat)):
            new_mat[i] += [0]*(long_len - len(new_mat[i]))
        mat = new_mat
    else:
        for m in (zip(*mat)):
            new_array = oper(m)
            new_mat.append(new_array)
            if long_len < len(new_array):
                long_len = len(new_array)
        for i in range(len(new_mat)):
            new_mat[i] += [0]*(long_len - len(new_mat[i]))
        n_mat = []
        for m in (zip(*new_mat)):
            n_mat.append(m)
        mat = n_mat
            




    

