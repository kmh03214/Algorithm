import sys
read = sys.stdin.readline
mat, color_paper_number = [], [-1,5,5,5,5,5] # 색종이 맵(10x10), 색종이갯수
for i in range(10):
    mat.append(list(map(int,read().split())))
s = []
def is_rectangle(r,c,length):
    return sum([sum(mat[r+l][c:c+length]) for l in range(length)]) // length**2 if r+length < 11 else 0

def cover(r,c,size,fg): # fg 가 0이면 붙이기 1이면 떼기
    for i in range(r, r + size):
        for j in range(c, c + size):
            mat[i][j] = fg

def is_end(): # ret이 0 이면 전체 커버 아니면 실패.
    return sum( [sum(mat[i]) for i in range(10)] )

def find_one():
    for r in range(10):
        for c in range(10):
            if mat[r][c] == 1:
                return r,c

def solution(r,c):
    if not is_end(): # 전체커버 됐으면 종료
        return 25 - (sum(color_paper_number) + 1 ) # 색종이 쓴 갯수
    
    r,c = find_one()
    for size in range(5,0,-1):
        if is_rectangle(r,c,size) and color_paper_number[size] > 0 and (r is not None and c is not None):
            cover(r,c,size,0) # 색종이 붙이기
            color_paper_number[size] -= 1  
            sol = solution(r,c)
            if sol:
                s.append(sol)
            cover(r,c,size,1) # 색종이 떼기
            color_paper_number[size] += 1

if not is_end():
    print(0)
else:
    solution(0,0)
    if s:
        print(min(s))
    else:
        print(-1)