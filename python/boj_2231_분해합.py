import sys

read = sys.stdin.readline

N = int(read())

# 모든경우를 돌아도 되지만
# 최소 (N - 자리수 * 9) 탐색 하면 최적화 가능
flag = 1
start = max(0, N - len(str(N))*9)

for i in range(start, N ):
    M, si = 0, str(i)
    
    for j in si:
        M += int(j)
    M += i
    if M == N:
        print(i)
        flag = 0
        break

if flag:
    print(0)