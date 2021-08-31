import sys
read = sys.stdin.readline
N,M,K = map(int, read().split())
arr = list(map(int,read().split()))

arr.sort()

rep,sol = 0,0
for i in range(M):
    if rep < K:
        sol += arr[-1]
        rep += 1
    else:
        sol += arr[-2]
        rep = 0
print(sol)



