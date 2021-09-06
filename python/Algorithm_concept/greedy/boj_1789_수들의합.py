# (n-1)(n) /2 < S < (n)(n+1) / 2
# n^2 - n < 2*S < n^2+n
# ( n - (1/2) )**2 < 2*S + 1/4 < ( n + (1/2) )**2 
# n - 1/2 < (2*S + 1/4)^0.5 < n + 1/2
# n < (2*S + 1/4)^0.5 + 1/2 < n + 1
print( int((2*int(input()) + 1/4)**0.5 + 1/2) - 1)


# S,n,s = int(input()),1,0
# while s<S:
#     s, n = (n*(n+1))/2, n+1
# if s == S:
#     print(n-1)
# else:
#     print(n-2)
