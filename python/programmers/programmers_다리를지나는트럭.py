def solution(bridge_length, weight, truck_weights):
    answer = 0
    cur_bridge, end_bridge, total_truck = [], [], len(truck_weights)
    truck_weights.reverse()    
    while len(end_bridge) != total_truck:
        answer+=1
        fg = 0
        if cur_bridge:
            if cur_bridge[0][1] == bridge_length:
                end_bridge.append(cur_bridge[0])
                fg = 1

        cur_bridge = [(w,t+1) for w,t in cur_bridge[fg:]]
        if truck_weights:
            if sum([w for w,t in cur_bridge]) + truck_weights[-1] <= weight:
                w = truck_weights.pop()
                cur_bridge.append((w,1))
        # print(answer, end_bridge, cur_bridge)        
    return answer