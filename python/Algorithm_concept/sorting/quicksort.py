import sys
read = sys.stdin.readline
N = int(read())
arr = list(map(int,read().split()))
# arr = [10,5,25,8,91,50,20,2,1,21]
# (10), 5, 1 8 2 50 20 91 25 21
# 2 5 1 8 (10) 50 20 91 25 21

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    left = []
    right = []
    pv, p = arr[0], 0
    for i in range(1,len(arr)):
        if pv > arr[i]:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quick_sort(left) + [pv] + quick_sort(right)

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

print(sorted(arr))
arr = quick_sort(arr)
print(arr)