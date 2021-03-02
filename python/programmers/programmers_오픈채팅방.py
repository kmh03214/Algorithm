def solution(record):
    nick_table,answer,order_table = {},[],{'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    
    for rec in record:
        r = rec.split()
        if r[0] == 'Enter':
            nick_table[r[1]] = r[2]
            answer.append((r[1],order_table[r[0]]))
        elif r[0] == 'Leave':
            answer.append((r[1],order_table[r[0]]))
        else:
            nick_table[r[1]] = r[2]
    
    return [nick_table[ans[0]] + ans[1] for ans in answer]