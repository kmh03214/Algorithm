import sys
read = sys.stdin.readline

N = int(read())
if N < 5 and N != 3:
    print(-1)
elif N < 5 and N == 3:
    print(1)
else:
    q,r = N//5, N%5
    if r == 3:
        print(q+1)

    elif r == 1 or r == 4:
        print( (q-1) + (r+5)//3)

    elif r == 2:
        print( (q-2) + (r+10)//3 )
    
    else:
        print(q)