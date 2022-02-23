import sys
read = sys.stdin.readline

N = int(read())

people = list(map(int,read().split()))
G = {}
for i in range(N):
    a = list(map(int,read().split()))
    G[i+1] = a[1:]

# N < 10 -> 2구역으로 나누기 10C1 + 10C2 + ...10C10 = 2^10-1
# 연결성 확인. g1 / g2 
# 최소값 찾기

# arr = [1,2,3,4,5,6]
# masks = [1 << i for i in range(len([arr))] => [1,2,4,8,16,32]
def powerset(s):
    masks = [1 << i for i in range(len(s))]
    for i in range( 1 << len(s)): # 1 ~ 63
        yield [ss for ss,mask in zip(s,masks) if i & mask] # 1 & masks / 2 & masks .... 31 & masks

def bfs(s,complement_set):
    check = {i:1 for i in complement_set}
    check[s] = 1
    q = [s]
    while q:
        Next = []
        for v in q:
            for u in G[v]:
                if u not in check:
                    check[u] = 1
                    Next.append(u)
        q = Next
    if len(check) != N:
        return 0
    return 1

arr = [i+1 for i in range(N)]
sol = []
for p in powerset(arr):
    # if len(p) > (N//2) +1:
    #     break
    if len(p) == 0 or len(p) == N:
        continue
    complement = list(set(arr).difference(p))
    if bfs(complement[0],p) and bfs(p[0], complement):
        sol.append(abs(sum(people[i-1] for i in complement) - sum([people[i-1] for i in p])))

if sol:
    print(min(sol))
else:
    print(-1)