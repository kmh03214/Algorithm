import sys
read = sys.stdin.readline

N,M = map(int,read().split())

Edge = []
for i in range(M):
    Edge.append(list(map(int,read().split())))

Edge.sort(key = lambda x: x[2], reverse = True) # 2번 키에대해 큰 순 정렬

parents = [i for i in range(N+1)]
rank = [0 for i in range(N+1)]
def find(v):
    if v != parents[v]:
        parents[v] = find(parents[v])
    return parents[v]

s = 10000000000
def union(a,b,w):
    global s
    root1 = find(a)
    root2 = find(b)
    if root1 != root2:
        s = min(s,w)
        if rank[root1] < rank[root2]:
            parents[root1] = root2
        else:
            parents[root2] = root1

            if rank[root1] == rank[root2]:
                rank[root1] += 1
    if parents[start] == parents[end]:
        return 'end'
start,end = map(int,read().split())

for e in Edge:
    if union(e[0],e[1],e[2]) == 'end':
        break

print(s)
