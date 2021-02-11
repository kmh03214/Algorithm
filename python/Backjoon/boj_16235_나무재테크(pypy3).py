import sys
read = sys.stdin.readline

N,M,K = map(int,read().split())

arr = [] # 겨울에 뿌릴 양분배열
for i in range(N):
    a = list(map(int,read().split()))
    arr.append(a)

class ground():
    def __init__(self):
        self.nutrient = 5
        self.trees = []

mat = []
for i in range(N):
    mat.append([ground() for j in range(N)])

for i in range(M): # 처음에 심을 나무정보 심을 나무위치는 전부 다르므로 정렬은 필요없다.
    x,y,z = map(int,read().split())
    mat[x-1][y-1].trees.append(z)

add_trees = {} # 주변에 번식시킬 나무 좌표
def simulation(x,y):
    trees_old = mat[x][y].trees
    tmp_nutrient = 0
    tmp_trees = []

    for tree_idx in range(len(trees_old)):
        if trees_old[tree_idx] <= mat[x][y].nutrient:
            mat[x][y].nutrient -= trees_old[tree_idx]
            trees_old[tree_idx] += 1
            tmp_trees.append(trees_old[tree_idx])
            if trees_old[tree_idx]%5 == 0: # 가을
                if (x,y) not in add_trees:
                    add_trees[(x,y)] = 1
                else:
                    add_trees[(x,y)] += 1
        else:
            tmp_nutrient += trees_old[tree_idx]//2  # 양분 흡수 못하면, 죽어서 양분됨
    mat[x][y].trees = tmp_trees
    mat[x][y].nutrient += tmp_nutrient + arr[x][y] # 겨울

    return add_trees

def bfs(start,num):
    q = [start]
    check = {start:1}
    dx,dy = [1,1,0,-1,-1,-1,0,1], [0,1,1,1,0,-1,-1,-1]
    while q:
        for v in q:
            r,c = v[0],v[1]
            for i in range(8):
                nx,ny = r+dx[i], c+dy[i]
                if 0 <= nx < N and 0 <= ny < N and (nx,ny) not in check:
                    check[(nx,ny)] = 1
                    mat[nx][ny].trees = [1]*num + mat[nx][ny].trees # 1살짜리 tree append(가장 나이어림)
        break

for k in range(K):
    for i in range(N):
        for j in range(N):
            simulation(i,j)

    for add_tree in add_trees:
        bfs(add_tree, add_trees[add_tree])
    add_trees = {}

sol = 0
for i in range(N):
    for j in range(N):
        sol += len(mat[i][j].trees)

print(sol)


    