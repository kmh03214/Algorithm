n, r = map(int,input().split())
arr = [i for i in range(1,n+1)]
check = {}
def DFS(a):
    if len(a) == r:
        for k in a:
            print(k, end=' ')
        print()
        return
    else:
        for i in arr:
            if i not in check:
                check[i] = 1
                DFS(a+[i])
                del check[i]
DFS([])