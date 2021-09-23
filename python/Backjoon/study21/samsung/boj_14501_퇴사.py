import sys
read = sys.stdin.readline
N = int(read())
TP = [list(map(int,read().split())) for i in range(N)]

# Ti,Pi
DP_table = {}
def dp(i):
    if i > N-1 or i + TP[i][0] > N:
        return 0
    
    if i not in DP_table:
        DP_table[i] = max(dp(i+TP[i][0])+TP[i][1], dp(i+1))
        return DP_table[i]
    else:
        return DP_table[i]

dp(0)
if 0 in DP_table:
    print(DP_table[0])
else:
    print(TP[0][1])

