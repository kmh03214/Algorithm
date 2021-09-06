# 1. 일단 간다.
# 2. 뒤에가 더 비싸다면, 앞에서 싼가격에 해당 거리만큼 더 충전한다.
# 2. min값이 나오면 끝낸다.

import sys
read = sys.stdin.readline
N = int(read())
dist = list(map(int,read().split()))
oil_price = list(map(int,read().split()))
oil_price.pop()
m, before, sol = min(oil_price), 10000000001 ,0

for i in range(len(oil_price)):
    if oil_price[i] == m:
        sol += (m * sum(dist[i:]))
        break
    if oil_price[i] >= before:
        sol += before*dist[i]
    else:
        before = oil_price[i]
        sol += before*dist[i]
print(sol)

