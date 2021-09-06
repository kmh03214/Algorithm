


# 100 / 6 -> 16.666

# 10 * 6 = 60

# 20 * 4 = 80

# 30 * 1 = 30

import sys
read = sys.stdin.readline
N = int(read())
ropes = [int(read()) for i in range(N)]
ropes.sort()
before,w = 0,0
for i in range(N):
    if ropes[i] != before:
        w, before = max(w,ropes[i]*(N-i)), ropes[i]
    else:
        continue

print(w)

