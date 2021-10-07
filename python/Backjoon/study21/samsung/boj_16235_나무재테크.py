import sys
read = sys.stdin.readline
N,M,K = map(int, read().split())
mat = [[5 for i in range(N)] for j in range(N)]
s2d2 = [list(map(int,read().split())) for i in range(N)]
trees = {}
for i in range(M):
    x,y,z = map(int,read().split())
    trees[(x-1,y-1)] = [z]
dd = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
for year in range(K):
    check = {}
    for v in trees:
        dead, Next = 0, []
        for i in range(len(trees[v])):
            old = trees[v][i]
            if mat[v[0]][v[1]] < old:
                dead += old//2
            else:
                mat[v[0]][v[1]] -= old
                Next.append(old+1)
                if (old+1)%5 == 0:
                    if v in check:
                        check[v] += 1
                    else:
                        check[v] = 1
        trees[v] = Next
        mat[v[0]][v[1]] += dead
    for v in check:
        cnt = check[v]
        for i in range(8):
            nx,ny = v[0] + dd[i][0], v[1] + dd[i][1]
            if 0 <= nx < N and 0 <= ny < N:
                if (nx,ny) in trees:
                    trees[(nx,ny)] = [1]*cnt + trees[(nx,ny)]
                else:
                    trees[(nx,ny)] = [1]*cnt
                    
    for i in range(N):
        for j in range(N):
            mat[i][j] += s2d2[i][j]
print(sum([len(trees[v]) for v in trees]))



