import sys
from itertools import permutations

read = sys.stdin.readline

def game(ar,data,h_num):
    outcount, score = 0,0
    b1,b2,b3 = 0,0,0

    while outcount < 3:
        action = ar[data[h_num]]
        h_num = (h_num + 1)%9
        if action == 0:
            outcount += 1
        elif action == 1:
            score += b3
            b1,b2,b3 = 1,b1,b2
        elif action == 2:
            score += (b2+b3)
            b1,b2,b3 = 0,1,b1
        elif action == 3:
            score += (b1+b2+b3)
            b1,b2,b3 = 0,0,1
        else:
            score += (b1+b2+b3)+1
            b1,b2,b3 = 0,0,0

    return score, h_num

N = int(read())
arr = []
for i in range(N):
    arr.append(list(map(int,read().split())))

sol = 0

for per in permutations([1,2,3,4,5,6,7,8],8):
    s = 0
    per = [*per[:3],0,*per[3:]]
    
    n_hitter = 0
    for ar in arr:
        score, n_hitter = game(ar, per, n_hitter)
        s += score
    sol = max(s,sol)
print(sol)
