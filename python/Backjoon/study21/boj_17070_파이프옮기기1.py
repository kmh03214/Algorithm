import sys
read = sys.stdin.readline
N = int(read())
mat = []
for i in range(N):
    mat.append(list(map(int,read().split())))

check = {}
next_xy = [(0,1), (1,1), (1,0)]
next_state = [(0,1), (0,1,2), (1,2)]
possible = [[(0,0)],[(0,0), (0,-1), (-1,0)], [(0,0)]]

def dfs(s,r,c):
    if sum([mat[r+s[0]][c+s[1]] for s in possible[s]] ) != 0:
        return 0
    if r == N-1 and c == N-1:
        return 1

    if (s,r,c) in check:
        return check[(s,r,c)]
    else:
        check[(s,r,c)] = sum(
            [dfs(ns, r + next_xy[ns][0], c + next_xy[ns][1]) for ns in next_state[s] 
            if r + next_xy[ns][0]< N and c + next_xy[ns][1] < N]
            )   
    return check[(s,r,c)]
dfs(0,0,1)
print(check[(0,0,1)])