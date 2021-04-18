import sys
read = sys.stdin.readline
N, M = map(int,read().split())
weights = {}
mat = [[] for i in range(N)]
for i in range(M):
    A,B,C = map(int,read().split())
    if (A-1,B-1) in weights:
        C = max(C,weights[(A-1,B-1)])
    weights[(A-1,B-1)] , weights[(B-1,A-1)] = C , C
    mat[A-1].append(B-1)
    mat[B-1].append(A-1)
    
start, end = map(int,read().split())

sol = 0
def bfs(start,end,w):
    global sol
    q = [start]
    check = {start:1}
    while q:
        Next = []
        for v in q:
            if v == end:
                sol = w
                return 1
            for u in mat[v]:
                if u not in check and weights[(v,u)] >= w:
                    Next.append(u)
                    check[u] = 1
        q = Next
    return 0

# def dfs(start,end,check,tmp):
#     global sol
#     if start == end:
#         sol = max(sol,tmp)
#         return 1

#     for i in range(N):
#         for j in mat[i]:
#             w = weights[(i,j)]
#             if w != 0 and i not in check and tmp > sol:
#                 check[i] = 1
#                 dfs(i,end,check, min(tmp,w) )
#                 del check[i]

lo, hi = 0,1000000000
while lo <= hi:
    mid = (lo + hi) // 2
    if bfs(start-1,end-1,mid):
        lo = mid+1
    else:
        hi = mid-1
print(sol)

        
    

    