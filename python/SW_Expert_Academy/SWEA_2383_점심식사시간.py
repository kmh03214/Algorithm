from itertools import combinations
T = int(input())

def divide(persons ,stair1,stair2):
    for r in range(len(persons)+1):
        for combi in combinations(persons,r):
            div1, div2 = list(combi), list(set(persons).difference(set(combi)))
            s1,s2 = [],[]
            for p in div1:
                s1.append(abs(p[0]-stair1[0])+abs(p[1]-stair1[1]))
            for p in div2:
                s2.append(abs(p[0]-stair2[0])+abs(p[1]-stair2[1]))
            yield sorted(s1), sorted(s2)

def down_stair(wait,stair_num,down):
    Next = []
    for p in wait:
        if p == time:
            down.append([stair_num[2],-1])
        else:
            Next.append(p)
    wait = Next
    return wait,down

def go_down(down):
    tmp = []
    for i in range(min(len(down),3)):
        down[i][1] += 1
        if down[i][0] == down[i][1]:
            tmp.append(down[i])
    cnt = 0
    for t in tmp:
        down.remove(t)
        cnt += 1
    for i in range(min(3,len(down))):
        if down[i][1] == -1:
            down[i][1] += 1

    return down

for test in range(1,T+1):
    N = int(input())
    person, stair, sol = [], [], 1000000000
    for i in range(N):
        a = list(map(int, input().split()))
        for j in range(N):
            if a[j] == 1:
                person.append((i,j))
            if a[j] > 1:
                stair.append((i,j,a[j]))

    for s1, s2 in divide(person,stair[0],stair[1]):
        time, down1, down2 = 0, [], []
        # s1,s2 = [2,2,2,3],[2,2]
        while True:
            down1 = go_down(down1)
            down2 = go_down(down2)
            time += 1
            if not down1 and not down2 and not s1 and not s2:
                sol = min(sol,time)
                break
            s1, down1 = down_stair(s1,stair[0],down1)
            s2, down2 = down_stair(s2,stair[1],down2)
            if not down1 and not down2 and not s1 and not s2:
                sol = min(sol,time)
                break
    print('#%d %d'%(test, sol))


