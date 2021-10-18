import sys
read = sys.stdin.readline

n,m = map(int,read().split())

def binary_search(y=n-1):
    # 1<= y <= n-1
    low, high, mid = 1, y, (1+y)//2
    while low+1 < high:
        mid = (low+high) //2
        print(u*n-(u+d)*mid)

        if u*n-(u+d)*mid < 0:
            high = mid
        else:
            low = mid
    print(low,mid,high)

    print("val: ",u*n-(u+d)*low)

    if u*n-(u+d)*low > 0:
        while u*n-(u+d)*low > 0:
            low += 1
        return u*n-(u+d)*(low-1)
    elif u*n-(u+d)*low > 0:
        while u*n-(u+d)*low < 0:
            low -= 1
        return u*n-(u+d)*(low)
    else:
        return u*n-(u+d)*(low-1)

sol = float('inf')
for i in range(m):
    u,d = map(int,read().split())
    sol = min(sol, binary_search())
print(sol)





