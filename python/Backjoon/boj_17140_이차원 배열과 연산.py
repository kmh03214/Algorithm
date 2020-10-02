import sys
read = sys.stdin.readline

r,c,k = map(int,read().split())
mat = [list(map(int,read().split())) for i in range(3)]

def oper(lis):
    num_cnt = [[i,0] for i in range(101)] # 최대길이 100이라 100이상 숫자갯수가 안나옴
    for i in range(len(lis)):
        num_cnt[lis[i]][1] += 1
    num_cnt.sort(key = lambda x: (x[1],x[0]))
    s = []
    for i in num_cnt:
        if i[0] == 0:
            continue
        if i[1] != 0:
            s.append(i[0])
            s.append(i[1])
    return s

def operation(mat):
    for time in range(101):
        try:
            if mat[r-1][c-1] == k:
                return time
        except:
            pass
        
        if len(mat) >= len(mat[0]): # 행 >= 열 -> R연산 모든 행에 대해
            next_mat = []
            for i in range(len(mat)):
                next_mat.append(oper(mat[i]))

            ml = len(max(next_mat, key= lambda x:len(x)))
            mat = [next_mat[i]+[0]*(ml-len(next_mat[i])) for i in range(len(next_mat))]             
        else: # 행 < 열 -> C연산
            mat = [list(i) for i in zip(*mat)] # Transpose 연산
            next_mat = []

            for i in range(len(mat)):
                next_mat.append(oper(mat[i]))

            ml = len(max(next_mat, key= lambda x:len(x)))
            mat = [next_mat[i]+[0]*(ml-len(next_mat[i])) for i in range(len(next_mat))]
            mat = [list(i) for i in zip(*mat)]
    return -1
print(operation(mat))