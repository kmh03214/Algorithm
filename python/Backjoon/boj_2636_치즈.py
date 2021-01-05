import sys
read = sys.stdin.readline
N,M = map(int,read().split())
mat = []
for i in range(N):
    a = list(map(int, read().split()))
    mat.append(a)
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def search(start):
    check = {start:1}
    q = [start]
    ret = []
    while q:
        Next = []
        for v in q:
            r,c = v[0],v[1]
            for i in range(4):
                nr,nc = r+dx[i],c+dy[i]
                if 0<= nr < N and 0 <= nc < M and (nr,nc) not in check and mat[nr][nc]==0:
                    check[(nr,nc)] = 1
                    Next.append((nr,nc))
        q = Next
        ret += Next
    return ret
st = search((0,0))
def bfs(start):
    check = {}
    for s in start:
        check[s] = 1
    q = st
    level = 0
    sol2 = 0
    while q:
        Next, Next_ = [],[] # Next_ 는 방금 녹은 치즈리스트
        for v in q:
            r,c = v[0],v[1]
            for i in range(4):
                nr,nc = r+dx[i], c+dy[i]
                if 0 <= nr < N and 0 <= nc < M and (nr,nc) not in check:
                    check[(nr,nc)] = 1
                    if mat[nr][nc] == 1:
                        Next_.append((nr,nc))
                        mat[nr][nc] = 0
                    else:
                        ss = search((nr,nc))
                        for s in ss:
                            if s not in check:
                                check[s] = 1
                                q.append(s)

        q = Next + Next_
        level += 1
        for m in mat:
            print(m)
        print()
        if len(Next_):
            sol2 = len(Next_)
    print(level-1)
    print(sol2)
bfs(st)



