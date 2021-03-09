import sys
read = sys.stdin.readline
N, K = map(int,read().split())

belt = [[i,0] for i in map(int,read().split())] # (내구도,로봇여부)
cnt,sol =0, 0
def move_belt():
    global belt
    belt = [belt[-1]] + belt[:-1] # 회전
    if belt[N-1][1] == 'R':
        belt[N-1][1] = 0

def move_robot():
    global cnt
    for i in range(N-2,-1,-1):
        if belt[i][1] == 'R' and belt[i+1][1] != 'R' and belt[i+1][0] != 0:
            belt[i+1][0], belt[i][1], belt[i+1][1] = belt[i+1][0]-1,0,'R'
            if belt[i+1][0] == 0:
                cnt += 1
    if belt[N-1][1] == 'R':
        belt[N-1][1] = 0
    if belt[0][0] > 0:
        belt[0][0], belt[0][1] = belt[0][0]-1, 'R'
        if belt[0][0] == 0:
            cnt += 1


while cnt < K:
    sol += 1
    move_belt()
    move_robot()
print(sol)