from itertools import product
p1 = [[1,2,3],[1,2],[4,5]]
for pro in product(*p1,repeat=1):
    print(pro)