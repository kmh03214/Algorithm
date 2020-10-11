def solution(N, stages):
    stage = [0]*(N+2)
    for i in range(len(stages)):
        stage[stages[i]] += 1
    
    s,fail_rate_list = sum(stage),[]
    for st,clear_num in enumerate(stage):
        if st == 0 or st == N+1:
            continue
        if s == 0:
            fail_rate_list.append((st,0))
            continue
        fail_rate = clear_num/s
        fail_rate_list.append((st, fail_rate))
        s-=clear_num
        
    fail_rate_list.sort(reverse = True,key = lambda x: x[1])
    return [i[0] for i in fail_rate_list]