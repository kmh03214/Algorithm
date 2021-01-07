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

def move(mat, pos, d): # red or blue , direction
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

# 중복허용 순열인데 앞에 나온건 다시 안쓴다.
def main():
    for depth in range(1,11):
        product = itertools.product([0,1,2,3],repeat = depth)
        sol = []

        for prod in product:
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
                    ret_r = move(mat,red,direction)
                    ret_b = move(mat,blue,direction)
                    if ret_r == 1 and ret_b == 0:
                        return depth
                else: # B, R
                    ret_b = move(mat,blue,direction)
                    ret_r = move(mat,red,direction)
                    if ret_r == 1 and ret_b == 0:
                        return depth
                if ret_b == 1:
                    return # 실패 더 이상 탐색할 필요 없음.

sol = main()
if sol:
    print(sol)
else:
    print(-1)