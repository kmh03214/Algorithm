import sys
read = sys.stdin.readline
N = int(read())
mat = []
for i in range(N):
    mat.append(list(map(int,read().split())))

def rotation_90(arr):
    return [list(reversed(i)) for i in zip(*arr)]

left = [[0,0,2,0,0],
[0,10,7,1,0],
[5,0,0,0,0],
[0,10,7,1,0],
[0,0,2,0,0]]

up = rotation_90(left)
right = rotation_90(up)
down = rotation_90(right)

def move_left(r,c): # 현재위치입력
    
    ret_sand = 0 # 밖으로 나간 모래
    s = 0 # 나눠준 모래
    nr,nc = r,c-1
    cur_sand = mat[nr][nc]
    mat[nr][nc] = 0 

    for i in range(5):
        for j in range(5):
            
            if 0 <= nr - 2 + i < N and 0 <= nc - 2 + j < N:
                alpha = int(cur_sand * (left[i][j]/100))
                mat[ nr-2+i ][ nc-2+j ] += alpha
                s += alpha
                
            else: # 모레가 밖으로 나가는 경우
                ret_sand += int(cur_sand * (left[i][j]/100))
    
    
    if 0 <= nr < N and 0 <= nc-1 < N:
        mat[nr][nc-1] += cur_sand - s - ret_sand # 남은 모래양 alpha에 추가
    else:
        ret_sand = cur_sand - s

    return nr,nc,ret_sand

def move_right(r,c): # 현재위치입력
    
    ret_sand = 0
    s = 0
    nr,nc = r,c+1
    cur_sand = mat[nr][nc]
    mat[nr][nc] = 0 

    for i in range(5):
        for j in range(5):
            
            if 0 <= nr - 2 + i < N and 0 <= nc - 2 + j < N:
                alpha = int(cur_sand * (right[i][j]/100))
                mat[ nr-2+i ][ nc-2+j ] += alpha
                s += alpha
                
            else: # 모레가 밖으로 나가는 경우
                ret_sand += int(cur_sand * (right[i][j]/100))
    
    if 0 <= nr < N and 0 <= nc+1 < N:
        mat[nr][nc+1] += cur_sand - s - ret_sand # 남은 모래양 alpha에 추가
    else:
        ret_sand = cur_sand - s

    return nr,nc,ret_sand

def move_down(r,c): # 현재위치입력
    
    ret_sand = 0
    s = 0
    nr,nc = r+1,c
    cur_sand = mat[nr][nc]
    mat[nr][nc] = 0 

    for i in range(5):
        for j in range(5):
            
            if 0 <= nr - 2 + i < N and 0 <= nc - 2 + j < N:
                alpha = int(cur_sand * (down[i][j]/100))
                mat[ nr-2+i ][ nc-2+j ] += alpha
                s += alpha
                
            else: # 모레가 밖으로 나가는 경우
                ret_sand += int(cur_sand * (down[i][j]/100))
    
    if 0 <= nr+1 < N and 0 <= nc < N:
        mat[nr+1][nc] += cur_sand - s - ret_sand # 남은 모래양 alpha에 추가
    else:
        ret_sand = cur_sand - s

    return nr,nc,ret_sand

def move_up(r,c): # 현재위치입력
    
    ret_sand = 0
    s = 0
    nr,nc = r-1,c
    cur_sand = mat[nr][nc]
    mat[nr][nc] = 0 

    for i in range(5):
        for j in range(5):
            
            if 0 <= nr - 2 + i < N and 0 <= nc - 2 + j < N:
                alpha = int(cur_sand * (up[i][j]/100))
                mat[ nr-2+i ][ nc-2+j ] += alpha
                s += alpha
                
            else: # 모레가 밖으로 나가는 경우
                ret_sand += int(cur_sand * (up[i][j]/100))
    if 0 <= nr-1 < N and 0 <= nc < N:
        mat[nr-1][nc] += cur_sand - s - ret_sand # 남은 모래양 alpha에 추가
    else:
        ret_sand = cur_sand - s
    
    return nr,nc,ret_sand

nr,nc = N//2, N//2
solution = 0
for level in range((N//2)):
    nr,nc,sol = move_left(nr,nc)
    solution += sol

    for i in range((level+1)*2 - 1):
        nr,nc, sol = move_down(nr,nc)
        solution += sol
        
    for i in range((level+1)*2):
        nr,nc, sol = move_right(nr,nc)
        solution += sol

    for i in range((level+1)*2):
        nr,nc, sol = move_up(nr,nc)
        solution += sol
        
    for i in range((level+1)*2):
        nr,nc, sol = move_left(nr,nc)
        solution += sol

print(solution)
        
        
        
