import sys
read = sys.stdin.readline
N,K = map(int,read().split())
pots = [int(read()) for i in range(N)]

low, high = 1, max(pots)+1
mid = float('inf')

while low+1 < high:
    mid = (low+high)//2
    s = sum(p//mid for p in pots)    
    if s < K:
        high = mid
    else:
        low = mid

print(mid)
