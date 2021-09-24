import sys
read = sys.stdin.readline
N = int(read())
TP = [list(map(int,read().split())) for i in range(N)]

# 정의 dp(i) -> i일 이후로 상담가능한 최대값
# 상담한다 or not
dp_table = {}
def dp(i):
    if i > N-1:
        return 0
    
    if i not in dp_table:
        dp_table[i] = max( [ dp(i+TP[i][0]) + TP[i][1] for j in range(1) if i+TP[i][0] <= N ] + [dp(i+1)] )
        return dp_table[i]
    else:
        return dp_table[i]

print(dp(0))

