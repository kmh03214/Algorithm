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
            DFS(a+[i])
DFS([])