import sys
read = sys.stdin.readline
Node = int(read())
edge = int(read())
G = {}
for i in range(edge):
    v1,v2 = map(int,read().split())
    if v1 not in G:
        G[v1] = [v2]
        if v2 not in G:
            G[v2] = [v1]
        else:
            G[v2].append(v1)
    else:
        G[v1].append(v2)
        if v2 not in G:
            G[v2] = [v1]
        else:
            G[v2].append(v1)

def bfs(start, G):
    check = {start:1}
    q = [start]
    while q:
        Next = []
        for v in q:
            for u in G[v]:
                if u not in check:
                    Next.append(u)
                    check[u] = 1
        q = Next
    print(len(check)-1)

bfs(1,G)