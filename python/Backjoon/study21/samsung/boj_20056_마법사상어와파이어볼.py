# 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
#   이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.

# 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
#   같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
#   파이어볼은 4개의 파이어볼로 나누어진다.
#   나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
#       질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
#       속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
#       합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
#   질량이 0인 파이어볼은 소멸되어 없어진다.

import sys
read = sys.stdin.readline
N,M,K = map(int,read().split())
fire_balls = [list(map(int,read().split())) for i in range(M)]

dd = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)] # 0,2,4,6

for i in range(K):

    Next, N_fire_balls = {}, []
    
    for ball in fire_balls:
        r,c,m,s,d = ball
        nx,ny = (r+s*dd[d][0])%N , (c+s*dd[d][1])%N
        if (nx,ny) not in Next:
            Next[(nx,ny)] = [m,s,1,d]
        else:
            Next[(nx,ny)][0] += m
            Next[(nx,ny)][1] += s
            Next[(nx,ny)][2] += 1
            if Next[(nx,ny)][3] != 'N' and Next[(nx,ny)][3]%2 != d%2:
                Next[(nx,ny)][3] = 'N'
    for n in Next:
        m,s,cnt,fg = Next[n]
        if cnt == 1:
            N_fire_balls.append([n[0],n[1],m,s,fg])
            continue
        m //= 5
        if m == 0:
            continue
        s //= cnt
        if fg == 'N':
            for d in [1,3,5,7]:
                N_fire_balls.append([n[0],n[1],m,s,d])
        else:
            for d in [0,2,4,6]:
                N_fire_balls.append([n[0],n[1],m,s,d])
    fire_balls = N_fire_balls
sol = 0
for b in fire_balls:
    sol += b[2]
print(sol)