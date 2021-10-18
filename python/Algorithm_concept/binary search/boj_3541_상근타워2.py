import sys
read = sys.stdin.readline

n,m = map(int,read().split())
sol = float('inf')
for i in range(m):
    u,d = map(int,read().split())
    x = ((d*n)//(u+d) + 1)
    sol = min(sol, u*x-d*(n-x))
print(sol)