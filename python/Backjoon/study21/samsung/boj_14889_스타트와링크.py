import sys
from itertools import combinations

read = sys.stdin.readline
N = int(read())
mat = [list(map(int,read().split())) for i in range(N)]
arr = [ i for i in range(N)]
def score(iters,s=0):
    iters = list(iters)
    for i in range(len(iters)):
        for j in range(i+1,len(iters)):
            s += (mat[iters[i]][iters[j]] + mat[iters[j]][iters[i]])
    return s
sol = []
for combi in combinations(arr, N//2):
    comp = set(arr).difference(set(combi))
    sol.append(abs(score(comp)-score(combi)))
print(min(sol))