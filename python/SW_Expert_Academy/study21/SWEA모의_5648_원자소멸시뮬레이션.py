dd = [(0,1),(0,-1),(-1,0),(1,0)]
def move(atoms):
    ret,E = {}, 0
    for (x,y) in atoms:
        d,k = atoms[(x,y)][0]
        nx,ny = x+dd[d][0], y+dd[d][1]
        if -1000<= nx <= 1000 and -1000 <= ny <= 1000:
            if (nx,ny) in atoms and (atoms[(nx,ny)][0][0] + d)%4 == 1: # 방향반대(1.5초후 부딪힘)
                E += k
                continue
            if (nx,ny) not in ret:
                ret[(nx,ny)] = [(d,k)]
            else:
                ret[(nx,ny)].append((d,k))
    next_atoms = {}
    for r in ret:
        atoms_ = ret[r]
        if len(atoms_) > 1:
            E += sum([k for d,k in atoms_])
            continue
        next_atoms[r] = ret[r]
    return next_atoms, E

T = int(input())
for test in range(1,T+1):
    N = int(input())
    atoms, sol = {}, 0
    for i in range(N):
        x,y,d,k = map(int,input().split())
        atoms[(x,y)] = [(d,k)]
    
    while atoms:
        atoms,s = move(atoms)
        sol += s
    print("#%d %d"%(test,sol))