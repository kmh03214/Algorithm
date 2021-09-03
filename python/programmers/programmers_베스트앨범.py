def solution(genres, plays):
    answer = []
    plays_cnt = {} # (genre : cnt)  len < 100
    plays_idx = {} # (genre : [(idx,plays)] )
    
    for i in range(len(genres)):
        genre, play_cnt = genres[i], plays[i]
        if genre not in plays_cnt:
            plays_cnt[genre] = play_cnt
            plays_idx[genre] = [(i,play_cnt)]
        
        else:
            plays_cnt[genre] += play_cnt
            plays_idx[genre].append((i,play_cnt))
    
    while len(plays_cnt):
        max_genre = max(plays_cnt, key = lambda x:plays_cnt[x])

        target = sorted(plays_idx[max_genre], key = lambda x:x[1], reverse= True)
        for i in range(min(len(target),2)):
            answer.append(target[i][0])
        del plays_cnt[max_genre]
            
    return answer