def move(atoms,cur_atoms):
    dx,dy = [0,0,-1,1],[1,-1,0,0]
    sol = 0
    while atoms:
        next_atoms = {}
        del_next_atoms = set()
        for atom in atoms:
            x,y = atom
            d,e = cur_atoms[(x,y)]
            nx, ny = x+dx[d],y+dy[d]
            if not (-1000 <= nx <= 10000 and -1000 <= ny <= 1000): # 범위밖 절대안만남
                continue
            if (nx,ny) in cur_atoms and (d + cur_atoms[(nx,ny)][0])%4 == 1: # 0.5초 충돌
                sol += e
                continue
            if (nx,ny) in next_atoms: # 1초 충돌
                sol += e # e추가
                del_next_atoms.add((nx,ny))
                continue
            next_atoms[(nx,ny)] = (d,e)
        for s in del_next_atoms:
            sol += next_atoms[s][1]
            del next_atoms[s]
        atoms = list(next_atoms.keys())
        cur_atoms = next_atoms
    return sol

T = int(input())
for test in range(T):
    N = int(input())
    atoms = []
    cur_atoms = {}
    for i in range(N):
        x,y,d,e = map(int,input().split())
        cur_atoms[(x,y)] = (d,e)
        atoms.append((x,y))
    print('#%d %d'%(test+1,move(atoms,cur_atoms)))


# 2
# 4
# -1000 0 3 5
# 1000 0 2 3
# 0 1000 1 7
# 0 -1000 0 9
# 4
# -1 1 3 3
# 0 1 1 1
# 0 0 2 2
# -1 0 0 9
