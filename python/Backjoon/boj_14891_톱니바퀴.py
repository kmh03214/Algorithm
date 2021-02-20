import sys
read = sys.stdin.readline
last_num = 4
def rot(N,d):
    left, right = tobni[N][6], tobni[N][2]
    if d == 1:
        tobni[N] = tobni[N][7] + tobni[N][:7]
    else:
        tobni[N] = tobni[N][1:] + tobni[N][0]
    
    if N > 1 and left != tobni[N-1][2]:
        rot_l(N-1,-d)

    if N < last_num and right != tobni[N+1][6]:
        rot_r(N+1,-d)

def rot_l(N,d):
    left = tobni[N][6]
    if d == 1:
        tobni[N] = tobni[N][7] + tobni[N][:7]
    else:
        tobni[N] = tobni[N][1:] + tobni[N][0]
    if N == 1:
        return
    if left != tobni[N-1][2]:
        rot_l(N-1,-d)

def rot_r(N,d):
    right = tobni[N][2]
    if d == 1:
        tobni[N] = tobni[N][7] + tobni[N][:7]
    else:
        tobni[N] = tobni[N][1:] + tobni[N][0]
    if N == last_num:
        return
    if right != tobni[N+1][6]:
        rot_r(N+1,-d)
    

# def rotation(N,d):
#     if N == 1:
#         right = tobni[N][2]
#         rot(N,d)
#         if right != tobni[N+1][6]:
#             rotation(N+1,-d)
#     elif N == last_num:
#         left = tobni[N][6]
#         rot(N,d)
#         if left != tobni[N-1][2]:
#             rotation(N-1,-d)
#     else:
#         right, left = tobni[N][2], tobni[N][6]
#         rot(N,d)
#         if right != tobni[N+1][6]:
#             rotation(N+1,-d)
#         if left != tobni[N-1][2]:
#             rotation(N-1,-d)

tobni = {}
for i in range(last_num):
    tobni[i+1] = input()

K = int(read())
for i in range(K):
    N, direction = map(int,read().split())
    rot(N,direction)
s = 0
for i in range(1,5):
    s += int(tobni[i][0])*2**(i-1)
print(s)







# import sys
# read = sys.stdin.readline
# last_num = 4
# def rot(N,d):
#     left, right = tobni[N][6], tobni[N][2]
#     if d == 1:
#         tobni[N] = [tobni[N][7]] + tobni[N][:8]
#     else:
#         tobni[N] = tobni[N][1:] + [tobni[N][0]]
    
#     if N > 1 and left != tobni[N-1][2]:
#         rot_l(N-1,-d)

#     if N < last_num and right != tobni[N+1][6]:
#         rot_r(N+1,-d)

# def rot_l(N,d):
#     left = tobni[N][6]
#     if d == 1:
#         tobni[N] = [tobni[N][7]] + tobni[N][:8]
#     else:
#         tobni[N] = tobni[N][1:] + [tobni[N][0]]
#     if N == 1:
#         return
#     if left != tobni[N-1][2]:
#         rot_l(N-1,-d)

# def rot_r(N,d):
#     right = tobni[N][2]
#     if d == 1:
#         tobni[N] = [tobni[N][7]] + tobni[N][:8]
#     else:
#         tobni[N] = tobni[N][1:] + [tobni[N][0]]
#     if N == last_num:
#         return
#     if right != tobni[N+1][6]:
#         rot_r(N+1,-d)
    

# # def rotation(N,d):
# #     if N == 1:
# #         right = tobni[N][2]
# #         rot(N,d)
# #         if right != tobni[N+1][6]:
# #             rotation(N+1,-d)
# #     elif N == last_num:
# #         left = tobni[N][6]
# #         rot(N,d)
# #         if left != tobni[N-1][2]:
# #             rotation(N-1,-d)
# #     else:
# #         right, left = tobni[N][2], tobni[N][6]
# #         rot(N,d)
# #         if right != tobni[N+1][6]:
# #             rotation(N+1,-d)
# #         if left != tobni[N-1][2]:
# #             rotation(N-1,-d)

# tobni = {}
# for i in range(last_num):
#     tobni[i+1] = ' '.join(read()).split()

# K = int(read())
# for i in range(K):
#     N, direction = map(int,read().split())
#     rot(N,direction)
# s = 0
# for i in range(1,5):
#     s += int(tobni[i][0])*2**(i-1)
# print(s)
