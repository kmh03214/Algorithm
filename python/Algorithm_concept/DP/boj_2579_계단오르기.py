import sys
read = sys.stdin.readline
N = int(read())
S = [0] + [int(read()) for i in range(N)]

dp_table = {} # memo S(i,k) = val.

def dp(stair,cnt):
    if stair > N or cnt >= 3:
        return -100000000000
    if stair == N and cnt <= 3:
        return S[N]
    
    if (stair,cnt) in dp_table:
        print(stair,cnt)
        return dp_table[(stair,cnt)]
    else:
        dp_table[(stair,cnt)] = max(dp(stair+1,cnt+1),dp(stair+2, 1)) + S[stair]
        print(dp_table)
        return dp_table[(stair,cnt)]

print(dp(0,0))


