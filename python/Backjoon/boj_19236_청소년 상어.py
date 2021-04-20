import sys
read = sys.stdin.readline
dirs = {
    1:(-1,0),2:(-1,-1),3:(0,-1),4:(1,-1),
    5:(1,0),6:(1,1),7:(0,1),0:(-1,1)
}
fishes = {}
def fish_move(mat_c):
    # 번호 작은순
    for num in range(1,17): # 1부터 16번까지 없으면 다음번호
        if num not in fishes:
            continue
        r,c,d = fishes[num]
        for i in range(8):
            nr,nc = r + dirs[(d+i)%8][0], c + dirs[(d+i)%8][1]
            if 0<= nr <4 and 0 <= nc < 4 and mat_c[nr][nc][0] != -1: # 격자내부랑 상어가 아니면
                num1,nd = mat_c[nr][nc][0], mat_c[nr][nc][1] # 바꿀 물고기 번호
                mat_c[nr][nc], mat_c[r][c] = mat_c[r][c], mat_c[nr][nc] # 위치 교환
                mat_c[nr][nc] = (num, (d + i) % 8)
                if mat_c[r][c][0] != 0:
                    fishes[num] = (nr,nc,(d+i)%8)
                    fishes[num1] = (r,c,nd)
                else:
                    fishes[num] = (nr,nc,(d+i)%8)
                    if num1 != 0:
                        del fishes[num1]
                break

def simulation(ma,shark,eat):
    global fishes
    mat_c = []
    for m in ma:
        mat_c.append(m.copy())
    fish_move(mat_c)

    shark_nomi = []
    sr,sc,sd = shark[0],shark[1],shark[2]
    for i in range(3): # 최대 3칸이동
        nsr,nsc = sr+ (i+1)*dirs[sd][0], sc + (i+1)*dirs[sd][1]
        if 0<= nsr < 4 and 0 <= nsc <4 and mat_c[nsr][nsc][0] != 0: # 빈칸이 아니면
            shark_nomi.append((nsr,nsc))

    if not shark_nomi: # 비어있으면
        sols.append(eat)
        return

    for s_pos in shark_nomi:
        nsr,nsc = s_pos[0],s_pos[1]
        remember = mat_c[nsr][nsc] # 먹은 물고기 정보, num,dir
        remember_fishes = fishes.copy()
        mat_c[nsr][nsc] = (-1,remember[1])
        mat_c[sr][sc] = (0,0)
        if remember[0] != 0:
            del fishes[remember[0]]


        simulation(mat_c,(nsr,nsc,remember[1]), eat+remember[0])
        mat_c[nsr][nsc] = (remember[0],remember[1]) # 먹은 물고기 정보 복구
        mat_c[sr][sc] = (-1,sd)
        fishes = remember_fishes

mat = []
for i in range(4):
    a = list(map(int,read().split()))
    aa = []
    for j in range(4):
        aa.append( (a[2*j],a[2*j+1]) ) # 번호 / 방향
        fishes[a[2*j]] = (i,j,a[2*j+1]) # 번호 : 좌표 / 방향
    mat.append(aa)


sols = []
eat,sd = mat[0][0][0],mat[0][0][1]
del fishes[eat] # 먹힘
mat[0][0] = (-1,sd) # 상어 == -1
shark = (0,0,sd)

simulation(mat,shark,eat)
print(max(sols))