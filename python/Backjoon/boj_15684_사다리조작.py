import sys
import itertools
read = sys.stdin.readline

N, M, H = map(int,read().split())
ladder = {}
nomi = [(j,i) for i in range(1,N) for j in range(1,H+1)]
for i in range(M):
    a,b = map(int,read().split())
    if (a,b) not in ladder:
        ladder[(a,b)] = 1
        ladder[(a,b+1)] = -1
        nomi.remove((a,b))
        try:
            if b != 1:
                nomi.remove((a,b-1))
            if b+1 != N:
                nomi.remove((a,b+1))
        except:
            continue

def check(ladders):
    for lad in ladders:
        x,y = lad[0],lad[1]
        if (x,y-1) in ladders or (x,y+1) in ladders:
            return 'no'
    return 'yes'


# 사다리 놓기
def ladder_set(ladder,add_ladder):
    a = ladder.copy()
    for lad in add_ladder:
        x,y = lad[0],lad[1]
        a[(x,y)] = 1
        a[(x,y+1)] = -1
    return a

def solution(ladder,cnt):
    for combi in itertools.combinations(nomi,cnt):
        fg = 0
        if check(combi) == 'yes':
            ladder_copy = ladder_set(ladder, combi)
            for i in range(1,N+1):
                ret = go_ladder(ladder_copy,i)
                if ret != i:
                    fg = -1
                    break # 실패
            if fg == -1:
                continue
            return cnt
        else:
            continue

def go_ladder(ladder_copy, start_y):
    y = start_y
    for x in range(1,H+1):
        if (x,y) in ladder_copy:
            y = y+ladder_copy[(x,y)]
    return y

for cnt in range(4):
    flag,flag1 = 0,0
    if cnt == 0:
        for i in range(1,N+1):
            ret = go_ladder(ladder,i)
            if ret != i:
                flag = -1
                break # 실패
        if flag == 0:
            print(cnt)
            flag1 = 1
            break

    if solution(ladder,cnt):
        print(cnt)
        flag1 = 1
        break
if not flag1:
    print(-1)
