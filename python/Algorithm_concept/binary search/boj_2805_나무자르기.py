N,M = map(int,input().split()) # N < 100만 / M < 20억
trees = sorted(list(map(int, input().split())))
low, high, mid = 0, 2*trees[-1], -1
while low <= high:
    mid = (low + high)//2
    S = sum([max(0,tree-mid) for tree in trees])
    if S < M:
        high = mid-1
    else:
        low = mid+1
print(high)
