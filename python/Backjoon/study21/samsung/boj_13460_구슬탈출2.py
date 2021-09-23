import sys
read = sys.stdin.readline
N,M = map(int,read().split())
mat = []
for i in range(N):
    a = ' '.join(read()).split()
    for j in range(M):
        if a[j] == 'B':
            blue = (i,j)
        if a[j] == 'R':
            red = (i,j)
    mat.append(a)

def product(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in product(arr,r-1):
                if next[0] == arr[i]:
                    continue
                yield [arr[i]] + next

# 4*3^9 = 78732
# N, M < 10 -> 최대 20칸이동 * 10
# 78732 * 200 = 1574만
dd = [(0,1),(1,0),(0,-1),(-1,0)] # 오 아래 왼 위
def bfs(start,d):
    q = [start]
    check = {start:1}
    move = 0
    while q:
        Next = []
        for v in q:
            nx,ny = v[0] + dd[d][0], v[1] + dd[d][1]
            if 0 <= nx < N and 0 <= ny < M and (nx,ny) not in check and mat[nx][ny] != '#':
                if mat[nx][ny] == 'O':
                    return (nx,ny), 1, move
                check[(nx,ny)] = 1
                Next.append((nx,ny))
        q = Next
        move += 1
    return v, 0, move


sol = []

for dirs in product([0,1,2,3],10):
    cnt = 0
    for d in dirs:
        cnt += 1
        red, succ_r,red_move = bfs(red,d)
        blue, succ_b, blue_move = bfs(blue,d)
        if succ_r and not succ_b: # 성공
            # cnt == 1 -> 그냥 종료
            sol.append(cnt)
        elif succ_b:
            break # 실패
        else:
            if red == blue:
                # 겹쳤다는건, (x1,y1), (x2,y2)에서 x1 == x2 or y1 == y2
                if red_move < blue_move:
                    blue = blue[0] - dd[d][0] , blue[1] - dd[d][1]
                else:
                    red = red[0] - dd[d][0] , red[1] - dd[d][1]

print(min(sol))
