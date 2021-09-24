N = int(input())
arr = list(map(int,input().split()))
A,B = map(int,input().split())
print(sum(list(map(lambda x : (x-A)//B+2 if (x-A)%B > 0 and x-A > 0 else [(x-A)//B+1 if x-A>=0 else 1][0], arr))))

