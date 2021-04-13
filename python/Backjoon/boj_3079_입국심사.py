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


# for i in range(M):
#     m = 
#     m[0] += m[1]
# print(max(priority)[0])


# 9 1000000000
# 3261135
# 1807
# 43
# 7
# 3
# 2
# 1
# 1
# 1
# 답 : 250000001

# 13 1000000000
# 3258830
# 1807
# 43
# 7
# 3
# 2
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 답 : 125000001




# for i in range(M):
#     count[i] += 1

# print(max([i*j for i,j in zip(time_table,count)]))

# if N == 1:
#     print(M*sol_table[0][0])
# else:
#     for i in range(1,M):
#         if time_table:
#             min_table = min(sol_table, key = lambda x : x[0]*x[1])
#             min_table[1] += 1
#             if min_table[0] * min_table[1] > time_table[-1]:
#                 sol_table.append([time_table.pop(),1])
#                 min_table[1] -= 1
#         else:
#             sol_table.sort()
#             min_table, second_min_table = sol_table[0], sol_table[1]
#             min_table[1] += 1
#             if min_table[0] * min_table[1] > second_min_table[0] * (second_min_table[1]+1):
#                 second_min_table[1] += 1
#                 min_table[1] -= 1
#     sol = max(sol_table, key = lambda x : x[0]*x[1])
#     print(sol[0]*sol[1])