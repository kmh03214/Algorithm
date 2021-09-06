import sys
read = sys.stdin.readline

N = int(read())

q,r = N//5, N%5
if r == 3:
    print(q+1)
elif r == 1 or r == 4:
    if q-1 >= 0:
        print( (q-1) + (r+5)//3)
    else:
        print(-1)
elif r == 2:
    if q-2 >= 0:
        print( (q-2) + (r+10)//3 )
    else:
        print(-1)
else:
    print(q)

# 가장 빠른 풀이?
# n = int(input())

# a = n//5
# b = n%5
# c = 0

# while a>=0:
#     if b%3 == 0:
#         c = b//3
        
#         break
#     a -= 1
#     b += 5
        
# if b%3 == 0:
#     print(a+c)
# else:
#     print(-1)