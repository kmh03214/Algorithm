# 50만
# 산술평균 -> O(N)
# 중앙값 -> O(1)
# 최빈값 -> O(1) dict 여러개일 때, 최빈값 중 두번째로 작은 값
# 범위 : 최대 - 최소
import sys
read = sys.stdin.readline
N = int(read())
arr,cnt = [], {}
S = 0
for i in range(N):
    a = int(read())
    if a not in cnt:
        cnt[a] = 1
    else:
        cnt[a] += 1
    S += a
    arr.append(a)
arr.sort()
many = sorted(cnt.items(), key = lambda x:(x[1],-x[0]), reverse=True)
if len(many)>1 and many[0][1] == many[1][1]:
    many_ = many[1][0]
else:
    many_ = many[0][0]
print(round(S/N))
print(arr[N//2])
print(many_)
print(arr[-1]-arr[0])
