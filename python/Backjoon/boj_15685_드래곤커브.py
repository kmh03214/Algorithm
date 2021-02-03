import sys
read = sys.stdin.readline
N = int(read())

def rotation_clock(x,y):
    # clock wise rotation(cos-90 -sin-90)
    #                    (sin-90 cos-90)
    return x*0+y*(-1),x*(1)+y*0
def translation(x,y,dx,dy): # 평행이동
    return x+dx,y+dy

total_d_curve = {}

def dragon_curve(x,y,d,g):
    d_curve_points = {(x,y):1}
    total_d_curve[(x,y)] = 1

    dxdy = [(1,0),(0,-1),(-1,0),(0,1)]
    last_point = x+dxdy[d][0],y+dxdy[d][1]
    d_curve_points[last_point] = 1
    total_d_curve[last_point] = 1
    
    for gen in range(1,g+1):
        dx,dy = 0-last_point[0], 0-last_point[1]
        p = translation(x,y,dx,dy)
        p = rotation_clock(p[0],p[1])
        p = translation(p[0],p[1],-1*dx,-1*dy)
        last_point = p
        keys = list(d_curve_points.keys())

        for point in keys:
            p = translation(point[0],point[1],dx,dy)
            p = rotation_clock(p[0],p[1])
            p = translation(p[0],p[1],-1*dx,-1*dy)

            if p not in d_curve_points:
                d_curve_points[p] = 1
                total_d_curve[p] = 1
    return d_curve_points
def check_rectangle():
    sol = 0
    for i in range(100):
        cnt = 0
        for j in range(100):
            if (i,j) in total_d_curve:
                cnt+= 1
            if (i+1,j) in total_d_curve:
                cnt+= 1
            if (i,j+1) in total_d_curve:
                cnt+= 1
            if (i+1,j+1) in total_d_curve:
                cnt+= 1

            if cnt == 4:
                sol+=1
                cnt = 0
            else:
                cnt = 0
    return sol
            

for i in range(N):
    x,y,d,g = map(int,read().split())
    dragon_curve(x,y,d,g)

print(check_rectangle())
