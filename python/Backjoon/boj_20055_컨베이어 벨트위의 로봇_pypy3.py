import sys
read = sys.stdin.readline
N, K = map(int,read().split())

global belt, robot
belt = list(map(int,read().split()))
robot = [0 for i in range(N)]

def robot_bye():
    if robot[-1] == -1:
        robot[-1] = 0

def move_belt():
    global belt,robot
    belt = [belt[-1]] + belt[:-1]
    robot = [0] + robot[:-1]
    robot_bye()

def move_robot():
    global belt,robot
    next_robot = [0 for i in range(N)]
    for i in range(N-1,-1,-1):
        if robot[i] == -1 and belt[i+1] > 0:
            if next_robot[i+1] == -1:
                next_robot[i] = -1
                robot[i] = 0
                continue
            next_robot[i+1] = -1
            robot[i+1] = -1
            robot[i] = 0
        elif robot[i] == -1 and belt[i+1] <= 0:
            next_robot[i] = -1
            robot[i] = 0

    for i in range(N):
        belt[i] += robot[i]

    robot = next_robot
    robot_bye()

def robot_hi():
    if belt[0] > 0:
        robot[0] = -1
        belt[0] -= 1
step = 0
while True:
    step += 1
    move_belt()
    move_robot()
    robot_hi()
    if belt.count(0) >= K:
        print(step)
        break