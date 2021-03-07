import sys
read = sys.stdin.readline
N,M,fuel = map(int,read().split())
mat = []
for i in range(N):
    mat.append(list(map(int,read().split())))
taxi_p = list(map(int,read().split()))

taxi = (taxi_p[0]-1,taxi_p[1]-1)

match = {}
for i in range(M):
    x,y,x_,y_ = map(int,read().split())
    match[(x-1,y-1)] = (x_-1,y_-1)
    mat[x-1][y-1] = (-1,-1) # 승객


dx, dy = [1,-1,0,0], [0,0,1,-1]
def find_client(start):
    q, dist = [start], 0
    check = {start:1}
    while q:
        Next = []
        for v in q:
            r,c = v[0],v[1]
            if mat[r][c] == (-1,-1):
                ret = []
                for tmp in q:
                    if mat[tmp[0]][tmp[1]] == (-1,-1):
                        ret.append(tmp)
                ret.sort(key = lambda x : (x[0],x[1]))
                r,c = ret[0]
                mat[r][c] = 0
                return (r,c),dist

            for i in range(4):
                nx, ny = r + dx[i], c + dy[i]
                if 0<= nx < N and 0<= ny < N and mat[nx][ny] != 1 and (nx,ny) not in check:
                    check[(nx,ny)] = 1
                    Next.append((nx,ny))
        q = Next
        dist += 1
    return (0,0),-1

def find_goal(start,end):
    q, dist = [start], 0
    check = {start:1}
    while q:
        Next = []
        for v in q:
            r,c = v[0],v[1]
            if v == end:
                return (r,c),dist

            for i in range(4):
                nx, ny = r + dx[i], c + dy[i]
                if 0<= nx < N and 0<= ny < N and mat[nx][ny] != 1 and (nx,ny) not in check:
                    check[(nx,ny)] = 1
                    Next.append((nx,ny))
        q = Next
        dist += 1
    return (0,0),-1

def solution(fuel):
    x,y = taxi
    for i in range(M):
        (x, y), dist_ = find_client((x,y))
        if dist_ == -1:
            return -1
        fuel -= dist_
        if fuel < 0:
            return -1

        (x, y), dist_ = find_goal((x,y),match[(x,y)])
        if dist_ == -1:
            return -1

        fuel -= dist_
        if fuel < 0:
            return -1
        else:
            fuel += (2*dist_)
    return fuel
print(solution(fuel))
