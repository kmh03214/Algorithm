import sys
read = sys.stdin.readline

for test in range(10):
    n = int(read())
    arr = list(map(int,read().split()))
    sol = 0

    for i in range(2,n-2):
        cnt = min(arr[i]-arr[i-1],arr[i]-arr[i-2],arr[i]-arr[i+1],arr[i]-arr[i+2])
        if cnt <= 0:
            continue
        sol += cnt
    
    print('#%d'%(test+1), sol)

