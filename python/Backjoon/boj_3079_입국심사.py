import sys
import heapq
read = sys.stdin.readline
N, M = map(int,read().split())
time_table = [int(read()) for i in range(N)]
Max = time_table[-1]

ratio = []
for i in range(N):
    ratio.append(Max / time_table[i])
k = M/sum(ratio)

count = []
for i in range(N):
    ratio[i] *= k
    a = int(ratio[i])
    M -= a
    count.append(a)

heap = []
for i in range(N):
    heapq.heappush(heap, [time_table[i]*(1+count[i]) ,time_table[i]*(count[i]),time_table[i]]) # 합 원본 시간

for i in range(M):
    h = heapq.heappop(heap)
    h[1] += h[2]
    h[0] += h[2]
    heapq.heappush(heap,h)
print(max(heap, key = lambda x:x[1])[1])