def solution(table, languages, preference):
    ret = {}
    for tb in table:
        a = tb.split()
        job = a[0]
        for idx, lang in enumerate(languages):
            for i in range(1,6):
                if lang == a[i]:
                    if job in ret:
                        ret[job] += (preference[idx] * (6-i))
                    else:
                        ret[job] = (preference[idx] * (6-i))
    sol, score = '', 0
    for key in ret:
        if ret[key] > score:
            sol,score = key, ret[key]
        elif ret[key] == score:
            sol = min(sol,key)
            
    return sol


########## 2번














def solution(inp_str):
    table = {}
    for i in range(65,91):
        table[i] = 1
    for i in range(97,123):
        table[i] = 2
    for i in range(48,58):
        table[i] = 3
    for s in "~!@#$%^&*":
        table[ord(s)] = 4
    
    answer = []
    fg = [0,0,0,0,0,0]
    tmp_grp,tmp_same,bef_s,cnt = {},{},'',1
    
    for s in inp_str:
        if not fg[0]:
            if not (8 <= len(inp_str) <= 15):
                answer.append(1)
                fg[0] = 1
        if ord(s) not in table: # 2조건
            if fg[2] == 0:
                answer.append(2)
                fg[2] = 1
        else: # 3조건
            grp = table[ord(s)]
            if grp not in tmp_grp:
                tmp_grp[grp] = 1
                
                
        if not fg[5]: # 5조건
            if ord(s) not in tmp_same:
                tmp_same[ord(s)] = 1
            else:
                tmp_same[ord(s)] += 1
            
            if tmp_same[ord(s)] == 5:
                fg[5] = 1
                answer.append(5)
                
        if not fg[4]:
            if bef_s == s:
                cnt += 1
            else:
                cnt = 1
                
            if cnt == 4:
                fg[4] = 1
                answer.append(4)
            bef_s = s
    if len(tmp_grp) < 3:
        fg[3] = 1
        answer.append(3)
    answer.sort()
    if not answer:
        answer.append(0)
    
    return answer