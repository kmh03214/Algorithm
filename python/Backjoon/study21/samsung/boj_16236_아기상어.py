# 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다. 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다. 따라서, 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.

# 아기 상어가 어디로 이동할지 결정하는 방법은 아래와 같다.

# 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
# 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
# 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
# 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
# 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
# 아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다고 가정한다. 즉, 아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동했다면, 이동과 동시에 물고기를 먹는다. 물고기를 먹으면, 그 칸은 빈 칸이 된다.

# 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다. 예를 들어, 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다.

# 공간의 상태가 주어졌을 때, 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하는 프로그램을 작성하시오.

import sys
read = sys.stdin.readline
N = int(read())
mat = []
for i in range(N):
    a = list(map(int,read().split()))
    for j in range(N):
        if a[j] == 9:
            bs, size_eat,a[j] = (i,j), [2,0], 0
    mat.append(a)
dd = [(0,1),(1,0),(0,-1),(-1,0)]
def bfs(s):
    q, check, fg,eat, cnt = [s], {s:1}, 0,[], 0
    while q:
        Next = []
        for v in q:
            for i in range(4):
                nx,ny = v[0]+dd[i][0], v[1]+dd[i][1]
                if 0<= nx < N and 0 <= ny < N and (nx,ny) not in check and mat[nx][ny] <= size_eat[0]:
                    if 0 < mat[nx][ny] < size_eat[0]:
                        eat.append((nx,ny))
                        fg = 1
                    Next.append((nx,ny))
                    check[(nx,ny)] = 1
        q = Next
        cnt += 1
        if fg:
            e = sorted(eat)[0]
            mat[e[0]][e[1]] = 0
            size_eat[1] += 1
            if size_eat[0] == size_eat[1]:
                size_eat[0],size_eat[1] = size_eat[0]+1, 0
            return e, cnt
    return s, 0
dist,sol = 1,0
while dist:
    bs, dist = bfs(bs)
    sol += dist
print(sol)