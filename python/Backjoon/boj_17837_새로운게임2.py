# a = [1,2,5,2,3]
# a.extend([4,5,6])
# a.reverse()
# print(a)

import sys
read = sys.stdin.readline
N,K = map(int,read().split())
mat = []
for i in range(N):
    mat.append(list(map(int,read().split())))

players,stack = [],{}
for i in range(K):
    r,c,d = map(int,read().split())
    r,c,d = r-1,c-1,d-1
    players.append([r,c,d])
    if (r,c) not in stack:
        stack[(r,c)] = [i+1]
    else:
        stack[(r,c)].append(i+1)
    

def move(r,c,nx,ny,num,color):
    idx = stack[(r,c)].index(num)
    stack[(r,c)],move = stack[(r,c)][:idx], stack[(r,c)][idx:]
    if color == 1:
        move.reverse()

    if (nx,ny) in stack:
        stack[(nx,ny)].extend(move)
        if len(stack[(nx,ny)]) >= 4:
            return 'end'
    else:
        stack[(nx,ny)] = move
    
    for player_num in move:
        players[player_num-1][0],players[player_num-1][1] = nx,ny
    
    return 'continue'
    
for turn in range(1,1001):
    num = 0

    for player in players:
        dx,dy = [0,0,-1,1],[1,-1,0,0]
        r,c,d = player[0],player[1],player[2]
        num += 1

        nx,ny = r+dx[d], c+dy[d]

        if 0 <= nx < N and 0 <= ny < N and mat[nx][ny] == 0:
            ret = move(r,c,nx,ny,num,0)
        elif 0 <= nx < N and 0 <= ny < N and mat[nx][ny] == 1:
            ret = move(r,c,nx,ny,num,1)
        else:
            if d == 0:
                d = 1
            elif d == 1:
                d = 0
            elif d == 2:
                d = 3
            else:
                d = 2
            nx,ny,players[num-1][2] = r + dx[d], c + dy[d], d
            

            if 0 <= nx < N and 0 <= ny < N and mat[nx][ny] == 0:
                ret = move(r,c,nx,ny,num,0)
            elif 0 <= nx < N and 0 <= ny < N and mat[nx][ny] == 1:
                ret = move(r,c,nx,ny,num,1)
            else:
                continue
        
        if ret == 'end':
            print(turn)
            break
    if ret == 'end':
        break
if ret == 'continue':
    print(-1)


