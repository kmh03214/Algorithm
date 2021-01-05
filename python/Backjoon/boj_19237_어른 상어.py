import sys
read = sys.stdin.readline
class shark():
    def __init__(self):
        self.curdir = None # 상어가 현재 보는 방향
        self.direction = [0] # 우선순위 방향을 담을 리스트 1,2,3,4 인덱스에 우선순위
        
    def move(self,r,c):
        # 냄새를 뿌리고 해당냄새는 K초 후 사라짐
        dirs = self.direction[self.curdir] # 우선순위 방향
        # 보는방향의 우선순위대로 움직임
        for d in dirs:
            nr, nc = r + dx[d], c + dy[d]
            # 먼저 아무냄새가 없는칸부터 이동한다.
            if 0<= nr < N and 0 <= nc < N and (nr,nc) not in smells:
            # 우선순위로 움직이는데 다른상어냄새가있으면 안감
                self.curdir = d
                smells[(nr,nc)] = K

            # 갈데가 없으면 냄새가 있는자리로 되돌아감.
        
            # 같은칸에 여러개 같이 존재하면 작으놈 빼고 다 나감



# N , M , K - 격자크기, 상어 수 , 냄새소멸시간
N,M,K = map(int,read().split())
# 격자 모습 N개 0 은 빈칸, 0이아닌수는 상어 번호
mat = []
sharks = {} # 해당번호 상어를 관리할 딕셔너리
smells = {} # 냄새를 남긴 곳을 저장할 딕셔너리

for i in range(N):
    a = list(map(int,read().split()))
    for j in range(N):
        if a[j] != 0:
            # 상어 위치 저장
            sharks[a[j]] = shark() 
            a[j] = sharks[a[j]] # 배열에 (i,j)에 a[j]번 상어 입력됨
            smells((i,j)) = K
    mat.append(a)

# 상어 방향 1/2/3/4 = 위/아래/왼/오
tmp_dir = list(map(int,read().split()))
for i in range(len(tmp_dir)):
    sharks[i+1].curdir = tmp_dir[i]

# 상어 방향 우선순위 상어 당 4줄
for i in range(M):
    for j in range(4):
        p_dir = list(map(int,read().split()))
        sharks[i+1].direction.append(p_dir) # 해당번호 상어 우선순위 방향 위,아래,왼,오 순서대로 입력

# 1/ 2/ 3/ 4 = 위 를향할때 우선순위/ 아래/ 왼/ 오
dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1]

# 1번 상어만 격자에 남게 되기까지 걸리는 시간 출력 1000초 넘으면 -1 출력
