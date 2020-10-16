def rotation_90(arr):
    return [list(reversed(a)) for a in zip(*arr)]

test = int(input())
for t in range(test):
    N = int(input())
    mat = []
    for i in range(N):
        mat.append(list(map(int,input().split())))
    
    mat_ = []
    for i in range(3):
        if mat_:
            mat_.append(rotation_90(mat_[i-1]))
        else:
            mat_.append(rotation_90(mat))
    print("#%d"%(t+1))
    for i in range(N):
        for j in range(3):
            for k in range(N):
                print(mat_[j][i][k], end='')
            print(' ', end ='')
        print()

    
# ###
# 1
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# ###