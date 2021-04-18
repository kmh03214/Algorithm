for test in range(1,11):
    sol = 0
    dumps = int(input())
    arr = list(map(int,input().split()))
    for d in range(dumps):
        M_idx = arr.index(max(arr))
        m_idx = arr.index(min(arr))
        arr[M_idx]-=1
        arr[m_idx]+=1
    print("#%d %d"%(test,max(arr)-min(arr)))