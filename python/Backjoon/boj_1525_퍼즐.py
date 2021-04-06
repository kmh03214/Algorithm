import sys
read = sys.stdin.readline
destination = ''
for i in range(3):
    destination += ''.join(read().split())

check = {'123456780':1}
def change(string,pos1,pos2):
    mem = string[pos1]
    string = string.replace(string[pos1],string[pos2])
    return string[:pos2] + mem + string[pos2+1:]

def search(state,zero_pos):
    q,cnt = [[state,zero_pos]], 0
    while q:
        Next = []
        for st, zp in q:
            for i in [-1,1,-3,3]:
                if (zp == 2 or zp == 5) and i == 1:
                    continue
                if (zp == 3 or zp == 6) and i == -1:
                    continue
                nzp = zp + i
                if 0 <= nzp < 9:
                    nst = change(st,zp,nzp)
                    if nst == destination:
                        return cnt
                    if nst not in check:
                        Next.append([nst,nzp])
                        check[nst] = 1
        q = Next
        cnt += 1
    return -2
if destination == '123456780':
    print(0)
else:
    print(search('123456780',8)+1)

# import sys
# read = sys.stdin.readline
# mat = []
# for i in range(3):
#     a = list(map(int,read().split()))
#     mat.append(a)
# check,dx,dy = {'123456780':1},[1,-1,0,0],[0,0,1,-1]

# state = ''.join([str(s) for s in mat[0]] + [str(s) for s in mat[1]]+ [str(s) for s in mat[2]] )
# def dfs(mat,r,c,depth):
#     if state == '123456780':
#         return 0
#     q = [(mat,r,c)]
#     lv = 0
#     while q:
#         Next = []
#         for m,r,c in q:
#             for i in range(4):
#                 nr,nc = r+dx[i] , c+dy[i]
#                 if 0 <= nr < 3 and 0 <= nc < 3:
#                     m[nr][nc], m[r][c] = m[r][c], m[nr][nc]
#                     cur_state = ''.join([str(s) for s in m[0]] + [str(s) for s in m[1]]+ [str(s) for s in m[2]])
#                     if cur_state == state:
#                         return lv+1
#                     if cur_state not in check:
#                         n_mat = []
#                         for ma in m:
#                             n_mat.append(ma.copy())
#                         Next.append((n_mat,nr,nc))
#                         check[cur_state] = 1
#                     m[nr][nc], m[r][c] = m[r][c], m[nr][nc]
                    
#         q = Next
#         lv += 1
#     return -1
# def solvable(tiles):
#     count = 0
#     for i in range(8):
#         for j in range(i+1, 9):
#             if tiles[j] and tiles[i] and tiles[i] > tiles[j]:
#                 count += 1
#     return count % 2 == 0
# if solvable(list(map(int,' '.join(state).split()))):
#     print(dfs([[1,2,3],[4,5,6],[7,8,0]],2,2,0))
# else:
#     print(-1)

