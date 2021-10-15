# 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
# 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
    # 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
# 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
# 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.

import sys
read = sys.stdin.readline
N,K = map(int,read().split())
belt = [[0,i] for i in map(int,read().split())]

def check(robot):
    if robot[-1][0]:
        robot[-1] = [0,robot[-1][1]]
time,fg,cnt = 0,0,0

while cnt < K:
    belt = [belt[-1]] + belt[:-1]
    robot, belt = belt[:N], belt[N:]
    check(robot)

    for i in range(len(robot)-2,-1,-1):
        if robot[i][0] == 1 and robot[i+1][1] > 0 and robot[i+1][0] == 0:
            robot[i][0] ,robot[i+1] = 0, [1,robot[i+1][1]-1]
            if robot[i+1][1] == 0:
                cnt += 1
    check(robot)

    if not robot[0][0] and robot[0][1] > 0:
        robot[0] = [1,robot[0][1]-1]
        if robot[0][1] == 0:
            cnt += 1
    belt = robot+belt
    

    time += 1
print(time)
