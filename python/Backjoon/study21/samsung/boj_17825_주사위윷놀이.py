from itertools import product
order = list(map(int,input().split()))
board =[
    [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40],
    [13,16,19,25,30,35,40],
    [22,24,25,30,35,40],
    [28,27,26,25,30,35,40]
    ]
# 10 : 0 -> 1
# 20 : 0 -> 2
# 30 : 0 -> 3 (0번 30일 때 만)
# 4**10 = 100만
sol = 0
for prod in product([1,2,3,4], repeat = 10):
    player, s = {1:[0,-1], 2:[0,-1], 3:[0,-1], 4:[0,-1]}, 0
    for o,p in zip(order,prod):
        if player[p][1] + o >= len(board[player[p][0]]):
            player[p][1] = len(board[player[p][0]])
            continue
        player[p][1] += o
        x,y = player[p][0],player[p][1]
        
        if board[x][y] == 10:
            player[p] = [1,-1]
        if board[x][y] == 20:
            player[p] = [2,-1]
        if board[x][y] == 30 and player[p][0] == 0:
            player[p] = [3,-1]
        if board[x][y] == 25:
            player[p] = [3,3]
        if board[x][y] == 30 and player[p][0] != 3:
            player[p] = [3,4]
        if board[x][y] == 35:
            player[p] = [3,5]

        if board[x][y] == 40:
            player[p] = [3,6]
            
        if player[p] in [player[i] for i in player if i!=p]:
            break
        s += board[x][y]
    sol = max(sol,s)
print(sol)
