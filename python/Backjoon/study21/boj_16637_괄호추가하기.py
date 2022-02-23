import sys
read = sys.stdin.readline
N = int(read())

# 연산만큼 괄호 N//2
poly = ['(' for i in range((N//2)-1)]
oper = {'+':1,'-':1,'*':1}
position = [] 
cnt = 0
for s in read()[:-1]:
    poly.append(s)
    cnt += 1
    if cnt == 1 or cnt == N:
        continue
    if s not in oper:
        poly.append(')')
        position.append(len(poly)-1)

print(poly)
print(''.join(poly))
print(position)

from itertools import product

for p in product([0,1],repeat = len(position)):
    poly_c = poly.copy()
    cnt = 0
    for fg,idx in zip(p,position):
        if fg == 1:
            poly_c[idx] = '('
            poly_c[idx],poly_c[idx-1] = poly_c[idx-1],poly_c[idx]
            poly_c.append(')')
            cnt+=1
    print(''.join(poly_c[cnt:]))
    try:
        print(eval(''.join(poly_c)))
    except:
        continue


# check = {}
# def dfs():
#     if len(check) == len(position):
#         print(check)
#         return
#     for v in position:
#         if v not in check:
#             check[v] = 1
#             dfs()
#             del check[v]


