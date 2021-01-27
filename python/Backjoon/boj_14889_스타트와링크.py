import sys,itertools
read = sys.stdin.readline

def cal_power(team,s=0):
    for com in itertools.combinations(team,2):
        s += (power_table[com[0]][com[1]] + power_table[com[1]][com[0]])
    return s

N = int(read())
power_table, humans = [],[i for i in range(N)]
for i in range(N):
    a = list(map(int,read().split()))
    power_table.append(a)
sol = 100000000
combination = list(itertools.combinations(humans,N//2))
for i in range(len(combination)//2):
    team_a,team_b = combination[i],combination[-i-1]
    sol = min(sol, abs(cal_power(team_a) - cal_power(team_b)))
    
print(sol)
