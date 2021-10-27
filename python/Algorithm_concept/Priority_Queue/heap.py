import sys
read = sys.stdin.readline
class heapq():
    def __init__(self, arr):
        self.arr = arr
        self.heapify()
    
    def heapify(self):
        #            0
        #      1            2
        #   3     4      5     6
        #  7 8   9 10  11 12 13 14
        for i in range(len(self.arr)//2):
            if 2*i+2 < len(self.arr):
                root = self.arr[i]
                left = self.arr[2*i+1]
                right = self.arr[2*i+2]
                if root > left:
                    self.arr[i],self.arr[2*i+1] = self.arr[2*i+1],self.arr[i]
                    root,left = left,root
                if root > right:
                    self.arr[i],self.arr[2*i+2] = self.arr[2*i+2],self.arr[i]
                    root,right = right,root
            else:
                root = self.arr[i]
                left = self.arr[2*i+1]
                if root > left:
                    self.arr[i],self.arr[2*i+1] = self.arr[2*i+1],self.arr[i]
                    root,left = left,root
    def heappush(self,a):
        self.arr.append(a)
        idx = len(self.arr)-1
        # 5,6 -> 2
        root_idx = (idx-1)//2
        while self.arr[root_idx] > self.arr[idx]:
            self.arr[root_idx], self.arr[idx] = self.arr[idx], self.arr[root_idx]
            idx = root_idx
            root_idx = (idx-1)//2
            if root_idx < 0 or idx < 0:
                break
    def heappop(self):
        if self.arr:
            self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
            ret = self.arr.pop()
            self.heapify()
            return ret
        else:
            return 0

N = int(read())
heapq = heapq([])
for i in range(N):
    x = int(read())
    if x > 0:
        heapq.heappush(x)
    else:
        print(heapq.heappop())


#    1
#  2   1 
# 5 3 4  3
# heapq = heapq([5,1,3,2,3,4])
# print(heapq.arr)
# heapq.heappush(1)
# print(heapq.arr)
# for i in range(len(heapq.arr)):
#     print(heapq.heappop())