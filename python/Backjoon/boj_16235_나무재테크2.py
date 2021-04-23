import sys
read = sys.stdin.readline

N,M,K = map(int,read().split()) # 땅,나무개수, 지난 연도
mat = [[5 for i in range(N)] for j in range(N)]
A = [] # 로봇이 겨울에 양분을 주는 양
trees = [[[] for i in range(N)] for j in range(N)]
check = {}

for i in range(N):
    A.append(list(map(int,read().split())))
for i in range(M): # 나무
    r,c,year = map(int,read().split())
    trees[r-1][c-1].append(year)
    check[(r-1,c-1)] = 1

dx,dy = [-1,-1,0,1,1,1,0,-1],[0,-1,-1,-1,0,1,1,1]
for time in range(K):
    dead = {}
    create = {}
    del_p = []
    for tree_pos in check: # 봄
        r,c = tree_pos
        Next = []
        tree_heap = trees[r][c]
        nut = 0
        for i in range(len(tree_heap)):
            old = tree_heap[i]
            if old <= mat[r][c]:
                mat[r][c] -= old
                old +=1
                Next.append(old)
                if old % 5 == 0:
                    if (r,c) in create:
                        create[(r,c)] += 1
                    else:
                        create[(r,c)]= 1
            else:
                nut += old//2
        mat[r][c] += nut
        if Next:
            trees[r][c] = Next
        else:
            trees[r][c] = []
            del_p.append((r,c))
    for de in del_p:
        del check[de]
    for cr_pos in create: # 가을
        r,c = cr_pos
        num = create[(r,c)]
        for i in range(8):
            nr,nc = r+dx[i],c+dy[i]
            if 0<= nr < N and 0<= nc < N:
                trees[nr][nc] = [1]*num + trees[nr][nc]
                check[(nr,nc)] = 1
    for i in range(N):
        for j in range(N):
            mat[i][j] += A[i][j]
sol = 0
for tree in trees:
    for t in tree:
        sol += len(t)
print(sol)