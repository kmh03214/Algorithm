import sys
read = sys.stdin.readline
mat = []
fish_position = [0]*17
direction = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]

for i in range(4):
    a = list(map(int, read().split()))
    b = []
    for j in range(4):
        fish_position[a[2*j]] = (i,j)
        b.append((a[2*j],a[2*j+1]))
    mat.append(b)

shark = (0,mat[0][0][1])
shark_pos = (0,0)
shark_size = mat[0][0][0]
fish_position[mat[0][0][0]] = 0
mat[0][0] = shark

sol = []
def shark_move():
    q = []
    r,c = shark_pos[0],shark_pos[1]
    for i in range(4):
        dx,dy = direction[shark[1]-1]
        r,c = r+dx, c+dy
        if 0 <= r < 4 and 0 <= c < 4:
            q.append((r,c))
    return q

def fish_move(ma,fish_pos,shark,shark_size,shark_pos):
    m,f_pos = [], fish_pos.copy()
    for m_ in ma:
        m.append(m_.copy())
    for pos in f_pos:
        if pos == 0:
            continue
        r,c = pos[0],pos[1]
        f_num, d = m[r][c] # 물고기의 현재 번호 및 방향
        for i in range(8):
            dx,dy = direction[(d+i)%8-1]
            nr,nc = r+dx, c+dy
            if 0 <= nr < 4 and 0 <= nc < 4 and m[nr][nc][0] != shark[0]: # 이동할 수 있는경우
                if f_pos[m[nr][nc][0]]: # 물고기가 있다면
                    f_pos[f_num], f_pos[m[nr][nc][0]] = f_pos[m[nr][nc][0]], f_pos[f_num]
                    m[r][c], m[nr][nc] = m[nr][nc], m[r][c]
                else:
                    m[r][c], m[nr][nc] = m[nr][nc], m[r][c]
                break
    
    q = shark_move()
    print(q)
    if q:
        for s_pos in q:
            m[shark_pos[0]][shark_pos[1]] = 
            sr,sc = shark_pos = s_pos
            fish_num, fish_d = m[sr][sc]
            shark = (0,m[sr][sc][1])
            m[sr][sc] = shark
            shark_size += m[sr][sc][0]
            print(shark_pos,shark,shark_size)

            fish_move(m,f_pos,shark,shark_size,shark_pos)

            m[sr][sc] = fish_num, fish_d
            shark_size -= fish_num
    else:
        sol.append(shark_size)
        return




    #fish_move(m,f_pos,shark)
    

fish_move(mat,fish_position,shark,shark_size,shark_pos)
shark_move()
            



        


    
    

