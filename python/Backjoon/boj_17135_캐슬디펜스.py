import sys

def combinations(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations(arr[i+1:],r-1):
                yield next + [arr[i]]

read = sys.stdin.readline
N,M,D = map(int, read().split()) # row , column, distance
enemy_positions, archers_positions = [], list(combinations([[0,j] for j in range(M)] ,3))

for i in range(N):
    a = list(map(int,read().split()))
    for j in range(M):
        if a[j] == 1:
            enemy_positions.append((N-i,j))

sol = []
for archers_pos in archers_positions:
    copy_enemy_positions = enemy_positions.copy()
    cnt = 0
    while copy_enemy_positions:
        will_remove_enemy = []
        for a_pos in archers_pos:
            near_enemy = []
            dist1 = 0
            for e_pos in copy_enemy_positions:
                dist = abs(a_pos[0] - e_pos[0]) + abs(a_pos[1] - e_pos[1])
                if dist <= D:
                    near_enemy.append((dist, e_pos))
                    dist1 = dist
            near_enemy.sort(key = lambda x: (x[0],x[1][1]) )

            try:
                will_remove_enemy.append(near_enemy[0])
            except:
                pass
        for r_enemy in will_remove_enemy:
            try:
                copy_enemy_positions.remove(r_enemy[1])
                cnt += 1
            except:
                pass
        
        tmp = []
        for i in range(len(copy_enemy_positions)):
            if copy_enemy_positions[i][0] == 1:
                pass
            else:
                tmp.append([copy_enemy_positions[i][0]-1,copy_enemy_positions[i][1]])
        copy_enemy_positions = tmp
        
    sol.append(cnt)
print(max(sol))       

