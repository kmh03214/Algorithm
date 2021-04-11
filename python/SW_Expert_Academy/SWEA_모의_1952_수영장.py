from itertools import combinations
a = [0,1,2,3,4,5,6,7,8,9,10,11]
def simul(tm_ticket):
    if tm_ticket == 0:
        payments = 0
        for j in range(12):
            payments += min(all_day_pays[j],tickets[1])
        return payments
    sols = []
    for combi in combinations(a,tm_ticket): # 몇월에 3개월권을 쓸건지.
        check = {}
        payments = tickets[2]*tm_ticket
        for c in combi:
            check[c],check[c+1],check[c+2] = 3,3,3
        for j in range(12):
            if j not in check:
                payments += min(all_day_pays[j],tickets[1])
        sols.append(payments)
    return min(sols)

T = int(input())
for test in range(1,T+1):
    tickets = list(map(int,input().split()))
    plans = list(map(int,input().split()))
    sol = min([tickets[-1], tickets[0]*sum(plans)])
    all_day_pays = [plans[i]*tickets[0] for i in range(12)]
    print("#%d %d" %(test,min(simul(0),simul(1),simul(2),simul(3),simul(4),sol)))
    



