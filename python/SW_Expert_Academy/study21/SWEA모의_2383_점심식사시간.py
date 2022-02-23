def down(num,persons):
    sx,sy = stairs[num]
    length, time = mat[sx][sy], 0
    arrive_time = sorted([abs(sx-px)+abs(sy-py) for px,py in persons], reverse=True)
    q = []
    while True:
        time += 1
        if q and q[0] == time:
            fg = 0
            for i in range(len(q)):
                if q[i] != time:
                    fg = 1
                    q = q[i:]
                    break
            if not fg:
                q = []
        while arrive_time and len(q) < 3 and arrive_time[-1] < time:
            p = arrive_time.pop()
            q.append(time+length)
        if len(arrive_time) == 0 and len(q)==0:
            return time
    return time

def powerset(s): # [1,2,3,4,5]
    masks = [1 << i for i in range(len(s))] # 1 10 100 1000 10000
    for i in range(1 << len(s)): # 2^N
        yield [ss for mask,ss in zip(masks,s) if mask&i], [ss for mask,ss in zip(masks,s) if not mask&i]

T = int(input())

for test in range(1,T+1):
    N = int(input())
    mat, persons, stairs = [],[],[]
    for i in range(N):
        a = list(map(int,input().split()))
        for j in range(N):
            if a[j] == 1:
                persons.append((i,j))
            if 2 <= a[j]:
                stairs.append((i,j))
        mat.append(a)
    sol = float('inf')
    
    for s1,s2 in powerset(persons):
        for num in range(2):
            sol = min(sol,max(down(num%2, s1),down((num+1)%2,s2)))
    print("#%d %d"%(test, sol))