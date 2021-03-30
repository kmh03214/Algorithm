from itertools import combinations
test = int(input())

def TEST(mat):
    for arr in zip(*mat):
        before,cnt,fg = arr[0],0,0
        for cur in arr:
            if cur == before:
                cnt+=1
            else:
                cnt = 1
                before = cur
            if cnt == K:
                fg = 1
                break # 해당 열 통과
        if fg == 0:
            return 0 # 통과 못할 때
    return 1 # 마지막까지 통과

for t in range(test):
    D,W,K = map(int,input().split())
    mat = []
    for i in range(D):
        mat.append(list(map(int,input().split())))
    ret,end = TEST(mat), 0
    if ret:
        print('#%d %d'%(t+1,0))
    else:
        for r in range(1,D+1):
            for combi in combinations([i for i in range(D)],r):
                # ex [1,3,5] -> 1 1 1 
                #               1 1 0 / 1 0 1 / 0 1 1
                #               1 0 0 / 0 1 0 / 0 0 1
                #               0 0 0
                memory = {i:mat[i].copy() for i in combi} # 바꿀 row 기억해 놔야 할 듯
                for k in range(len(combi)+1):
                    for combi2 in combinations(combi,k): # 비트마스킹으로하면 쉬울듯
                        combi3 = list(set(combi).difference(set(combi2))) # 차집합
                        for i in combi2:
                            mat[i] = [1]*W
                        for i in combi3:
                            mat[i] = [0]*W
                        if TEST(mat):
                            end = 1
                            print('#%d %d'%(t+1,r))
                            break
                        for i in memory: # 원복
                            mat[i] = memory[i]
                    if end:
                        break
                if end:
                    break
            if end:
                break
