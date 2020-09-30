import sys
read = sys.stdin.readline
n = int(read())
weight_heights = []
for i in range(n):
    weight_heights.append(list(map(int,read().split())))

sol = []
for i in range(n):
    cnt = 0
    for wh in weight_heights:
        if weight_heights[i][0] < wh[0] and weight_heights[i][1] < wh[1]:
            cnt += 1
    sol.append(cnt)

[print(i+1, end=' ') for i in sol]