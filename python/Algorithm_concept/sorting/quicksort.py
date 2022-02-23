import sys
sys.setrecursionlimit(50000)
read = sys.stdin.readline
N = int(read())
arr = [int(read()) for i in range(N)]
# arr = [10,5,25,8,91,50,20,2,1,21]
# (10), 5, 1 8 2 50 20 91 25 21
# 2 5 1 8 (10) 50 20 91 25 21

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     left = []
#     right = []
#     pv, p = arr[0], 0
#     for i in range(1,len(arr)):
#         if pv > arr[i]:
#             left.append(arr[i])
#         else:
#             right.append(arr[i])
#     return quick_sort(left) + [pv] + quick_sort(right)

# def partition(s,e,p):
#     while s < e:
#         while s < e and arr[s] <= arr[p]:
#             s += 1
#         while s < e and arr[e] >= arr[p]:
#             e -= 1
#         arr[s],arr[e] = arr[e],arr[s]
#         s+=1
#         e-=1
#     arr[e],arr[p] = arr[p],arr[e]
#     return e # next_pivot

# def quick_sort(l,r,pivot):
#     if l > r :
#         return
#     p = partition(l,r,pivot)
    
#     quick_sort(l, p-1 ,l) # (왼) p 오
#     quick_sort(p+1, r ,p+1) #  왼 p (오)

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복 
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(arr, 0, len(arr) - 1)
for s in arr:
    print(s)
