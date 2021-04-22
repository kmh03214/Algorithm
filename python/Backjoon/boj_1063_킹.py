import sys
read = sys.stdin.readline
king, stone, N = read().split()
N = int(N)

col = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}
decode_col = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H'}
row = {'1':7,'2':6,'3':5,'4':4,'5':3,'6':2,'7':1,'8':0}
decode_row = {7:'1',6:'2',5:'3',4:'4',3:'5',2:'6',1:'7',0:'8'}

king = (row[king[1]],col[king[0]])
stone = (row[stone[1]],col[stone[0]])

direct = {'R':(0,1),'L':(0,-1),'B':(1,0),'T':(-1,0),'RT':(-1,1),'LT':(-1,-1),'RB':(1,1),'LB':(1,-1)}

def move(king,stone,order):
    d = direct[order]
    x,y = king
    nx,ny = x+d[0],y+d[1]
    if 0<= nx < 8 and 0<= ny < 8:
        if (nx,ny) == stone:
            sx,sy = stone
            nsx,nsy = sx+d[0],sy+d[1]
            if 0<= nsx < 8 and 0 <= nsx < 8:
                stone = (nsx,nsy)
                king = (nx,ny)
        else:
            king = (nx,ny)
    else:
        king = (x,y)
    return king, stone

for i in range(N):
    order = read().split()
    king,stone = move(king,stone,order[0])
print(decode_col[king[1]]+decode_row[king[0]])
print(decode_col[stone[1]]+decode_row[stone[0]])

