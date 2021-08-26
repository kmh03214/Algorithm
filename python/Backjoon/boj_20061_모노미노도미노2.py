import sys
read = sys.stdin.readline

blocks = {1:[(0,0)],2:[(0,0),(0,1)],3:[(0,0),(1,0)]} 


mat = [[0 for i in range(10)] for j in range(10)]

def push(start,dx,dy):
    q = start
    while q:
        Next = []
        for v in q:
            nx,ny = v[0]+dx,v[1]+dy
            if 0<= nx < 10 and 0 <= ny < 10:
                if mat[nx][ny] != 1:
                    Next.append((nx,ny))
                else:
                    for u in q:
                        mat[u[0]][u[1]] = 1
                    return
            else:
                for u in q:
                    mat[u[0]][u[1]] = 1
                return
        q = Next


def first_test(color):
    cnt = 0
    if color == 'blue':
        while True:
            for j in range(9,5,-1):
                fg = 1    
                for i in range(0,4):
                    if mat[i][j] != 1:
                        fg = 0
                        continue
                if fg:
                    for i in range(0,4):
                        mat[i][j] = 0
                    cnt += 1
                    for k in range(j,2,-1):
                        for t in range(0,4):
                            mat[t][k] = mat[t][k-1]
                    break
            if fg:
                continue
            break
    if color == 'green':
        while True:
            for j in range(9,5,-1):
                fg = 1    
                for i in range(0,4):
                    if mat[j][i] != 1:
                        fg = 0
                        continue
                if fg:
                    for i in range(0,4):
                        mat[j][i] = 0
                    cnt += 1
                    for k in range(j,2,-1):
                        for t in range(0,4):
                            mat[k][t] = mat[k-1][t]
                    break
            if fg:
                continue
            break
    return cnt
def second_test(color):
    if color == 'blue':
        for j in range(4,6):
            for i in range(0,4):
                if mat[i][j] == 1:
                    if j == 4:
                        for k in range(8,2,-1): # 두칸밀기
                            for t in range(0,4):
                                mat[t][k+1] = mat[t][k]
                        return
                    if j == 5:
                        for k in range(8,3,-1): # 한칸밀기
                            for t in range(0,4):
                                mat[t][k+1] = mat[k][t] 
                        return
    if color == 'green':
        for j in range(4,6):
            for i in range(0,4):
                if mat[j][i] == 1:
                    if j == 4:
                        for k in range(8,2,-1):
                            for t in range(0,4):
                                mat[k+1][t] = mat[k][t]
                        return
                    if j == 5:
                        for k in range(8,3,-1):
                            for t in range(0,4):
                                mat[k+1][t] = mat[k][t]
                        return

N = int(read())
score = 0
for i in range(N):
    t,x,y = map(int,read().split())
    start = []
    for block in blocks[t]:
        start.append((x+block[0],y+block[1]))
    
    # for m in mat[:4]:
    #     for idx in range(6,10):
    #         m[idx] = 1
    # # mat[3][6]=0

    # for m in mat[6:10]:
    #     for idx in range(0,4):
    #         m[idx] = 1
    # # mat[6][3] = 0


    
    push(start,0,1) ,push(start,1,0) # right push, down push
    score += first_test('blue') + first_test('green')
    second_test('blue')
    second_test('green')

print(score)
print(sum([m.count(1) for m in mat]))


