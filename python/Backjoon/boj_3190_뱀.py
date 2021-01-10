import sys
read = sys.stdin.readline
N = int(read())
mat = [[0 for i in range(N)] for j in range(N)]
K = int(read())
for i in range(K):
    r,c = map(int,read().split())
    mat[r-1][c-1] = 'apple' # 시작점이 1,1 기준

move_order = []
L = int(read())
btime = 0
for i in range(L):
    time, order = read().split()
    for j in range(btime, int(time)):
        move_order.append('N')
    move_order.append(order)
    btime = int(time)+1

# print(move_order) 10000초까지 필요할듯
move_order = move_order + ['N']* (10000-len(move_order))
def where(cur_dir,input_dir):
    dirs = [0,1,2,3]
    if input_dir == 'N': # 그대로 진행
        return cur_dir
    elif input_dir == 'L': # 왼쪽 90
        return dirs[cur_dir-1]
    else: # 오른쪽 90
        return dirs[(cur_dir+1)%4]

class snake():
    def __init__(self):
        self.me = {(0,0):1}
        self.length = 1
        self.direction = 1 # 상:0, 우:1, 하:2, 좌:3
        self.head = (0,0)
        self.tail = (0,0)
        self.next_tail = [(0,0)]
    
    def move(self):
        d = self.direction
        head = self.head
        tail = self.tail
        print(self.next_tail)
        if d == 0:
            head = ( head[0]-1, head[1] )
            if head in self.me: # 자기자신과 부딪힌 경우
                return 'end_me'
            if head[0] == -1: # 맵을 넘어간 경우
                return 'end_map_over'
            else:
                if mat[head[0]][head[1]] == 'apple':
                    mat[head[0]][head[1]] = 0
                    self.head = head
                    self.next_tail = [head] + self.next_tail
                    self.me[head] = 1
                else:
                    del self.me[tail] # 꼬리삭제
                    self.me[head] = 1
                    self.next_tail = [head] + self.next_tail
                    self.next_tail.pop()
                    self.tail = self.next_tail[-1]
            self.head = head
        elif d == 1:
            head = ( head[0], head[1]+1 )
            if head in self.me: # 자기자신과 부딪힌 경우
                return 'end_me'
            if head[1] == N: # 맵을 넘어간 경우
                return 'end_map_over'
            else:
                if mat[head[0]][head[1]] == 'apple':
                    mat[head[0]][head[1]] = 0
                    self.head = head
                    self.next_tail = [head] + self.next_tail
                    self.me[head] = 1
                else:
                    del self.me[tail] # 꼬리삭제
                    self.me[head] = 1
                    self.next_tail = [head] + self.next_tail
                    self.next_tail.pop()
                    self.tail = self.next_tail[-1]
            self.head = head
        elif d == 2:
            head = ( head[0]+1, head[1] )
            if head in self.me: # 자기자신과 부딪힌 경우
                return 'end_me'
            if head[0] == N: # 맵을 넘어간 경우
                return 'end_map_over'
            else:
                if mat[head[0]][head[1]] == 'apple':
                    mat[head[0]][head[1]] = 0
                    self.head = head
                    self.next_tail = [head] + self.next_tail
                    self.me[head] = 1
                else:
                    del self.me[tail] # 꼬리삭제
                    self.me[head] = 1
                    self.next_tail = [head] + self.next_tail
                    self.next_tail.pop()
                    self.tail = self.next_tail[-1]
            self.head = head
        elif d == 3:
            head = ( head[0], head[1]-1 )
            if head in self.me: # 자기자신과 부딪힌 경우
                return 'end_me'
            if head[1] == -1: # 맵을 넘어간 경우
                return 'end_map_over'
            else:
                if mat[head[0]][head[1]] == 'apple':
                    mat[head[0]][head[1]] = 0
                    self.head = head
                    self.next_tail = [head] + self.next_tail
                    self.me[head] = 1
                else:
                    del self.me[tail] # 꼬리삭제
                    self.me[head] = 1
                    self.next_tail = [head] + self.next_tail
                    self.next_tail.pop()
                    self.tail = self.next_tail[-1]
            self.head = head
        
        return 'go'
s = snake()
for i in range(len(move_order)):
    if i == 0:
        continue
    order = move_order[i]
    ret = s.move()
    s.direction = where(s.direction,order)
    if ret != 'go':
        print(ret)
        print(i)
        break


