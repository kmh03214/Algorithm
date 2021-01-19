import sys
read = sys.stdin.readline

dx, dy = [1,-1,0,0], [0,0,1,-1]

R,C,N = map(int,read().split()) # N초가 지난 후 격자판 상태 출력.
mat, check = [], [[0 for i in range(C)] for j in range(R)]

for i in range(R):
    a = list(' '.join(read()).split())
    for j in range(C):
        if a[j] == 'O':
            check[i][j] = 1
    mat.append(a)


def func(q):
    # 3초 된 폭탄 터트리기
    for v in q:
        mat[v[0]][v[1]] = '.'
        check[v[0]][v[1]] = 0
        for i in range(4):
            nx,ny = v[0]+dx[i], v[1]+dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                mat[nx][ny] = '.'
                check[nx][ny] = 0

q = []
for time in range(20):
    if q:
        func(q)
        q = []
        if N%4 + 4 == time:
            break
    else:
        if N < 4 :
            if N%4 == time:
                break
        elif N > 4:
            if N%4 +4 == time:
                break

    if time == 0: # 폭탄 시간증가
        for i in range(R):
            for j in range(C):
                if mat[i][j] == 'O':
                    check[i][j] += 1
        continue
    # 폭탄설치 및 시간증가
    for i in range(R):
        for j in range(C):
            if mat[i][j] == '.':
                mat[i][j] = 'O'
            check[i][j] += 1

            if check[i][j] == 4: # 3초가 된 폭탄 저장
                q.append((i,j))

for m in mat:
    print(''.join(m))
# 0 예외처리 / 4, 8 / 1,5,9 / 2,6,10 / 3, 7, 11
