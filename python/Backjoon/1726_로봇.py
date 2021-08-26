import sys
read = sys.stdin.readline
N,M = map(int,read().split())
mat = []
for i in range(N):
    mat.append(list(map(int,read().split())))

sx,sy,sd = map(int, read().split())
ex,ey,ed = map(int, read().split())
def transform_dir(d):
    if d == 1:
        d = 0
    elif d == 2:
        d = 2
    elif d == 3:
        d = 1
    else:
        d = 3
    return d
sx,sy,ex,ey = sx-1, sy-1, ex-1, ey-1

sd,ed = transform_dir(sd), transform_dir(ed)

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(start):
    



# dp_table = {}
# def DP(start, d , check, level):
#     x,y = start
#     if not (0<= x < N and 0 <= y < M and mat[x][y] == 0):
#         return 100000
#     check[start] = 1
#     print(start,d)
#     if start == (ex,ey) and d == ed:
#         return level

#     else:
#         if (x,y,d) not in dp_table:
#             # 한칸 이동 / 두칸이동 / 세칸이동 / 방향전환
#             tmp = []
#             for lv in range(4):
#                 add = 0
#                 if lv == 2:
#                     add = 2
#                 elif lv == 1 or lv == 3:
#                     add = 1



#                 for i in range(1,4):
#                     nx,ny = x+i*dx[d], y+i*dy[d]
#                     if 0<= nx < N and 0 <= ny < M and mat[nx][ny] == 0 and (nx,ny) not in check:
#                         tmp.append(DP((nx, ny), (d+lv)%4 ,check, level+add+1))
#                     else:
#                         break
            

#         else:
#             return dp_table[(x,y,d)]
#     return 100000

# DP((sx,sy),sd,{},0)
# print(dp_table)