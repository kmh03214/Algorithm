# N <= 11 -> 11! 3000만이라 permutation으로도 가능할 듯. 2초이내
import sys
from itertools import permutations

read = sys.stdin.readline
N = int(read())
arr = list(map(int,read().split()))
oper_map = {0:'+',1:'-',2:'*',3:'//'}
opers = [ oper_map[idx] for idx,v in enumerate(map(int,read().split())) for v in range(v) ]

sol = []
for oper in set([p for p in permutations(opers,len(opers) )]):
    s = arr[0]
    for i in range(1,len(arr)):
        if oper[i-1] == '//' and s < 0:
            s = -1*eval(str(abs(s)) + oper[i-1] + str(arr[i]))
        else:
            s = eval(str(s) + oper[i-1] + str(arr[i]))
    sol.append(s)
print(max(sol))
print(min(sol))