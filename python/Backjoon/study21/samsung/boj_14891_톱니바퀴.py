import sys
read = sys.stdin.readline
tobni = [read()[:-1] for i in range(4)]
K = int(read())
order = [list(map(int,read().split())) for i in range(K)]

# 10 1 01 1 11 / 2,-2
# 01111101
# 11001110
# 00000010
def dfs(n,k):
    if k == 1:
        tobni[n] = tobni[n][-1] + tobni[n][:-1]
    else:
        tobni[n] = tobni[n][1:] + tobni[n][0]
    for i in [-1,1]:
        nn = n+i
        if 0 <= nn < 4 and nn not in check and tobni[n][i*2+k] != tobni[nn][-i*2]:
            check[nn] = 1
            dfs(nn,-k)
for o in order:
    check = {o[0]-1 : 1}
    dfs(o[0]-1,o[1])
print( sum([(2**i)*(int(tobni[i][0])) for i in range(4)]) )