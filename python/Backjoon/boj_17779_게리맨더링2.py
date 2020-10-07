import sys
read = sys.stdin.readline
N = int(read()) # N <= 20
mat = []
for i in range(N):
    mat.append(list(map(int,read().split())))

def div(x,y,d1,d2): # d1,d2 >= 1, 1<= x < x+d1+d2 <= N, 1<= y-d1 < y < y+d2 <= N
    vote_num = [0,0,0,0,0]
    check = {} # 5번구역
    for k in range(d2+1):
        for i in range(d1+1-k):
            if (x+i+k,y-i) not in check:

                check[(x+i+k,y-i)] = 5
            if (x+d2+i,y+d2-i-k) not in check:

                check[(x+d2+i,y+d2-i-k)] = 5

        for i in range(d2+1-k):
            if (x+i+k,y+i) not in check:

                check[(x+i+k,y+i)] = 5
            if (x+d1+i,y-d1+i+k) not in check:

                check[(x+d1+i,y-d1+i+k)] = 5

    for r in range(N):
        for c in range(N):
            # 1번 선거구
            if 0 <= r < x +d1 and 0 <= c <= y and (r,c) not in check:
                vote_num[0] += mat[r][c]
            # 2번 선거구
            if 0 <= r <= x +d2 and y < c <= N and (r,c) not in check:
                vote_num[1] += mat[r][c]
            # 3번 선거구
            if x+d1 <= r <= N and 0<= c < y-d1+d2 and (r,c) not in check:
                vote_num[2] += mat[r][c]
            # 4번 선거구
            if x+d2 < r <= N and y-d1+d2 <= c <= N and (r,c) not in check:
                vote_num[3] += mat[r][c]
    # 5번 선거구 남은 거
    vote_num[4] = sum([mat[key[0]][key[1]] for key in check])
    return max(vote_num)-min(vote_num)

nomi = []
for x in range(1,N+1):
    for y in range(1,N+1):
        for d1 in range(1,N+1):
            for d2 in range(1,N+1):
                if d1 >= 1 and d2 >= 1 and 1<= x < x+d1+d2 <= N and 1<=y-d1 < y < y+d2 <=N:
                    nomi.append((x,y,d1,d2))
sol = []
for x,y,d1,d2 in nomi:
    sol.append(div(x-1,y-1,d1,d2))
print(min(sol))

