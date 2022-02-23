import sys
from itertools import product
read = sys.stdin.readline

N,M = map(int,read().split())
mat, cctv = [], {}
for i in range(N):
    a = list(map(int,read().split()))
    for j in range(M):
        if a[j] != 0 and a[j] != 6:
            cctv[(i,j)] = a[j]

dd = [(0,1),(1,0),(0,-1),(-1,0)]
cctv_dirs = [(0,1,2,3),(0,1),(0,1,2,3),(0,1,2,3),(0,)]





# for pro in product():
#     print(pro)


# def sup(cctv_num, dirs):
    
#     while q:


