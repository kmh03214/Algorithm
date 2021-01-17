a = []
N = int(input())
DP_table = {}

for i in range(N):
    T,P = map(int,input().split())
    a.append((T,P))

def solution(a):
    l = len(a)
    if l == 0:
        return 0
    if l < a[0][0]:
        return solution(a[1:])
    if l not in DP_table:
        DP_table[l] = max(solution(a[1:]), solution(a[(a[0][0]):])+a[0][1])    
    return DP_table[l]
print(solution(a))