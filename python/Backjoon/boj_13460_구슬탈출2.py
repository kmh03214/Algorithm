import sys
import itertools

read = sys.stdin.readline
N, M = map(int,read().split())

m = []
for i in range(N):
    a = ' '.join(read()).split()
    for j in range(M):
        if a[j] == 'R':
            red_ = (i,j)
        elif a[j] == 'B':
            blue_ = (i,j)
    m.append(a)

def priority(d):
    if d == 0: # 우
        if red[1] < blue[1]:
            return 'B'
        else:
            return 'R'
    elif d == 1: # 좌
        if red[1] < blue[1]:
            return 'R'
        else:
            return 'B'
    elif d == 2: # 하
        if red[0] < blue[0]:
            return 'B'
        else:
            return 'R'
    else: # 상
        if red[0] < blue[0]:
            return 'R'
        else:
            return 'B'

def move(pos, d): # red or blue , direction
    color = mat[pos[0]][pos[1]]
    mat[pos[0]][pos[1]] = '.' # 이동할것이기 때문에 .으로 비워줌
    q, dx, dy = [pos], [0,0,1,-1], [1,-1,0,0]
    global red, blue
    while q:
        Next = []
        for v in q:
            r,c = v
            nr, nc = r + dx[d], c + dy[d]
            if mat[nr][nc] == '.':
                Next.append((nr,nc))
            elif mat[nr][nc] == 'O':
                return 1 # 성공
        q = Next
    mat[r][c] = color # 이동 후 색 설정.
    if color == 'R':
        red = (r,c)
    else:
        blue = (r,c)
    return 0
sol = []

direction = [0,1,2,3]
pool = []
def dfs(arr,before,depth):
    if depth == 10:
        yield pool
        return

    for i in arr:
        if i != before:
            pool.append(i)
            for next in dfs(arr,i,depth+1):
                yield next
            pool.pop()
for prod in dfs(direction,10,0):
    cnt,before_dir = 0,-1
    mat = []
    for ma in m:
        mat.append(ma.copy())
    
    global red, blue
    red, blue = red_, blue_

    for direction in prod:
        if direction == before_dir: # 현재 방향이 이전에 갔던 방향하고 동일하면 탐색 중지
            break
        before_dir = direction
        who = priority(direction)
        cnt += 1
        if who == 'R': # R, B
            ret_r = move(red,direction)
            ret_b = move(blue,direction)
            if ret_r == 1 and ret_b == 0:
                sol.append(cnt)
                break
        else: # B, R
            ret_b = move(blue,direction)
            ret_r = move(red,direction)
            if ret_r == 1 and ret_b == 0:
                sol.append(cnt)
                break
        if ret_b == 1:
            break # 실패 더 이상 탐색할 필요 없음.
if sol:
    print(min(sol))
else:
    print(-1)


