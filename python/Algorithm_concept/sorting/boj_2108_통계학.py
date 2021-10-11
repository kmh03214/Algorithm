import sys
read = sys.stdin.readline
N = int(read())

# 50만
# 산술평균 -> O(N)
# 중앙값 -> O(1)
# 최빈값 -> O(1) dict 여러개일 때, 최빈값 중 두번째로 작은 값
# 범위 : 최대 - 최소
