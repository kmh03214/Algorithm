import sys
import heapq
read = sys.stdin.readline
N = int(read())
arr, sol = [int(read()) for i in range(N)], 0
heapq.heapify(arr)
while len(arr) != 1:
    s = 0
    for i in range(min(2,len(arr))):
        s += heapq.heappop(arr)
    sol += s
    heapq.heappush(arr,s)
print(sol)