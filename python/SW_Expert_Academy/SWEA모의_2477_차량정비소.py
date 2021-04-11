
T = int(input())
for test in range(1,T+1):
    N,M,K,A,B = map(int,input().split())
    recept = [[0,t,0] for t in map(int,input().split())]
    repair = [[0,t,0] for t in map(int,input().split())]
    time = list(map(int,input().split()))

    t = min(time)
    start = 0
    history = {}
    q1, q2 = [], []
    while K:
        for num in range(start,len(time)): # 고객번호
            tt = time[num]
            if t == tt:
                q1.append(num)
            else:
                start = num
                break        
        q1.sort()
        for i in range(len(recept)):
            r = recept[i]
            if r[0] == 0:
                if q1:
                    r[0],r[2], q1 = 1,q1[0], q1[1:]
                    history[r[2]+1] = [i+1]
            else:
                r[0] += 1
            if r[0] == r[1]:
                r[0] = 0
                q2.append(r[2]) # 고객 number
        
        for i in range(len(repair)):
            r = repair[i]
            if r[0] == 0:
                if q2:
                    r[0],r[2],q2 = 1,q2[0],q2[1:]
                    history[r[2]+1].append(i+1)
            else:
                r[0] += 1
            if r[0] == r[1]:
                r[0] = 0
                K -= 1
        t += 1
    sol = 0
    for k in history:
        if history[k] == [A,B]:
            sol+= k

    print('#%d %d'%(test,sol))


