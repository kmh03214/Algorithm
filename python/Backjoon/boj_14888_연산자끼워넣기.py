import sys
import itertools
read = sys.stdin.readline

N = int(read())
numbers = read().split()
oper = ['+','-','*','//']
oper_idx = list(map(int,read().split()))
opers = []
for idx in range(4):
    for i in range(oper_idx[idx]):
        opers.append(oper[idx])

opers_com = [[0]+list(com) for com in set(itertools.permutations(opers,N-1))]
sol = []
for oper in opers_com:
    for i in range(N):
        if i == 0:
            s = numbers[i] # str
            continue
        if oper[i] == '//' and s[0] == '-':
            s = str(abs(int(s)))
            s = '-' + str(eval(s + oper[i] + numbers[i])) # str
            continue
        s = str(eval(s + oper[i] + numbers[i])) # str
    sol.append(int(s))
print(max(sol))
print(min(sol))