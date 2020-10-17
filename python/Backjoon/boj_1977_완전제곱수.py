M = int(input())
N = int(input())
sol_min = 0
for i in range(M,N+1):
    if (i**0.5%1) == 0:
        sol_min = int(i**0.5)
        break
t,sol_sum = sol_min,0
if not sol_min:
    print(-1)
else:
    while t**2 <= N:
        sol_sum += t**2
        t+=1
    print(sol_sum)
    print(sol_min**2)