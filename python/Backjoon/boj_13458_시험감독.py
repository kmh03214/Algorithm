N  = int(input())
T = list(map(int,input().split()))
S1,S2 = map(int,input().split())
s = 0
for i in range(N):
    if T[i]-S1 < 0:
        s = s+1
    else:
        if (T[i]-S1)%S2 == 0:
            s = s + ((T[i]-S1)//S2) + 1
        else:
            s = s + ((T[i]-S1)//S2) +1 + 1
print(s)

