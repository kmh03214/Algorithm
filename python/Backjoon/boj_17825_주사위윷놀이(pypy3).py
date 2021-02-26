import sys
read = sys.stdin.readline
dice = list(map(int,read().split()))

from itertools import product
board = {
    0:[2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,'end'],
    1:[28,27,26,25,30,35,40,'end'],
    2:[22,24,25,30,35,40,'end'],
    3:[13,16,19,25,30,35,40,'end']
    }
def go(num,move):
    pos = players[num]
    if pos == 'end':
        return 'end1'
    L = len(board[pos[0]])
    if L-1 <= pos[1]+move: # 'end' game
        players[num] = 'end'
        return 'end1'
    elif (pos[0],pos[1]+move) in players:
        return 'end2'
    else:
        score = board[pos[0]][pos[1]+move]
        if score == 25:
            if (1,3) in players or (2,2) in players or (3,3) in players:
                return 'end2'
        if score == 30 and pos[0] != 0:
            if (1,4) in players or (2,3) in players or (3,4) in players:
                return 'end2'
        if score == 35:
            if (1,5) in players or (2,4) in players or (3,5) in players:
                return 'end2'
        if score == 40:
            if (0,19) in players or (1,6) in players or (2,5) in players or (3,6) in players:
                return 'end2'
        if score == 'end':
            players[num] = 'end'
            return 'end2'
                
        if score == 10 and pos[0] == 0:
            if (3,-1) in players:
                return 'end2'
            players[num] = (3,-1)
        elif score == 20 and pos[0] == 0:
            if (2,-1) in players:
                return 'end2'
            players[num] = (2,-1)
        elif score == 30 and pos[0] == 0:
            if (1,-1) in players:
                return 'end2'
            players[num] = (1,-1)
        else:
            players[num] = (pos[0], pos[1]+move)
    return score
sol = []
for prod in product([0,1,2,3],repeat=10):
    score,fg = 0,0
    players = [(0,-1) for i in range(4)] # 0번말 위치 1번말 위치 2번말 위치 3번말 위치
    for player_num, move in zip(prod,dice):
        ret = go(player_num,move)
        if ret == 'end':
            continue
        elif ret == 'end1':
            continue
        elif ret == 'end2':
            fg = 1
            break
        else:
            score += ret
    if fg == 1:
        continue
    sol.append(score)
    
print(max(sol))

