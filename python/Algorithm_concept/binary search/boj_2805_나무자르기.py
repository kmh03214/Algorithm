import sys 
N,M = map(int,sys.stdin.readline().split())
trees = sorted(list(map(int, sys.stdin.readline().split())))


# N,M = map(int,input().split()) # N < 100만 / M < 20억
# trees = sorted(list(map(int, input().split())))
low, high, mid = 0, 2*trees[-1], -1
while low <= high:
    mid = (low + high)//2
    S = sum([tree-mid if tree-mid > 0 else 0 for tree in trees])
    if S < M:
        high = mid-1
    else:
        low = mid+1
print(high)



S[k] => k번째 계단에서 최대로 얻을 수 있는 점수.

S[k] = 100

1 -> K -> -> ->
2 -> return K

# DP => Memo // memoization
# dictionary / list.. O(1)